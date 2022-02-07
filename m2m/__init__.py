from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///data.db'
app.config["SECRET_KEY"]= b'isdfoi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

from m2m import routes