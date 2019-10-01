
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.code.business import get_code_items
from skf.api.code.serializers import code_items, message
from skf.api.restplus import api

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/items')
@api.response(404, 'Validation error', message)
class CodeCollection(Resource):

    @api.marshal_with(code_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of code example items.
        * Privileges required: **none**
        """
        result = get_code_items()
        return result, 200, security_headers()
