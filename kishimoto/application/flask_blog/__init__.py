#Flaskをimport
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Flaskの__name__インスタンスをappに代入
app = Flask(__name__)   
db = SQLAlchemy(app)

app.config.from_object('flask_blog.config')
#viewsをimport
# import kishimoto.application.flask_blog.views.views

import flask_blog.views
