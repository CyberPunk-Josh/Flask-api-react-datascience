from db import db


class ElectricServiceModel(db.Model):
    __tablename__ = 'electric_service'

    # structure of table in database
    index = db.Column(db.Integer, primary_key=True)
    CITY = db.Column(db.String(100))
    VALUE = db.Column(db.Float)

    def __init__(self, CITY, VALUE, index):
        self.VALUE = VALUE
        self.CITY = CITY
        self.index = index

    def json(self):
        return {
            'id': self.index,
            'city': self.CITY,
            'value': self.VALUE
        }

    @classmethod
    def find_by_city_name(cls, city):
        return cls.query.filter_by(CITY=city).first()
