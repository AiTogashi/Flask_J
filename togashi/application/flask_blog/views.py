from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route("/")
def show_entires():
    return render_template('entries/index.html')
    