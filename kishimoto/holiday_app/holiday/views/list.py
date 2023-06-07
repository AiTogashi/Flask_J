from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from decimal import Decimal, ROUND_HALF_UP
from holiday.models.mst_holiday import Holiday 

@app.route('/list', methods=['POST'])
def list():
    holidays = Holiday.query.all()
    return render_template('list.html', holidays=holidays)

@app.route('/list', methods=['POST'])
def back_list():
    return render_template('input.html')
