#João Victor de Jesus Augusto
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/microblog.db'
app.config['SECRET_KEY'] = "PDITA12345678"

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"

from app import routes
