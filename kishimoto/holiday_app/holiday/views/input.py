from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/',methods=['POST','GET'])
def input_html():
    return render_template('input.html')

# if request.form["button"] == "insert_update":
