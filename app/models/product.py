
from app import db

class Product(db.Model):
    __tables__="products"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    des = db.Column(db.String(200), unique=True)


    def __repr__(self):
        return '<Product: {}>'.format(self.name)