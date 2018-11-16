from main import db

class data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    tax_code = db.Column(db.Integer)
    price = db.Column(db.Integer) 

    def __init__(self, name, tax_code, price):
        #self.id = id
        self.name = name
        self.tax_code = tax_code
        self.price = price

    #def __repr__(self):
    #        return '<Computer: {}>'.format(self.id)