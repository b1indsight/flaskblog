from flask import request, render_template, session, redirect, url_for, flash
from .templates import main
from .models import User
from flask_login import LoginManager, login_required, logout_user
# from flask_mail import 
# from flask_wtf import
# from Bootstrap-Flask import

@main.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template("index.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'post':
		username = request.form['username'] 
		password = request.form['password'] 
	
		check = check(username, password)

		if check:
			flash("success")
			return redirect(url_for('login')) 
		else:
			return redirect(url_for('index'))
		
	else:
		return render_template("login.html") 	

def check(username, password):
    user = User.query.first()

    if username == user.username and user.verify_password(password):
        return True
    else:
        return False

@main.route('/logout')
def logout():
    logout_user()
    flash('logout success')
    return redirect(url_for('index'))


