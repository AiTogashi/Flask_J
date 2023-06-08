from flask import request, redirect, url_for, render_template, flash, session
from dictionary import app
from dictionary import db
from dictionary.models.mst_it import ITpassport
from datetime import date

@app.route("/maintenance_word", methods=["POST"])
def maintenance_word():
    # if request.form["IT_word"]=="":
    #     flash("祝日 日付を選択してください")
    #     if request.form["mean"]=="":
    #         flash("祝日 テキストを記入してください")
    #         return redirect(url_for("input"))
    #     return redirect(url_for("input"))
    # elif request.form["mean"]=="":
    #     flash("祝日 テキストを記入してください")
    #     return redirect(url_for("input"))
    
    IT_word = request.form["IT_word"]
    # mean = request.form["mean"]
    # dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))                 
    if request.form["button"] == "insert_update": 
        word = ITpassport.query.filter_by(IT_word=IT_word).first()
        print("ok")

        if word is None:
            word_new = ITpassport(IT_word=IT_word, mean=request.form["mean"])
            db.session.add(word_new)
            db.session.commit()
            result_message=request.form["IT_word"]+"（" + request.form["mean"] + "）が登録されました"
        else:
            holi_new = ITpassport(IT_word=IT_word,mean=request.form["mean"])
            db.session.merge(holi_new)
            db.session.commit()
            result_message=request.form["IT_word"]+"「" + request.form["mean"] + "」に更新されました"

        return render_template("result.html", result_message = result_message)

    elif request.form["button"] == "delete":
        word = ITpassport.query.filter_by(IT_word=IT_word).first()
        # mean_text = ITpassport.query.filter_by(mean=mean).first()

        if word is None:
            flash(request.form["IT_word"]+"は、祝日マスタに登録されていません")
            return redirect(url_for("input"))
        else:
            ITpassport.query.filter_by(IT_word = IT_word).delete()
            db.session.commit() 
            result_message=request.form["IT_word"]+"は、削除されました"
            return render_template("result.html", result_message = result_message)

    elif request.form["button"] == "serch":
        result_message=request.form["IT_word"]+"の検索結果は以下です。"
        serch_result=ITpassport.query.filter_by(IT_word=IT_word).first()
        result_mean = serch_result.mean  
        return render_template("serch.html", result_message = result_message, word=IT_word, mean=result_mean) 


                      