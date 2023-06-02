from flask import request,redirect,url_for,render_template,flash,session
from salary import app

def calc_salary(num):
    border_fee =1000000
    totalfee = num
    def sansyutsu (get):
        if get > border_fee :
            tax_fee_under_border = border_fee * 0.1
            fee_over_border = get - border_fee
            tax_fee_over_border = fee_over_border * 0.2
            total_tax = totalfee - tax_fee_under_border - tax_fee_over_border
            return int(total_tax)
        else:
            total_tax = totalfee * 0.9
            return int(total_tax)
    tax = totalfee - sansyutsu(totalfee)
    sikyu  =sansyutsu(totalfee)
    back_txt = str(totalfee) + "の場合、支給額:"+ str(sikyu) + "、税額:" + str(tax)
    return back_txt

def escapeprint():
    txt = "給与が未入力です。入力してください"
    return txt

@app.route('/')
def show_salary():
    return render_template('input.html')


@app.route('/calc',methods=['GET','POST'])
def calc():
    num = int(request.form['salary'])
    if request.method == 'POST':
        if num == 0:
            return render_template('input.html')
        else:
            print(calc_salary(num))
            return render_template('output.html',salary = calc_salary(num))
    else:
        return render_template('output.html',salary = escapeprint())