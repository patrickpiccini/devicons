import json
import logging

from src.build_icons import BuildSVG


def lambda_handler(event, context):
    try:
        if not event.get('queryStringParameters'):
            return {'statusCode': 400, 'body': json.dumps({'message': 'Please, inform the icon that you want'})}

        icons = event['queryStringParameters'].get('icons', 'Python,Java')
        theme = event['queryStringParameters'].get('theme', 'dark')
        perline = int(event['queryStringParameters'].get('perline', 30))
        size = int(event['queryStringParameters'].get('size', 48))

        if not icons or icons == None or icons == '':
            logging.error(
                'message: Please, inform the icon that you want - status: 400')
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Please, inform the icon that you want'})
            }

        if theme and theme != 'dark' and theme != 'light' or theme == '' or theme == None:
            logging.error(
                'message: You need choice "dark" or "light" theme - status: 400')
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'You need choice "dark" or "light" theme'})
            }

        if not perline or perline <= 0 or perline > 30:
            logging.error(
                'message: Icons per line must be a number between 1 and 30 - status: 400')
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Icons per line must be a number between 1 and 30'})
            }

        icons = icons.split(',')
        BSVG = BuildSVG(theme, perline, size)
        BSVG.build_icons(icons)
        svg_object = BSVG.build_svg()

        # svg_base64 = base64.b64encode(svg_object.encode('utf-8')).decode('utf-8')

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'image/svg+xml',
                'Cache-Control': 'no-cache',
                'Access-Control-Allow-Origin': '*'
            },
            'body': svg_object,
            'isBase64Encoded': False
        }

        # return svg_base64

    except Exception as error:
        logging.critical(f"Internal server error: {error}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Internal server error: {error}"})
        }
