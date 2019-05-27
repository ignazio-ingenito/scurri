import urllib

from flask import Flask, request, jsonify, abort
from flask_restplus import fields, Api, Resource, reqparse
from webapp.postcode import Postcode

app = Flask(__name__)
api = Api(app, default='Postcode',
          version='1.0',
          title='Postcode REST API',
          description='Postcode REST API fro Scurri')

post_parser = reqparse.RequestParser()
post_parser.add_argument('poscodes',  type=list, help='poscode list', location='json')

postcode_model = api.model('Postcode', {
    'in_postcode': fields.String(description='input postcode'),
    'fmt_postcode': fields.String(description='formatted postcode'),
    'outward_code': fields.String(description='outward code'),
    'inward_code': fields.String(description='inward code'),
    'postcode_area': fields.String(description='postcode area'),
    'postcode_district': fields.String(description='postcode district'),
    'postcode_sector': fields.String(description='postcode sector'),
    'postcode_unit': fields.String(description='postcode unit'),
    'is_valid': fields.Boolean(description='is_valid'),
    'message': fields.String(description='message'),
})

multiple_postcode_request = api.model('Multiple Postcode request', {
    'postcodes': fields.List(fields.String(), description='List of postcodes')
})

@api.route('/postcode/<id>')
@api.response(500, 'Invalid re')
class PostcodeResource(Resource):
    @api.marshal_with(postcode_model)
    @api.expect(id)
    def get(self, id):
        id = urllib.parse.unquote(id)
        p = Postcode()
        p.split_validate(id)
        return p

@api.route('/postcodes')
class MultiplePostcodeResource(Resource):
    @api.expect(multiple_postcode_request)
    @api.marshal_with(postcode_model)
    def post(self):
        ids = request.json['postcodes']

        result = []
        for id in ids:
            p = Postcode()
            p.split_validate(id)
            result.append(p)

        return result

@api.errorhandler(Exception)
@app.errorhandler(Exception)
def error_handler(e):
    response = jsonify(status = 401,
                       message = f"DecodeError {str(e)}",
                       success = False), 401
    return response