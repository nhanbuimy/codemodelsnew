from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = '^sfkknsjjfsnskn238u3849hftt4gd#$#FRESDGSYETE$^E^%&%&%ỲYGHF94u4394r3wkrhsjrfhesi'
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/qlks2?charset=utf8mb4' % quote('Admin@123456')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True



db = SQLAlchemy(app=app)
login = LoginManager(app=app)