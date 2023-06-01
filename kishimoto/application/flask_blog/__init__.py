#Flaskをimport
from flask import Flask
#Flaskの__name__インスタンスをappに代入
app = Flask(__name__)   

app.config.from_object('flask_blog.config')
#viewsをimport
import flask_blog.views
