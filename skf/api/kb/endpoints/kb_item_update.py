
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.kb.business import update_kb_item
from skf.api.kb.serializers import kb_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('kb', description='Operations related to kb items')


@ns.route('/update/<int:id>')
class KBItemUpdate(Resource):

    @api.expect(authorization, kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update a kb item.
        * Privileges required: **edit**
        * Specify the ID of the kb item in the request URL path.
        """
        validate_privilege(self, 'edit')
        data = request.json
        update_kb_item(id, data)
        return {'message': 'KB item successfully updated'}, 200, security_headers()

