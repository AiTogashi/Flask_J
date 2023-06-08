from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('cola_app.config')

db = SQLAlchemy(app)


from cola_app.views import list,load,mentenance,show