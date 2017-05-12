
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num
from skf.api.user.business import create_user
from skf.api.user.serializers import create, created, message
from skf.api.user.parsers import authorization
from skf.api.restplus import api
from skf.database.users import users

ns = api.namespace('user/create', description='Operations related to creating of users')


@ns.route('/')
class userCreation(Resource):

    @api.expect(authorization, create)
    @api.response(400, 'Validation Error', message)
    @api.marshal_with(created)
    def put(self):
        """
        Create an user.
        Privileges required: manage
        """
        data = request.json
        validate_privilege(self, 'manage')
        try:
            log("A new user created", "MEDIUM", "PASS")
            created_user = create_user(data)
            return created_user, 200, security_headers()
        except:
            log("User triggered error creating new user", "MEDIUM", "FAIL")
            return {'message': 'User not created'}, 400, security_headers()

