class User:

    def __init__(self, name, email): #construct the object of the class
        self.name = name
        self.email = email
        self.type = 'normal'
        self.password_hash = None

     #  the set password method goes here
    def set_password(self, password):
        self.password_hash=password

    def __repr__(self):
        s="Name: {}, Email: {}, Type: {}, Password {}"
        s= s.format(self.name, self.email, self.type, self.password_hash)
        return s


class Admin(User): # derived class of User
    def __init__(self, name, email):
        super().__init__(name,email) #when you call base class method super()
        self.type='admin'

#create base object
normal_user = User('countvc', 'cvc@sstreet.com')
normal_user.set_password('vatesdenumberofdeday')
print(normal_user)

#create derived object and set password
#first instantiate derived object
#then set password for admin user using the related method on the base classadmin_user.set_password('dreamersandme') and print details
admin_user = User('kermit', 'kermie@sstreet.com')
admin_user.set_password('dreamersandme')
print(admin_user)
