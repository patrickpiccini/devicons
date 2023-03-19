import logging
from flask_restful import Resource
from flask import render_template, make_response 

class Home(Resource):
    def get(self) -> object:
        try:
            return make_response(render_template('index.html'))
        
        except Exception as error:
            logging.error(error)
