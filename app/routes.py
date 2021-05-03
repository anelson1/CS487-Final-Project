from flask import *
from app import myapp
from datetime import date


#Home Page
@myapp.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
#Login Page
@myapp.route("/As", methods=['GET', 'POST'])
def login():
    return render_template("As.html")
#The User's account page
@myapp.route("/about", methods=['GET', 'POST'])
def useraccount():
    return render_template("about.html")   
#The driver's account page
@myapp.route("/riderlogin", methods=['GET', 'POST'])
def riderlogin():
    return render_template("riderLogIn.html")    
@myapp.route("/registered", methods=['GET', 'POST'])
def registered():
    name = request.args.get('name')
    return render_template("registered.html", name=name)
@myapp.route("/rideraccount", methods=['GET', 'POST'])
def rideraccount():
    return render_template("riderAccount.html")  
@myapp.route("/driverlogin", methods=['GET', 'POST'])
def driverlogin():
    return render_template("driverLogIn.html")  
@myapp.route("/driveraccount", methods=['GET', 'POST'])
def driveraccount():
    name = request.args.get('name')
    return render_template("driverAccount.html", name = name)  
@myapp.route("/driversignup", methods=['GET', 'POST'])
def driversignup():
    return render_template("driverSignUp.html")  
@myapp.route("/ridersignup", methods=['GET', 'POST'])
def ridersignup():
    return render_template("riderSignUp.html")  
@myapp.route("/book", methods=['GET', 'POST'])
def riderbook():
    name = request.args.get('name')
    return render_template("rideBook.html", name=name)  
@myapp.route("/confirm", methods=['GET', 'POST'])
def riderconfirm():
    session['origin'] = request.form['origin']
    session['destination'] = request.form['destination']
    return render_template("rideConfirm.html")  
@myapp.route("/route", methods=['GET', 'POST'])
def rideroute():
    return render_template("rideRoute.html")  
@myapp.route("/complete", methods=['GET', 'POST'])
def rideComplete():
    return render_template("rideComplete.html", origin = session['origin'], destination = session['destination'], date= date.today()
)  