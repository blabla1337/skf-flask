
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.code.business import create_code_item
from skf.api.code.serializers import code_properties, message
from skf.api.code.parsers import authorization
from skf.api.restplus import api

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
        validate_privilege(self, 'edit')
        data = request.json
        result = create_code_item(data, category_id)
        return result, 200, security_headers()

