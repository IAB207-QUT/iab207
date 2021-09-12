from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')