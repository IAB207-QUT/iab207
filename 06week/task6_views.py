from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    if 'email' in session:
        str='<h1>hello ' + session['email'] + '</h1>'
    else:
        str='<h1>hello world</h1>'
    return str

@mainbp.route('/login', methods = ['GET','POST'])
def login():

    email = request.values.get("email")
    pwd = request.values.get("pwd")
    print ("email: {}\npassword= {}".format(email,pwd))

    #store email in session
    session['email'] = request.values.get('email')

    return render_template('login.html')

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'