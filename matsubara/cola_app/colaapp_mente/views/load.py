#####################################################
# 本項では、server.pyにて起動した際の起動条件を記載する。
# 起動した際は、index.htmlを起動するように設定する。
##################################################### 
from flask import request, redirect, url_for, render_template, flash, session
from colaapp_mente import app

@app.route('/')
def ipa_show():
    return render_template('index.html')