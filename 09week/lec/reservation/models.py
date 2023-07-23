from . import db
from flask_login import UserMixin

class Hotel(db.Model):
    __tablename__='hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='default.jpg')
    
    #relationships are pseudo attributes and are not columns in DB
    rooms = db.relationship('Room', backref='hotel')
    
    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(64), index=True)
    num_rooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    
    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.room_type, self.id)


class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)#should be 128 in length to store hash
    
    usertype = db.Column(db.String(20), nullable=False, default='guest')


    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)

