class Destination:

    def __init__(self, name, description, image_url, currency):
        self.name = name
        self.description = description
        self.image = image_url
        self.currency = currency
        self.comments = list()

    def set_comments(self,comment):
        self.comments.append(comment)

    def __repr__(self):
        str = 'Name {0} , Currency {1}'
        str.format(self.name, self.currency)
        return str


class Comment:
    def __init__(self,user, text, created_at):
        self.user = user
        self.text = text
        self.create_at = created_at

    def __repr__(self):
        str = 'User {0}, \n Text {1}'
        str.format(self.user, self.text)
        return str
