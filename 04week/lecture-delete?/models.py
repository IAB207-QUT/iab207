
class User: # use the keyword class

    def __init__(self, name1, email1): #constuct an object of this class
        self.name = name1 # define and access attributes of the class using self.
        self.email = email1
        self.type='normal'
        self.password_hash=None

     #  the set password method goes here
    def set_password(self, password):
        self.password_hash=password

    def __repr__(self):
        s="Name: {}, Email: {}, Type: {}, Password {}"
        s= s.format(self.name, self.email, self.type, self.password_hash)
        return s


class Admin(User): # derived class of User1
    def __init__(self, name, email, privilege):
        super().__init__(name,email) #when you call base class method super()
        self.type='admin'
        self.privilege=privilege




#create a base class
normal_user = User('countvoncount', 'cvc@sstreet.com')
normal_user.set_password('vatesdenoovdeday')

# create the derived or admin class
admin_user = Admin('kermit', 'kermie@x.sstreet.com', 'xyzere')

 # the base class method is accessible in the derived class
admin_user.set_password('dreamersandme') 

#print both the classes
print(normal_user)
print(admin_user)









#create instance of the Hotel class: __init__ method is called here
#hotel_in_brisbane = Hotel('brisbane', 'Description of Brisbane')
#print(hotel_in_brisbane)

#create instance of the class
#hotel_in_sydney = Hotel('sydney', 'Close to Opera house')
#hotel_in_sydney.add_room('standard','basic room', 45,200)
#print(hotel_in_sydney)
#
#hotel_in_brisbane.add_room('standard',' basic room in Brisbane', 30, 120)
#print(hotel_in_brisbane)

#you could create independent room objects but current signature of hotel
# does not let you pass the child object, it takes control of the child object
#std_room1 = Room('standard', 'Basic room', 30,110)
#std_room2 = Room('standard', 'Basic room', 45,200)
