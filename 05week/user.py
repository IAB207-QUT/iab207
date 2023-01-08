

class User:
    # this is the function used to create the user
    def __init__(self):
        self.user_type='guest'
        self.uname=None
        self.pwd=None
        self.emailID=None

    def register(self,name,pwd,emailID):
        self.uname=name
        self.pwd=pwd
        self.emailID=emailID

    def __repr__(self):
        s= "Name: {0}, Email: {1}, type: {2}\n"
        s=s.format(self.uname, self.emailID, self.user_type)
        return s



    
    
    
    
    
    
    
    


class FrequentTraveller(User):

    def __init__(self):
        self.user_type='frequent traveller'
        self.travellerID='NONE'

    def register(self, username, pwd, emailID, travellerID):
        super().register(username,pwd,emailID)
        self.travellerID=travellerID
    
    def __repr__(self):
        s= super().__repr__()
        s = s + "Traveller ID: {0}".format(self.travellerID)
        return s