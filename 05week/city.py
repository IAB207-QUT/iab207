class City:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_city_details(self):
        return str(self)

    def __repr__(self):
        str = f"Name: {self.name}, Desciption: {self.description}\n"
        return str