
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.code.business import get_code_item
from skf.api.code.serializers import code, message
from skf.api.restplus import api

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/<int:id>')
@api.doc(params={'id': 'The code item id'})
@api.response(404, 'Validation error')
class CodeItem(Resource):

    @api.marshal_with(code)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a code example item.
        * Privileges required: **none**
        """
        result = get_code_item(id)
        return result, 200, security_headers()

