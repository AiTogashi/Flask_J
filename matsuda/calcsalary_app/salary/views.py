from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/',methods=['GET','POST'])
def show_entries():
    init_val = session.get("input_data",None)
    return render_template('input.html',input = init_val)

@app.route('/calculation',methods=['GET','POST'])
def calculation():
    # バリデーション
    if request.form['salary'] == "":
        flash("給与が未入力です。入力してください。")
        return redirect('/')
    
    if int(request.form["salary"]) > 9999999999:
        flash("給与には最大9,999,999,999まで入力可能です。")
        session["input_data"] = request.form['salary']
        return redirect(url_for("show_entries"))
    
    if int(request.form['salary']) < 0:
        flash("給与にはマイナスの値は入力できません。")
        session["input_data"] = request.form['salary']
        return redirect(url_for("show_entries"))
    
    # 計算
    if request.method == 'POST':
        input_saraly = int(request.form['salary'])
        if input_saraly > 1000000:
            tax_rate = 0.2
            tax = (input_saraly-1000000)*tax_rate + 1000000*0.1
        else:
            tax_rate = 0.1
            tax = input_saraly*tax_rate
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
        amount = input_saraly - tax    
        return render_template('output.html',salary=input_saraly,amount=amount,tax=tax)
