from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holidays import Holiday
from datetime import date

@app.route("/maintenance_date", methods=["POST"])
def maintenance_date():
    dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))                 

    return render_template("result.html")
                      