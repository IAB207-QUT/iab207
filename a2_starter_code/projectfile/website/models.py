from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):

class Event(db.Model):

class Comment(db.Model):

class Order(db.Model):