from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo

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
          validators=[EqualTo('password', message='Re-enter value same as Password')])
  submit = SubmitField('Register')


