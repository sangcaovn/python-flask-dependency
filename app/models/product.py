<<<<<<< HEAD
from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique = True)
    description = db.Column(db.String(200))
=======

from app import db

class Product(db.Model):
    __tables__="products"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    des = db.Column(db.String(200), unique=True)


    def __repr__(self):
        return '<Product: {}>'.format(self.name)
>>>>>>> fd65437623493d051c8defb037986aa473161df0
