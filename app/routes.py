from flask import *
from app import myapp, db
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, UserMixin, logout_user, login_required


login_manager = LoginManager()
login_manager.init_app(myapp)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phonenumber = db.Column(db.String(50))

    def __repr__(self):
        return "User: " + self.username
class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    riders = db.Column(db.String(12))
    time = db.Column(db.String(20))
    date = db.Column(db.String(20))

    def __repr__(self):
        return "trip: " + str(self.id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
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
    error = False
    try:
        error = request.args.get('error')
    except:
        print("No Error Here!")
    return render_template("riderLogIn.html", error= error)    
@myapp.route("/registered", methods=['GET', 'POST'])
def registered():
    name = request.form['username']
    password = request.form['pswd']
    phone = request.form['phone']
    address = request.form['address']
    newuser = User(username=name, password = password, phonenumber = phone, address=address)
    db.session.add(newuser)
    db.session.commit()
    return render_template("registered.html", name=name)
@myapp.route("/rideraccount", methods=['GET', 'POST'])
def rideraccount():
    return render_template("riderAccount.html")
@myapp.route("/loginhandle", methods = ["POST","GET"])
def formhandler():
    user = request.form['username']
    passw = request.form['password']
    curr_user = User.query.filter_by(username=user).first()
    if curr_user:
        #if password given = users password, then login 
        if curr_user.password == passw:
            login_user(curr_user)
            return redirect(url_for("rideraccount", user = user))
        else:
            return redirect(url_for("riderlogin", error = True))
    else:
        return redirect(url_for("riderlogin", error = True))
@myapp.route("/logouthandle")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
@myapp.route("/driverlogin", methods=['GET', 'POST'])
def driverlogin():
    return render_template("driverLogIn.html")  
@myapp.route("/driveraccount", methods=['GET', 'POST'])
def driveraccount():
    name = request.form['name']
    trips = Trip.query.all()
    return render_template("driverAccount.html", name = name, trips = trips)  
@myapp.route("/driversignup", methods=['GET', 'POST'])
def driversignup():
    return render_template("driverSignUp.html")  
@myapp.route("/ridersignup", methods=['GET', 'POST'])
def ridersignup():
    return render_template("riderSignUp.html")  
@myapp.route("/book", methods=['GET', 'POST'])
def riderbook():
    return render_template("rideBook.html")  
@myapp.route("/confirm", methods=['GET', 'POST'])
def riderconfirm():
    session['origin'] = request.form['origin']
    session['destination'] = request.form['destination']
    newtrip = Trip(origin = session['origin'], destination = session['destination'], riders=request.form['riders'], date = request.form['date'], time=request.form['time'])
    db.session.add(newtrip)
    db.session.commit()
    return render_template("rideConfirm.html")  
@myapp.route("/route", methods=['GET', 'POST'])
def rideroute():
    return render_template("rideRoute.html")  
@myapp.route("/complete", methods=['GET', 'POST'])
def rideComplete():
    return render_template("rideComplete.html", origin = session['origin'], destination = session['destination'], date= date.today()
)  