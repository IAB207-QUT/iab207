from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    user_name = StringField('Name' )    #, validators=[InputRequired()]
    email = StringField('Email Address')
    submit = SubmitField("Submit")

