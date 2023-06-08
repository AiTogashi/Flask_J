from flask import request, redirect, url_for, render_template, flash, session
from ipass import app

@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')