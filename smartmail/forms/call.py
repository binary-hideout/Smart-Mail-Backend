from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CallForm(FlaskForm):
    language = StringField('language', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
