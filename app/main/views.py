from flask import request, render_template, session, redirect, url_for, flash
from . import main
from ..models import User, Post
from flask_login import LoginManager, login_required, logout_user, current_user
# from flask_mail import 
from .forms import PostForm
# from Bootstrap-Flask import

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()

    if current_user.is_active and current_user.is_authenticated:
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template("index.html", form=form, posts=posts)


@main.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'post':
		username = request.form['username'] 
		password = request.form['password'] 
	
		check = check(username, password)

		if check:
			flash("success", "success")
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
    return redirect(url_for('.index'))

