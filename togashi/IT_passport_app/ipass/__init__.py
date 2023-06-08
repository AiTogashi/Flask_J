from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ipass.config')

db = SQLAlchemy(app)

from ipass.views import input, list, maintenance_date
