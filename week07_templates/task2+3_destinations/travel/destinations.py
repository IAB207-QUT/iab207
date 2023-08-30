from flask import Blueprint, render_template

# name - first argument is the blueprint name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('destination', __name__, url_prefix = '/destinations')

@destbp.route('/<id>')
def show(id):
    return render_template('destinations/show.html')