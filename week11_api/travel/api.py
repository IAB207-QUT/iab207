from flask import Flask, Blueprint, jsonify, request
from travel.models import Hotel, Room
from travel import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/hotels')
def get_hotel():
    hotels = db.session.scalars(db.select(Hotel)).all()
    hlist = [h.to_dictionary() for h in hotels]
    return jsonify(hotels=hlist)

def to_dict(self):
    h_dict = {b.name: str(getattr(self, b.name)) for b in self.__table__.columns}
    return h_dict

@api_bp.route('/hotels', methods=['POST'])
def create_hotel():
    json_dict = request.get_json()
    if not json_dict:
        return {'message': 'No input data provided'}, 400
    #creating sql alchemy hotel object from json dictionary
    hotel = Hotel(name=json_dict['name'], description=json_dict['description'],
                  city=json_dict['city'],
                  amenities=json_dict['amenities'])
        #reading the contained object - room
    for r_dict in json_dict['rooms']:
        room = Room(type=r_dict['type'],num_rooms=r_dict['num_rooms'],
                    description=r_dict['description'])
        room.hotel=hotel    #setting the hotel object
    db.session.add(hotel)
    db.session.commit()
    return jsonify(message='successfully created'),201

@api_bp.route('/hotels/<int:hotelid>', methods=['DELETE'])
def delete_hotel(hotelid):
    hotel = db.session.scalar(db.select(Hotel).where(Hotel.id==hotelid))
    db.session.delete(hotel)
    db.session.commit()
    return jsonify(message='deleted record'),200

@api_bp.route('/hotels/<int:hotelid>', methods=['PUT'])
def update_hotel(hotelid):
    json_dict = request.get_json()
    hotel = db.session.scalar(db.select(Hotel).where(Hotel.id==hotelid))
    hotel.name = json_dict['name']
    hotel.description=json_dict['description']
    db.session.commit()
    return jsonify(message='updated record'),200