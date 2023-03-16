import logging

from flask_restful import Resource, reqparse
from flask import  Response

from src.resources.build_icons import BuildSVG

class Icon(Resource):
    def get(self) -> object:
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('icon', type=str, location='args')
            parser.add_argument('theme', type=str, location='args', default='dark')
            parser.add_argument('perline', type=str, location='args', default='30')
            parser.add_argument('size', type=str, location='args', default='48')

            args = parser.parse_args()


            icons = args.get('icon')
            theme = args.get('theme')
            perline = int(args.get('perline'))
            size = int(args.get('size'))


            if not icons and icons == None and icons == '' :
                logging.error('message: Please, inform the icon that you want - status: 400')
                return {'message': 'Please, inform the icon that you want',
                        'status': 400}, 400
            
            if theme and theme != 'dark' and theme != 'light' or theme == '' or theme == None:
                logging.error('message: You need choice "dark" or "light" theme - status: 400')
                return {'message': 'You need choice "dark" or "light" theme',
                        'status': 400}, 400

            if not perline or perline <= 0 or perline > 30:
                logging.error('message: Icons per line must be a number between 1 and 30 - status: 400')
                return {'message': 'Icons per line must be a number between 1 and 30',
                        'status': 400}, 400

            icons = icons.split(',')
            BSVG = BuildSVG(theme, perline, size)
            BSVG.build_icons(icons)
            svg_object = BSVG.build_svg()


            # return make_response(render_template('index.xml'))
            return Response(svg_object, mimetype='image/svg+xml')
        
        
        except Exception as error:
            logging.critical(error)
