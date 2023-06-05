#Flaskをimport
from flask import Flask
#Flaskの__name__インスタンスをappに代入
app = Flask(__name__)   

app.config.from_object('holiday.config')

#viewsをimport
import holiday.views.input
import holiday.views.list
import holiday.views.maintenance_date