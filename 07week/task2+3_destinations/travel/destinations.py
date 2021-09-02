from flask import Blueprint, render_template

# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    return render_template('destinations/show.html')
