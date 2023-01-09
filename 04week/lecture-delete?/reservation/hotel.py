class Room:
    # This is a class that is a part-of the Hotel class
    def __init__(self, type, description, number_of_rooms, price):
        self.type=type
        self.description=description
        self.number_of_rooms=number_of_rooms
        self.price=price

    def __repr__(self): # the method that prints the string

        # the format function of the string is used
        s="Type: {}, Description: {}, Number of rooms: {}, price: {}"
        s= s.format(self.type, self.description, self.number_of_rooms, self.price)
        return s

class Hotel:
    
    def __init__(self,name, description):
        print('Called when a hotel is created')
        self.name=name
        self.description=description
        self.rooms = dict() # the dictionary object is used to store rooms and their types
        #this is where an object contains another object - aggregation/composition

    #this method allows the 'part-of' class to be added from the composite class   
    def add_room(self,type, description, number_of_rooms, price ): 
        # def add_Room(self, hotel_room) This would be the signature if this was an aggregation relationship
        # the hotel_room object is created within the add room class
        hotel_room = Room(type,description,number_of_rooms, price)
        self.rooms[type]=(hotel_room)
    
    def __repr__(self):
        s="Hotel name: {}, Description: {}, Rooms: {}"
        s= s.format(self.name, self.description, self.rooms)
        return s

#Create hotel
myhotel = Hotel('Grandview Hotel', 'Premier Brisbane hotel')

#Add rooms
myhotel.add_room('delux', 'high end', '20', '120')
myhotel.add_room('normal', 'high end', '10', '60')

print(myhotel)