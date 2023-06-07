from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holidays import Holiday

@app.route("/list", methods=["POST"])
def list():
    holidaylist = Holiday.query.all()
    return render_template('list.html', holidaylist=holidaylist)
