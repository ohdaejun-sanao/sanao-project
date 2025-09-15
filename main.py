from flask import Flask, render_template
# 1. WhiteNoise 보급 장비를 가져옵니다.
from whitenoise import WhiteNoise

app = Flask(__name__)

# 2. WhiteNoise를 엔진에 장착합니다.
# 이제 우리 서버는 HTML 뿐만 아니라 static 폴더의 CSS/JS 파일도 전달할 수 있습니다.
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')


def get_sanao_data():
    sanao_report_data = {
        "store_name": "사나오 프로젝트",
        "total_score": 100,
        "details": [
            {'item': '리뷰 수', 'status': '최적'},
            {'item': '리뷰 답글 최신성', 'status': '최적'},
            {'item': '새소식 관리', 'status': '최적'},
            {'item': '가격 정보', 'status': '고객 문의'},
            {'item': '휴무일', 'status': '최적'}
        ]
    }
    return sanao_report_data

@app.route('/')
@app.route('/login')
def login_page():
    return render_template('index.html') # login.html -> index.html로 변경된 것 유지

@app.route('/dashboard')
def dashboard_page():
    return render_template('main_dashboard.html')

@app.route('/report')
def report_page():
    data_for_report = get_sanao_data()
    return render_template('SANAO.html', data=data_for_report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)