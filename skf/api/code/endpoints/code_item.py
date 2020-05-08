
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.code.business import get_code_item
from skf.api.code.serializers import code, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('code', description='Operations related to code example items')

@ns.route('/<int:id>')
@api.doc(params={'id': 'The code item id'})
@api.response(404, 'Validation error', message)
class CodeItem(Resource):

    @api.marshal_with(code)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a code example item.
        * Privileges required: **none**
        """
        val_num(id)
        result = get_code_item(id)
        return result, 200, security_headers()

