from flask import request, redirect, url_for, render_template, flash, session
from colaapp_mente import app
from colaapp_mente import db
from colaapp_mente.scripts.intable import Colakind



@app.route("/list", methods=["POST"])
def list():
    colakindlist = Colakind.query.all()
    return render_template('input.html',colakindlist = colakindlist)

@app.route("/index",methods = ["POST"])
def backpage():
    return render_template('result.html')