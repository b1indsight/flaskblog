from flask import Flask, flash
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown

db = SQLAlchemy()
login_manager = LoginManager()
pagedown = PageDown()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    app.app_context().push()
    db.create_all()

    from .templates import main as mainBlueprint
    app.register_blueprint(mainBlueprint)

    return app