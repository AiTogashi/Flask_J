from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('colaapp_mente.config')

db = SQLAlchemy(app)


from colaapp_mente.views import list,load,mentenance,show
from colaapp_mente import db