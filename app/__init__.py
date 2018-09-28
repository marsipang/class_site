# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:45:53 2018

@author: pangi
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from models import User

from login.login import login_bp
from students.students import student_bp

app.register_blueprint(login_bp)
app.register_blueprint(student_bp)