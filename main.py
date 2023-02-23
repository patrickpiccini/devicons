from flask import Flask
from flask_restful import Api

from src.resources.icons import Icon
from src.resources.home import Home

app = Flask(__name__, template_folder='src/tamplate')
api = Api(app)

api.add_resource(Icon, '/icons', endpoint='icons')
api.add_resource(Home, '/', endpoint='/')

if __name__ == '__main__':
    app.run(debug=True)