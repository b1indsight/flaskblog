from flask_pagedown.fields import PageDownField
from wtforms import SubmitField, validators,StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 60)])
    body = PageDownField("write here", validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = PageDownField("write comment here", validators=[DataRequired()])
    submit = SubmitField('Submit')
