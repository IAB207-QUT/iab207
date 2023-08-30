from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, Length

from flask_wtf.file import FileRequired, FileField, FileAllowed


#add the types of files allowed as a set
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG', 'bmp'}

class HotelForm(FlaskForm):
  name = StringField('Hotel', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired(), Length(min=10, max=200)])
  
  #create a filefield that takes two validators - File required and File Allowed
  image = FileField('Hotel Image', validators=[FileRequired(message='Image can not be empty'),
                                         FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
    
  submit = SubmitField("Create")
