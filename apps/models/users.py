from mongoengine import Document, StringField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True, max_length=1024)


