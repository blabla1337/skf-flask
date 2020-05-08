
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.user.business import create_user
from skf.api.user.serializers import create, created, message
from skf.api.user.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('user', description='Operations related to users')

@ns.route('/create')
@api.response(404, 'Validation error', message)
class userCreation(Resource):

    @api.expect(authorization, create)
    @api.marshal_with(created)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create an user.
        * Privileges required: **manage**
        """
        data = request.json
        val_alpha_num_special(data.get('username'))
        val_alpha_num_special(data.get('privilege_id'))
        validate_privilege(self, 'manage')
        result = create_user(data)
        return result, 200, security_headers()
