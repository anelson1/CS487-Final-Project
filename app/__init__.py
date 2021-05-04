from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_user, current_user, UserMixin, logout_user, login_required
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PissUponYourChimneyKneeGrowBeOnThatBeheminiey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/taxi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
myapp = Flask(__name__)
myapp.config.from_object(Config)
db = SQLAlchemy(myapp)


from app import routes