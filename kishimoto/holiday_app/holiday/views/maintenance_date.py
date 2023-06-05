from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/input' , methods=['POST'])
def input():
    return render_template('result.html')