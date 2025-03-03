from flask import Flask, render_template, request

app = Flask(__name__)

# 배터리 와트 계산 함수
def calculate_watts(voltage, current):
    watts = voltage * current / 1000  # 밀리암페어를 암페어로 변환 후 계산
    if watts < 100:
        return f"와트 (W): {watts} W - 기내 반입 가능 (최대 5개)"
    elif 100 <= watts < 160:
        return f"와트 (W): {watts} W - 항공사 승인 필요 (최대 2개)"
    else:
        return f"와트 (W): {watts} W - 기내 반입 불가"

# 기본 페이지 라우팅
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 사용자로부터 입력 받기
        voltage = float(request.form["voltage"])
        current = float(request.form["current"])
        
        # 와트 계산 후 결과 반환
        result = calculate_watts(voltage, current)
        return render_template("index.html", result=result)
    
    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
