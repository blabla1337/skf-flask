
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers
from skf.api.user.business import login_user
from skf.api.user.serializers import login, message, token_auth
from skf.api.restplus import api

ns = api.namespace('user', description='Operations related to users')


@ns.route('/login')
@api.response(404, 'Validation error', message)
class userLogin(Resource):

    @api.expect(login)
    @api.marshal_with(token_auth)
    @api.response(400, 'No results found', token_auth)
    def post(self):
        """
        Login an user.
        * Privileges required: **none**
        """
        data = request.json
        result = login_user(data)
        return result, 200, security_headers()

