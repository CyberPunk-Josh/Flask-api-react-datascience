from flask_restful import Resource, reqparse
from flask import request
from models.electric_service import ElectricServiceModel
from models.alfabeta import AlfabetaServiceModel
from models.analfabetas import AnalfabetasServiceModel
from models.rezago import RezagoServiceModel


class ServiceValues(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        city = request.args.get('city')
        indicator = request.args.get('indicator')

        if indicator == 'electric':
            city = ElectricServiceModel.find_by_city_name(city)
            if city:
                return city.json()
            return {'message': 'City not found'}, 404
        elif indicator == 'alfabeta':
            city = AlfabetaServiceModel.find_by_city_name(city)
            if city:
                return city.json()
            return {'message': 'City not found'}, 404
        elif indicator == 'analfabetas':
            city = AnalfabetasServiceModel.find_by_city_name(city)
            if city:
                return city.json()
            return {'message': 'City not found'}, 404
        elif indicator == 'rezago':
            city = RezagoServiceModel.find_by_city_name(city)
            if city:
                return city.json()
            return {'massage': 'City not found'}, 404
        else:
            return {'massage': 'City or Indicator not found'}, 404
