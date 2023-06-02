from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/output')
def output():
    return render_template('output.html')
@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/input',methods=['GET','POST'])
def salary():
    return render_template("output.html", salary=)

#税額計算
if salary > 1000000 :
    tax = 100000 + (salary - 1000000) * 0.2
else:
    tax = salary * 0.1

tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)


#支給額計算
pay_amount = salary - tax

# print("支給額:" + str(pay_amount) + "、" +"税額:" + str(tax), end="")