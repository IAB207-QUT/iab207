from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return '<h1>Starter code for assignment 3<h1>'