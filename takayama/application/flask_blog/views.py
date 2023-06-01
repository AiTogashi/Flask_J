from flask_blog import app

@app.route("/")
def show_entires():
    return "Hello World!!"