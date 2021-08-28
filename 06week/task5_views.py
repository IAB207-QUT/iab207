from flask import Blueprint, render_template, request

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    str='<h1>hello world</h1>'
    return str

@mainbp.route('/login', methods = ['GET','POST'])
def login():
    email = request.values.get("email")
    pwd = request.values.get("pwd")
    print ("email: {}\npassword= {}".format(email,pwd))
    return render_template('login.html') #file must be in templates folder
