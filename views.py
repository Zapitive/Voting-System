from re import search,compile
from flask import Blueprint,render_template,url_for,request,flash,redirect
from flask_wtf import  FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email,EqualTo
from condb import *
from register import *


views = Blueprint(__name__,"views")

class Signup(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/signup" , methods=['GET','POST'])
def signup():
    form = Signup()
    return render_template("login.html",form=form)

@views.route("/test")
def test():
    x = con()
    if(x):
        return "Connected"
    else:
        return "not connnected"
    
@views.route("/success" , methods=['POST','GET'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        psw = request.form['password']
        psw_repeat = request.form['confirm_password']

        reg =  r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
        pat = compile(reg)
        mat = search(pat,psw)
        if psw != psw_repeat:
            flash('Password does not match')
            return redirect(url_for('views.signup'))
        elif mat:
            return "registered successfully"
        else:
            flash('password too weak')
            return redirect(url_for('views.signup'))