from flask_restful import Resource, reqparse
from flask import render_template, make_response, Markup

class Icon(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('icon', type=str, location='args')
        parser.add_argument('mode', type=str, location='args', default='dark')
        parser.add_argument('perline', type=str, location='args', default="1")
        args = parser.parse_args()

        icons = args['icon'].split(',')
        mode = args['mode']
        perline = args['perline']

        return make_response(render_template('index.xml'))

    def post(self):
        pass
