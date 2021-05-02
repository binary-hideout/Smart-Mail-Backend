from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ContactCreateForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])

class ContactUpdateForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])