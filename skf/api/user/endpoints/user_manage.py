
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.user.business import manage_user
from skf.api.user.serializers import manage, message
from skf.api.user.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('user', description='Operations related to users')

@ns.route('/manage/<int:id>')
@api.doc(params={'id': 'The user id'})
@api.response(404, 'Validation error', message)
class userManage(Resource):

    @api.expect(authorization, manage)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Manage an user.
        * Privileges required: **none**
        """
        data = request.json
        val_alpha(data.get('active'))
        val_num(id)
        validate_privilege(self, 'manage')
        result = manage_user(id, data)
        return result, 200, security_headers()

