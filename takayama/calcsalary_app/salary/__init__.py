from flask import Flask

app = Flask(__name__)
app.config.from_object("flask_blog.config")

import Flask_J.takayama.calcsalary_app.salary.views.views

