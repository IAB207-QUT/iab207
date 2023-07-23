from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,TextAreaField, 
                        Form, IntegerField, FormField, PasswordField, SelectField)
from wtforms.validators import InputRequired, Email, EqualTo

   

class HotelForm(FlaskForm):
    name=StringField('Name')
    description=TextAreaField('Description')
    image = StringField('Image File Name')
    submit = SubmitField("Create")

class LoginForm(FlaskForm):
  username = StringField('User Name', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired()])
    email = StringField('Email ID', validators=[InputRequired(),Email() ])
    #password field
    password = PasswordField('Password', validators=[InputRequired()])
  #validator to check if the user entry is equal to password
    confirm = PasswordField('Confirm Password', 
          validators=[EqualTo('password', message='Re-enter same as Password')])

    usertype = SelectField('User Type', choices=[('guest', 'Guest'),('admin', 'Administrator')])
    submit = SubmitField('Register')


  
class ContactForm(FlaskForm):
    user_name = StringField('Name' )    
    email = StringField('Email Address')
    submit = SubmitField("Submit")