from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route("/", methods=['GET', 'POST'])
def show_entries():
    return render_template("input.html")

@app.route("/input",methods=["GET","POST"])
def input():

    if str(request.form["salary"]) == "":
        flash('給与が未入力です。入力してください。')
        return redirect(url_for("output"))
    
    if int(request.form["salary"]) > 9999999999:
        flash('給与には最大9,999,999,999まで入力可能です。')
        return redirect(url_for("output"))

    if int(request.form["salary"]) < 0:
        flash('給与にはマイナスの値は入力できません。')
        return redirect(url_for("output")) 
    
    

    if request.method == "POST":
        payroll_amount = int(request.form["salary"])
        if(payroll_amount > 1000000):
            tax = 100000 + (payroll_amount - 1000000) * 0.2

        else:
            tax = payroll_amount *0.1

        tax_amount = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

        pay_amount = payroll_amount - tax_amount

    return render_template("output.html", salary=payroll_amount, pay_amount=pay_amount, tax_amount=tax_amount)

@app.route("/output",methods=["GET","POST"])
def output():
    return redirect(url_for("show_entries"))