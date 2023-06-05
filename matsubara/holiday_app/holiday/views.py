from flask import request,redirect,url_for,render_template,flash,session
from holiday import app

@app.route('/')
def show_holiday():
    return render_template('input.html')

@app.route('/sub_up',methods =['POST'])
def sub_update():
    return render_template('result.html')


@app.route('/delete',methods =['POST'])
def deletedate():
    return render_template('list.html')

@app.route('/allview',methods = ['POST'])
def showdataset():
    return render_template('list.html')
