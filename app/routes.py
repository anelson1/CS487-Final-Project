from flask import *
from app import myapp
#Home Page
@myapp.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
#Login Page
@myapp.route("login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")
#The User's account page
@myapp.route("useraccount", methods=['GET', 'POST'])
def useraccount():
    return render_template("account.html")   
#The driver's account page
@myapp.route("driveraccount", methods=['GET', 'POST'])
def driveraccount():
    return render_template("driveraccount.html")    
#The Page where the user books a ride
@myapp.route("book", methods=['GET', 'POST'])
def book():
    return render_template("book.html")