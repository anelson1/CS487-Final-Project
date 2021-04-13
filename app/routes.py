from flask import *
from app import myapp

@myapp.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
