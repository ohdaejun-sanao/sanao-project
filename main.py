import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 한글 인코딩 문제 해결

@app.route("/")
def analyze_place():
    mock_data = {
        "photo_count": 25,
        "recent_reviews": 15,
        "has_new_post": True,
        "is_talktalk_responsive": True
    }

    score = 0
    details = []

    if mock_data["photo_count"] > 20:
        score += 25
        details.append({"item": "사진 품질", "status": "최적"})

    if mock_data["recent_reviews"] > 10:
        score += 25
        details.append({"item": "최신 리뷰", "status": "양호"})

    if mock_data["has_new_post"]:
        score += 25
        details.append({"item": "새소식 관리", "status": "훌륭함"})

    if mock_data["is_talktalk_responsive"]:
        score += 25
        details.append({"item": "톡톡 응답성", "status": "훌륭함"})

    result_data = {
        "store_name": "사나오 테스트 가게",
        "total_score": score,
        "details": details
    }

    # 이제 json이 아닌, sanao.html 파일을 화면에 보여주고, result_data를 전달합니다.
    return render_template('sanao.html', data=result_data)