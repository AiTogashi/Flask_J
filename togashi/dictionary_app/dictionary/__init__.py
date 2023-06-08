from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('dictionary.config')

db = SQLAlchemy(app)

from dictionary.views import input, list, maintenance_word
