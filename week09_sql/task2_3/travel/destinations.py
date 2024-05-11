from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm
from . import db

destbp = Blueprint('destination', __name__, url_prefix='/destinations')

@destbp.route('/<id>')
def show(id):
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    # create the comment form
    cform = CommentForm()    
    return render_template('destinations/show.html', destination=destination, form=cform)

@destbp.route('/create', methods=['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = DestinationForm()
  if form.validate_on_submit():
    destination = Destination(name=form.name.data,
    description=form.description.data,
    image=form.image.data,
    currency=form.currency.data)
    # add the object to the db session
    db.session.add(destination)
    # commit to the database
    db.session.commit()
    print('Successfully created new travel destination', 'success')
    # Always end with redirect when form is valid
    return redirect(url_for('destination.create'))
  return render_template('destinations/create.html', form=form)

@destbp.route('/<id>/comment', methods=['GET', 'POST'])  
def comment(id):  
    form = CommentForm()  
    # get the destination object associated to the page and the comment
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    if form.validate_on_submit():  
      # read the comment from the form, associate the Comment's destination field
      # with the destination object from the above DB query
      comment = Comment(text=form.text.data, destination=destination) 
      # here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 
      # flashing a message which needs to be handled by the html
      # flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=id))