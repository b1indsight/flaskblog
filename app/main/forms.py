from flask_wtf import PageDownField
from wtforms import SubmitField, validators

class PostForm(FlaskForm):
    body = PageDownField("write here", validators=[DataRequired()])
    submit = SubmitField('Submit')
