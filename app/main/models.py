from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import 
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @password.setter
    def __init__(self, username, password):
        self.username = username
        password(self, password)
        
    def __repr__(self):
        return '<User %r>' % self
    