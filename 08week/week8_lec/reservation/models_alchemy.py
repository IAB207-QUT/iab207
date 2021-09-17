from . import db

class Hotel(db.Model):
    __tablename__='hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='default.jpg')
    
    #relationships are pseudo attributes and are not columns in DB
    rooms = db.relationship('Room', backref='hotel')
    comments = db.relationship('Review', backref='hotel')
    
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


class Review(db.Model):

    __tablename__= 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    date_posted = db.Column(db.Date, nullable=False)


    hotelid = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return "<id: {} from user {} >".format(self.comment, self.userid)


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)#should be 128 in length to store hash
    
    comments = db.relationship('Review', backref='user')
    hotels = db.relationship('Hotel', secondary='reviews',
                             backref=db.backref('commented_users'))


    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)

