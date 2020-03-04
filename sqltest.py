from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
db.init_app(app)
db.create_all()

@main.route('/', methods=['GET', 'POST'])
def index():
    y = x(id = 1)
    db.session.add(y)
    db.session.commit()
    return (db.query.first().id)


class x(db.Model):
    id = db.Column(db.Integer, primary_key=True)

app.run()