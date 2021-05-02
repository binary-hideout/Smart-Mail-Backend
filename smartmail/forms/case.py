from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CaseCreateForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    contact_id = StringField('contact_id', validators=[DataRequired()])
    tag_id = StringField('tag_id', validators=[DataRequired()])

class CaseUpdateForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    contact_id = StringField('contact_id', validators=[DataRequired()])
    tag_id = StringField('tag_id', validators=[DataRequired()])