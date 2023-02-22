from flask import Flask
from flask_restful import Api

from src.resources.images import HelloWorld
from src.resources.images import Icon

app = Flask(__name__, template_folder='src\\tamplate')
api = Api(app)


api.add_resource(HelloWorld, '/')
api.add_resource(Icon, '/icons')

if __name__ == '__main__':
    app.run(debug=True)