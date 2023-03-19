import os
import logging

from flask import Flask
from flask_restful import Api

from src.utils.build_json import build_json, load_select_options

from src.resources.icons import Icon
from src.resources.home import Home

from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

# Criation requirements files from logging


HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")

# Creation JSON files with svg names
build_json()
load_select_options()

app = Flask(__name__, template_folder='tamplate')
api = Api(app)

api.add_resource(Icon, '/icons', endpoint='icons')
api.add_resource(Home, '/', endpoint='/')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)