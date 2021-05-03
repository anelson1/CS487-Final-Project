from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PissUponYourChimneyKneeGrowBeOnThatBeheminiey'
myapp = Flask(__name__)
myapp.config.from_object(Config)

from app import routes