from flask import Blueprint,render_template, redirect, url_for, request
from .forms import ContactForm
from .models import Hotel
from .user_forms import HotelForm


#for file upload
from werkzeug.utils import secure_filename
import os



mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
     print('In index function - creating the landing page')
     tag_line='You need a vacation'
     hotels = get_hotel_list()
     #create the form
     contact_form=ContactForm()
     return render_template('index_bootstrap.html', tag_line=tag_line,
                    form=contact_form, hotels=hotels)




@mainbp.route('/contact', methods=['GET','POST']) # both get and post
def create_contact():
     print('In contact view function')
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))



def get_hotel_list():
    brisbane_hotel = Hotel('Brisbane', 'brisbane.jpg',
    'As the capital of the Sunshine State, we are blessed with idyllic subtropical weather all year round.')

    sydney_hotel = Hotel('Sydney', 'sydney.jpg',
    'From splendid Sydney Harbour, idyllic beaches and great national parks, to the marvellous creativity of the Sydney Opera House, dazzling entertainment and fascinating heritage, discover all the things to do and see throughout the year.')

    melbourne_hotel = Hotel('Melbourne', 'melbourne.jpg',
     'A packed agenda of food, wine, sports and arts is your introduction to the best of Melbourne – from its creative, exciting city centre, to its buzzing neighbourhood hubs.')

    hlist = list()
    hlist.append(brisbane_hotel)
    hlist.append(sydney_hotel)
    hlist.append(melbourne_hotel)
    return hlist


@mainbp.route('/hotel', methods=['GET','POST'])
def create_hotel():
     print('in create hotel')
     hform = HotelForm()
     if hform.validate_on_submit():
          check_file(hform)
          print('uploaded the image for hotel: ', hform.name.data )
     return render_template('user_form.html', heading='Upload form details', form=hform)


def check_file(form):
  img_file = form.image.data
  #getting the file data from form
  filename = img_file.filename
  # get the current path of the module file… store file relative to this path
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/img
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  # save the file and return the db upload path
  img_file.save(upload_path)
  