from datetime import datetime
from .user import User
class Booking:

    def __init__(self, startdate, enddate, city, user):
        self.startdate=startdate
        self.enddate=enddate
        self.city = city
        self.user = user
        self.num_guests = 1
    
    def __repr__(self):
        str = " User: {0} City: {1} \n Start date: {2}\n End date: {3}\n Number of Guests: {4}"
        str = str.format( self.user, self.city.name,self.startdate,
            self.enddate, self.num_guests)
        #str += " Num guests: %d"  % 
        return str