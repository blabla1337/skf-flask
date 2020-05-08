
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.user.business import list_users
from skf.api.user.serializers import user_items, message
from skf.api.user.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('user', description='Operations related to users')

@ns.route('/list')
@api.response(404, 'Validation error', message)
class userList(Resource):

    @api.expect(authorization)
    @api.marshal_with(user_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        List available users.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = list_users()
        return result, 200, security_headers()
