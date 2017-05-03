
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers
from skf.api.user.business import login_user
from skf.api.user.serializers import login, message, token_auth
from skf.api.restplus import api
from skf.database.users import users

ns = api.namespace('user/login', description='Operations related to login of users')


@ns.route('/')
class userLogin(Resource):

    @api.expect(login)
    @api.response(400, 'Validation Error', message)
    @api.marshal_with(token_auth, 'Authorization token')
    def post(self):
        """
        Login an user.
        Privileges required: none
        """
        try:
            log("User successfully logedin", "HIGH", "PASS", self)
            token = login_user(request.json)
            return {'Authorization token': token}, 200, security_headers()
        except:
            log("User login failed", "HIGH", "FAIL", self)
            return {'message': 'Wrong username/password'}, 400, security_headers()
