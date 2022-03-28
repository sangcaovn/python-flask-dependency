from app import db

class Product(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    description = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
        return '<Product: {}>'.format(self.name)
