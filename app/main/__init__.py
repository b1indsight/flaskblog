from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app ():
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)

    app.app_context().push()
    db.create_all()

    from .templates import main as mainBlueprint
    app.register_blueprint(mainBlueprint)

    return app