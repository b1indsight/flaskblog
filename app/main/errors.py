from flask import render_template
from . import main
from flask_login import current_user

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', user=current_user), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', user=current_user), 500

