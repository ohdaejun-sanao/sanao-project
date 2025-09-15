# -*- coding: utf-8 -*-
import json

# 이 함수가 우리의 AI 백엔드 핵심 로직입니다.
# 실제 서비스에서는 이 함수를 클라우드 서버(예: GCP Cloud Function)에 올리게 됩니다.
def analyze_place(request):
    """
    네이버 플레이스 URL을 받아, 미리 정의된 기준에 따라 점검하고 결과를 반환합니다.
    실제 구현에서는 request에서 URL을 추출하고, 웹 크롤링을 통해 데이터를 가져와야 합니다.
    이 코드는 그 핵심 로직의 '개념'을 보여주는 프로토타입입니다.
    """
    # 1. 실제로는 request에서 URL을 추출해야 합니다.
    # url = request.get_json().get('url')

    # 2. 지금은 테스트를 위해, 미리 준비된 가상 데이터를 사용합니다.
    # (실제로는 이 부분에 '주니퍼'가 만든 데이터 수집 모듈이 들어갑니다.)
    mock_data = {
        "photo_count": 25,
        "recent_reviews": 15,
        "has_new_post": True,
        "is_talktalk_responsive": True
    }

    # 3. '준수'가 설계한 분석 알고리즘에 따라 점수를 매깁니다.
    score = 0
    details = []

    # 사진 품질 체크
    if mock_data["photo_count"] > 20:
        score += 25
        details.append({"item": "사진 품질", "status": "최적"})
    else:
        details.append({"item": "사진 품질", "status": "개선 필요"})

    # 리뷰 관리 체크
    if mock_data["recent_reviews"] > 10:
        score += 25
        details.append({"item": "리뷰 최신성", "status": "최적"})
    else:
        details.append({"item": "리뷰 최신성", "status": "개선 필요"})
    
    # 새소식 관리 체크
    if mock_data["has_new_post"]:
        score += 25
        details.append({"item": "새소식 관리", "status": "최적"})
    else:
        details.append({"item": "새소식 관리", "status": "개선 필요"})

    # 고객 소통 체크
    if mock_data["is_talktalk_responsive"]:
        score += 25
        details.append({"item": "고객 소통", "status": "최적"})
    else:
        details.append({"item": "고객 소통", "status": "개선 필요"})
        
    # 4. 최종 결과를 생성합니다.
    report = {
        "score": score,
        "grade": "A+" if score >= 90 else "B",
        "details": details
    }

    # 5. 결과를 프론트엔드로 전달합니다.
    return json.dumps(report, ensure_ascii=False)

# 로컬 PC에서 테스트하기 위한 코드
if __name__ == '__main__':
    # 가상의 요청(request) 객체를 만들어 함수를 테스트합니다.
    class MockRequest:
        def get_json(self):
            return {'url': 'https://map.naver.com/p/entry/place/11591439'}

    result = analyze_place(MockRequest())
    print(result)