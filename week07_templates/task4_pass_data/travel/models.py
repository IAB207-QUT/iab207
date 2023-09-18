class Destination:

    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

    def __repr__(self):
        return f"Name: {self.name}, Currency: {self.currency}"

class Comment:
    def __init__(self,user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

    def __repr__(self):
        return f"User {self.user}, \n Text {self.text}"