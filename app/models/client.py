
from app import db

class Client(db.Model):
    __tables__="clients"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


    def __repr__(self):
        return '<Client: {}>'.format(self.name)