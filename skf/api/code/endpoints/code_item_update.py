
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.code.business import update_code_item
from skf.api.code.serializers import code_update, message
from skf.api.code.parsers import authorization
from skf.api.restplus import api
from skf.database.code_items import code_items

ns = api.namespace('code', description='Operations related to code example items')


@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The code item id'})
@api.response(404, 'Validation error')
class CodeItemUpdate(Resource):

    @api.expect(authorization, code_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a code example item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        result = update_code_item(id, data)
        return result, 200, security_headers()
 