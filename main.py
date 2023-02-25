from flask import Flask
from flask_restful import Api

from src.utils.build_json import build_json, load_select_options

from src.resources.icons import Icon
from src.resources.home import Home

# Creation JSON files with svg names
build_json()
load_select_options()

app = Flask(__name__, template_folder='src/tamplate')
api = Api(app)

api.add_resource(Icon, '/icons', endpoint='icons')
api.add_resource(Home, '/', endpoint='/')

if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True, )