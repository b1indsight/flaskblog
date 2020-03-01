from flask_pagedown.fields import PageDownField
from wtforms import SubmitField, validators
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    body = PageDownField("write here", validators=[DataRequired()])
    submit = SubmitField('Submit')
