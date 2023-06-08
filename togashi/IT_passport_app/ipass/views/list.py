from flask import request, redirect, url_for, render_template, flash, session
from ipass import app
from ipass import db
from ipass.models.mst_ipass import ITpassport

@app.route("/list", methods=["POST"])
def list1():
    wordlist = ITpassport.query.all()
    return render_template('list.html', wordlist=wordlist)
