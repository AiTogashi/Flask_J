from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holidays import Holiday
from datetime import date

@app.route("/maintenance_date", methods=["POST"])
def maintenance_date():
    if request.form["holiday"]=="":
        flash("祝日 日付を選択してください")
        if request.form["holiday_text"]=="":
            flash("祝日 テキストを記入してください")
            return redirect(url_for("input"))
        return redirect(url_for("input"))
    elif request.form["holiday_text"]=="":
        flash("祝日 テキストを記入してください")
        return redirect(url_for("input"))
    
    text = request.form["holiday_text"]
    dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))                 
    if request.form["button"] == "insert_update": 
        holiday = Holiday.query.filter_by(holi_date=dt).first()

        if holiday is None:
            holi_new = Holiday(holi_date=dt, holi_text=request.form["holiday_text"])
            db.session.add(holi_new)
            db.session.commit()
            result_message=request.form["holiday"]+"（" + request.form["holiday_text"] + "）が登録されました"
        else:
            holi_new = Holiday(holi_date=dt,holi_text=request.form["holiday_text"])
            db.session.merge(holi_new)
            db.session.commit()
            result_message=request.form["holiday"]+"「" + request.form["holiday_text"] + "」に更新されました"

        return render_template("result.html", result_message = result_message)

    elif request.form["button"] == "delete":
        holiday = Holiday.query.filter_by(holi_date=dt).first()
        holiday_text = Holiday.query.filter_by(holi_text=text).first()

        if holiday is None:
            flash(request.form["holiday"]+"は、祝日マスタに登録されていません")
            return redirect(url_for("input"))
        else:
            if holiday_text is None:
                flash("入力テキストが祝日マスタに登録されたテキストと一致しません")
                return redirect(url_for("input"))

            Holiday.query.filter_by(holi_date = dt).delete()
            db.session.commit() 
            result_message=request.form["holiday"]+"（" + request.form["holiday_text"] + "）は、削除されました"
            return render_template("result.html", result_message = result_message)                            
                      