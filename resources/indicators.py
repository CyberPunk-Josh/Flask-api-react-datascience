from flask_restful import Resource
from models.indicators import Indicators


class IndicatorsValueList(Resource):
    def get(self):
        return {'indicators': [x.json() for x in Indicators.query.all()]}
