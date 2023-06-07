from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from decimal import Decimal, ROUND_HALF_UP
from holiday.models.mst_holiday import Holiday

#登録処理
@app.route('/result', methods=['POST'])
def add_holiday():
    #モデルインスタンス作成
    holiday = Holiday(
                            #input.htmlのinputタグのname属性
        holi_date=request.form['holiday'],
        holi_text=request.form['holiday_text']
    )
    #データベース保存
    db.session.add(holiday)
    db.session.commit()
    return render_template('result.html',holiday=holiday)

#削除処理
# def delete_holiday(holi_date):
#     holiday = Holiday.query.get(holi_date)
#     db.session.delete(holiday)
#     db.session.commit()
#     flash('削除されました')
#     return render_template('result.html',holiday=holiday)


