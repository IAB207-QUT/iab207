from datetime import datetime
from .user import User

class Booking:

    def __init__(self, startdate, enddate, city, user):
        self.startdate = startdate
        self.enddate = enddate
        self.city = city
        self.user = user
        self.num_guests = 1
    
    def __repr__(self):
        str = f"User: {self.user} City: {self.city.name}\n Start date: {self.startdate}\n End date: {self.enddate}\n Number of Guests: {self.num_guests}"
        return str