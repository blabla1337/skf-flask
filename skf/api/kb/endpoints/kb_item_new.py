
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.kb.business import create_kb_item
from skf.api.kb.serializers import kb_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('kb', description='Operations related to kb items')


@ns.route('/new')
@api.response(404, 'Validation error', message)
class KBItemCreate(Resource):

    @api.expect(authorization, kb_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new kb item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        data = request.json
        result = create_kb_item(data)
        return result, 200, security_headers()

