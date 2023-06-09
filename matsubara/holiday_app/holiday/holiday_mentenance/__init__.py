from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('holiday_mentenance.config')

db = SQLAlchemy(app)


from holiday_mentenance.views import input, list , maintenance_date
