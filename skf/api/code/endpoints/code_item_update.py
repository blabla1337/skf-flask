
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.code.business import update_code_item
from skf.api.code.serializers import code_properties, message
from skf.api.code.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The code item id'})
@api.response(404, 'Validation error', message)
class CodeItemUpdate(Resource):

    @api.expect(authorization, code_properties)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a code example item.
        * Privileges required: **manage**
        """
        data = request.json
        val_alpha_num_special(data.get('title'))
        val_alpha_num(data.get('code_lang'))
        val_num(id)
        validate_privilege(self, 'manage')
        result = update_code_item(id, data)
        return result, 200, security_headers()
 