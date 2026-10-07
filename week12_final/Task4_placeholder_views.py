from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db
import numpy as np

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        if 'use_ai' in request.args:

            # Semantic search code to be added here
            print ("Semantic search selected")
            destinations=[] # placeholder

        else:
            query = "%" + request.args['search'] + "%"
            destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))