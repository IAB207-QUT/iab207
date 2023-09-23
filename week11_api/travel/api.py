from flask import Blueprint, jsonify, request
from travel.models import Hotel, Room
from travel import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/hotels')
def get_hotel():
    hotels = db.session.scalars(db.select(Hotel)).all()
    hotel_list = []
    for hotel in hotels:
        hotel_list.append(hotel.to_dict())
    return jsonify(hotels=hotel_list)

# Note you can have multiple functions with the same route path
# as long as they deal with different HTTP methods.
@api_bp.route('/hotels', methods=['POST'])
def create_hotel():
    json_dict = request.get_json()
    if not json_dict:
        return {'message': 'No input data provided'}, 400
    # Creating SQLAlchemy Hotel object from JSON dictionary
    hotel = Hotel(name=json_dict['name'], description=json_dict['description'],
                  destination=json_dict['destination'],
                  amenities=json_dict['amenities'])
    # Reading the nested Room object
    for r_dict in json_dict['rooms']:
        room = Room(type=r_dict['type'],num_rooms=r_dict['num_rooms'],
                    description=r_dict['description'])
        # Setting the Room's related Hotel object
        room.hotel = hotel
    db.session.add(hotel)
    db.session.commit()
    return jsonify(message='Successfully created new hotel!'), 201

@api_bp.route('/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    hotel = db.session.scalar(db.select(Hotel).where(Hotel.id==hotel_id))
    db.session.delete(hotel)
    db.session.commit()
    return jsonify(message='Record deleted!'), 200

@api_bp.route('/hotels/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    json_dict = request.get_json()
    hotel = db.session.scalar(db.select(Hotel).where(Hotel.id==hotel_id))
    hotel.name = json_dict['name']
    hotel.description = json_dict['description']
    db.session.commit()
    return jsonify(message='Record updated!'), 200