from flask import request, redirect, url_for, render_template, flash, session
from holiday_mentenance import app
from holiday_mentenance import db
from holiday_mentenance.models.mst_holiday import Holiday



@app.route("/list", methods=["POST"])
def list():
    holidaylist = Holiday.query.all()
    return render_template('list.html',holidaylist = holidaylist)
