from db import db


class Indicators(db.Model):
    __tablename__ = 'indicadores'

    # structure of table in database
    index = db.Column(db.Integer, primary_key=True)
    VALUES = db.Column(db.String(100))

    def __init__(self, index, VALUES):
        self.VALUE = VALUES
        self.index = index

    def json(self):
        return {
            'id': self.index,
            'value': self.VALUES
        }
