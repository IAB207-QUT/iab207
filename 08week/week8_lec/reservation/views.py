from flask import Blueprint,render_template, redirect, url_for, request
from .forms import ContactForm, HotelForm
from . import db
from .models_alchemy import Hotel, Room

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='You need a vacation'
    hotels = Hotel.query.all() #get the hotels
    form=ContactForm()
    return render_template('index_bootstrap.html', tag_line=tag_line,
                    form=form, hotels=hotels)




@mainbp.route('/contact', methods=['GET','POST']) # both get and post
def create_contact():
     print('In contact view function')
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))


@mainbp.route('/hotel/create', methods=['GET','POST']) # both get and post
def add_hotel():
     print('In create hotel')
     form = HotelForm()
     
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          #create a new hotel with the information passed
          new_hotel = Hotel(name=form.name.data, description=form.description.data,
                              image=form.image.data)
          # when creating a room, pass the hotel and set the attribute 
          new_room = Room(room_type=form.room.room_type.data, 
                              description = form.room.room_desc.data,
                              num_rooms=form.room.num_rooms.data, 
                              price=form.room.price.data, hotel=new_hotel)
          db.session.add(new_hotel)
          db.session.commit()
          #return redirect(url_for('main.create_hotel'))
          
     return render_template('forms.html', form=form)
