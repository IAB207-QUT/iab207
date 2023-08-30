class Hotel:

    def __init__(self,name, image, description):
        self.name =name
        self.image=image
        self.description=description

    def __repr__(self):
        str_val="Name: {}, description: {}".format(self.name, self.description)
        return str_val
    