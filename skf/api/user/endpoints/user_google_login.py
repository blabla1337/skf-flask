
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers
from skf.api.user.business import google_login
from skf.api.user.serializers import login, message, token_auth, google_login
from skf.api.restplus import api

ns = api.namespace('user', description='Operations related to users')


@ns.route('/google_login')
@api.response(404, 'Validation error', message)
class googleLogin(Resource):

    @api.expect(google_login)
    @api.marshal_with(token_auth)
    @api.response(400, 'No results found', token_auth)
    def post(self):
        """
        Login an user.
        * Privileges required: **none**
        """
        data = request.json
        result = google_login(data)
        return result, 200, security_headers()