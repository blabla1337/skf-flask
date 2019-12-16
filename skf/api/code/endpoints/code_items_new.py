
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.code.business import create_code_item
from skf.api.code.serializers import code_properties, message
from skf.api.code.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('code', description='Operations related to code examples items')

@ns.route('/new/<int:category_id>')
@api.response(404, 'Validation error', message)
class CodeItemCreate(Resource):

    @api.expect(authorization, code_properties)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, category_id):
        """
        Create new code example item.
        * Privileges required: **edit**
        """
        data = request.json
        val_alpha_num_special(data.get('title'))
        val_alpha_num(data.get('code_lang'))
        val_num(category_id)
        validate_privilege(self, 'edit')
        result = create_code_item(data, category_id)
        return result, 200, security_headers()

