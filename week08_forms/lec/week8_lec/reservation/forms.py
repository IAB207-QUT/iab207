from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, Form, IntegerField, FormField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    user_name = StringField('Name' )    #, validators=[InputRequired()]
    email = StringField('Email Address')
    submit = SubmitField("Submit")


class RoomForm(Form):
    room_type=StringField('Type')
    num_rooms = IntegerField('Number of Rooms')
    price = IntegerField('Price')
    room_desc=TextAreaField('Description')

    

class HotelForm(FlaskForm):
    name=StringField('Name')
    description=TextAreaField('Description')
    image = StringField('Image File Name')
    room = FormField(RoomForm)
    submit = SubmitField("Create")

