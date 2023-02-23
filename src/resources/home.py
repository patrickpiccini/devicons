from flask_restful import Resource, reqparse
from flask import render_template, make_response

class Home(Resource):
    def get(self):
        return {'message': 'home'}

    def post(self):
        pass