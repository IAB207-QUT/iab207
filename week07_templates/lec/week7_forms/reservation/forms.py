from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ContactForm(FlaskForm): # inherits from FlaskForm
    user_name = StringField('Name' )    
    email = StringField('Email Address')
    submit = SubmitField("Submit")
