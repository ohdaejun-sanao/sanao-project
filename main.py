from flask import Flask, render_template

# 1. 엔진(웹 서버) 초기화
# 앞으로 app이 우리의 웹 서버 본체입니다.
app = Flask(__name__)

# 2. SANAO.html에 사용할 데이터 생성 함수
# 기존에 터미널에 출력되던 데이터를 이곳으로 옮겼습니다.
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

# 3. 지휘 통제실 (URL 설계)
# 특정 URL 주소로 접속했을 때 어떤 HTML 화면을 보여줄지 결정합니다.

# 기본 주소 ('/') 또는 '/login'으로 접속 시, login.html을 보여줍니다.
@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')

# '/dashboard' 주소로 접속 시, main_dashboard.html을 보여줍니다.
@app.route('/dashboard')
def dashboard_page():
    return render_template('main_dashboard.html')

# '/report' 주소로 접속 시, SANAO.html에 데이터를 채워서 보여줍니다.
@app.route('/report')
def report_page():
    # 데이터 생성 함수를 호출하여 데이터를 가져옵니다.
    data_for_report = get_sanao_data()
    # 데이터를 SANAO.html에 전달하며 화면을 생성합니다.
    return render_template('SANAO.html', data=data_for_report)

# 4. 서버 가동
# 이 스크립트가 직접 실행될 때 웹 서버를 시작합니다.
if __name__ == '__main__':
    # debug=True는 개발 모드로, 코드 변경 시 서버가 자동 재시작됩니다.
    app.run(host='0.0.0.0', port=5000, debug=True)