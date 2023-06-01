from flask import request,redirect,url_for,render_template,flash,session
from salary import app

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/input.html')