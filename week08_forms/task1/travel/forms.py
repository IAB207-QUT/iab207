from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, Length

class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  #description meets the length requirements
  description = TextAreaField('Description', validators = [InputRequired()])
  image = StringField('Cover Image', validators=[InputRequired()])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')