from flask import request, redirect, url_for, render_template, flash, session
from colaapp_mente import app
from colaapp_mente import db
from colaapp_mente.models.db import Holiday



@app.route("/list", methods=["POST"])
def list():
    holidaylist = Holiday.query.all()
    return render_template('list.html',holidaylist = holidaylist)