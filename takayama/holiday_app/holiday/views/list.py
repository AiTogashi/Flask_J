from flask import render_template
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route("/list", methods=["POST"])
def list():
    holidaylist = Holiday.query.all()
    return render_template('list.html', holidaylist=holidaylist)