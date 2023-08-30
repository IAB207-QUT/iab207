from flask import Blueprint, render_template, request

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    str = '<h1>Hello World</h1>'
    return str

@mainbp.route('/login', methods = ['GET', 'POST'])
def login():
    email = request.values.get("email")
    passwd = request.values.get("pwd")
    print (f"Email: {email}\nPassword: {passwd}")
    return render_template('login.html') #file must be in templates folder