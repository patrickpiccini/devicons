from flask_restful import Resource
from flask import render_template, make_response

class Icon(Resource):
    def get(self):
        return make_response(render_template('index.html'))

    def post(self):
        pass

class HelloWorld(Resource):
    def get(self):
        return {'return': "Hello World"}

