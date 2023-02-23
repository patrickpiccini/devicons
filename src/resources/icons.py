from flask_restful import Resource, reqparse
from flask import render_template, make_response, Markup, Response

from src.resources.build_icons import BuildSVG

class Icon(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('icon', type=str, location='args', default='devicons')
        parser.add_argument('theme', type=str, location='args', default='dark')
        parser.add_argument('perline', type=str, location='args', default='1')
        args = parser.parse_args()

        icons = args.get('icon').split(',')
        theme = args.get('theme')
        perline = int(args.get('perline'))

        if not icons:
            return {'message': 'Please, inform the icon that you want',
                    'status': 400}, 400
        
        if theme and theme != 'dark' and theme != 'light':
            return {'message': 'You need choice "dark" or "light" theme',
                    'status': 400}, 400

        if not perline or perline <= 0 or perline > 20:
               return {'message': 'Icons per line must be a number between 1 and 20',
                    'status': 400}, 400


        BSVG = BuildSVG(theme, perline)
        BSVG.build_icons(icons)
        svg_object = BSVG.build_svg()


        # return make_response(render_template('index.xml'))
        return Response(svg_object, mimetype='image/svg+xml')

    def post(self):
        pass
