
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, val_num
from skf.api.user.business import activate_user
from skf.api.user.serializers import activate, message
from skf.api.restplus import api
from skf.database.users import users

ns = api.namespace('user/activate', description='Operations related to activation of users')


@ns.route('/<int:id>')
class userActivation(Resource):

    @api.expect(activate)
    @api.response(400, 'Validation Error', message)
    @api.marshal_with(message, 'Success')
    def put(self, id):
        """
        Activate an user.
        Privileges required: none
        """
        data = request.json
        val_num(id)
        try:
            log("User is activated", "HIGH", "PASS", self)
            activate_user(id, data)
            return {'message': 'User successfully activated'}, 200, security_headers()
        except:
            log("User is activation failed", "HIGH", "FAIL", self)
            return {'message': 'User could not be activated'}, 400, security_headers()