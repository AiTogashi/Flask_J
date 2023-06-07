#Flaskをimport
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Flaskの__name__インスタンスをappに代入
app = Flask(__name__)   
db  = SQLAlchemy(app)

app.config.from_object('holiday.config')

#viewsをimport
import holiday.views.input
import holiday.views.list
import holiday.views.maintenance_date