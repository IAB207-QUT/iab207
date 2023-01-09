from flask import Blueprint,render_template, redirect, url_for, request
from .forms import ContactForm
from .models import Hotel

# always import anything not defined in this python file
from .user_forms import LoginForm, RegisterForm

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
     print('In index function - creating the landing page')
     tag_line='Using Flask Bootstrap'
     hotels = get_hotel_list()
     contact_form=ContactForm()
     return render_template('index_bootstrap.html', tag_line=tag_line,
                    html_form=contact_form, hotels=hotels)




@mainbp.route('/contact', methods=['GET','POST']) # both get and post
def create_contact():
     print('In contact view function')
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(form.user_name.data)
          print(form.email.data)
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

#add a route for the user login
@mainbp.route('/login', methods=['GET','POST'])
def login():
     print('In login function')
     l_form = LoginForm()
     return render_template('user_form.html', heading='Login', form=l_form)

#add a route for registering
@mainbp.route('/register', methods=['GET','POST'])
def register():
     print('In Register function')
     rform = RegisterForm()
     if rform.validate_on_submit():
          print('The name of the user:', rform.username.data)
          print('The email of the user:', rform.email.data)
          
     return render_template('user_form.html', heading='Register', form=rform)