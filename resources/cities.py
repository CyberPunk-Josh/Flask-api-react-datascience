from flask_restful import Resource
from models.cities import Cities


class CitiesValueList(Resource):
    def get(self):
        return {'indicators': [x.json() for x in Cities.query.all()]}
