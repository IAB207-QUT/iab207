class User:
    # this is the function used to create the user
    def __init__(self):
        self.user_type = 'guest'
        self.username = None
        self.password = None
        self.email = None

    def register(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        str = f"Name: {self.username}, Email: {self.email}, User type: {self.user_type}"
        return str

class FrequentTraveller(User):

    def __init__(self):
        self.user_type = 'Frequent Traveller'
        self.travellerID = None

    def register(self, username, passwd, emailID, travellerID):
        super().register(username ,passwd, emailID)
        self.travellerID = travellerID
    
    def __repr__(self):
        str = super().__repr__()
        str = str + f" Traveller ID: {self.travellerID}"
        #str = str + "Traveller ID: {0}".format(self.travellerID)
        return str