from flask import request, redirect, url_for, render_template, flash, session
from dictionary import app
from dictionary import db
from dictionary.models.mst_it import ITpassport

@app.route("/list", methods=["POST"])
def list():
    dictionarylist = ITpassport.query.all()
    return render_template('list.html', dictionarylist=dictionarylist)