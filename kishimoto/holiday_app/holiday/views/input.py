from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def input_html():
    return render_template('input.html')

@app.route('/input', methods=['POST'])
def input():
    return render_template('result.html')

# @app.route('/result', methods=['POST'])
# def back():
#     return render_template('input.html')