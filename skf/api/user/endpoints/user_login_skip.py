
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers
from skf.api.user.business import login_skip
from skf.api.user.serializers import login, message, token_auth
from skf.api.restplus import api
from skf.api.security import log

ns = api.namespace('user', description='Operations related to users')

@ns.route('/skip')
@api.response(404, 'Validation error', message)
class userLogin(Resource):

    @api.expect()
    @api.marshal_with(token_auth)
    @api.response(400, 'No results found', token_auth)
    def get(self):
        """
        Login an anonymous user.
        * Privileges required: **none**
        """
        result = login_skip()
        return result, 200, security_headers()

