
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, val_num
from skf.api.user.business import activate_user
from skf.api.user.serializers import activate, message
from skf.api.restplus import api
from skf.database.users import users

ns = api.namespace('user', description='Operations related to users')


@ns.route('/activate/<int:id>')
@api.doc(params={'id': 'The user id'})
@api.response(404, 'Validation error')
class userActivation(Resource):

    @api.expect(activate)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Activate an user.
        * Privileges required: **none**
        """
        data = request.json
        result = activate_user(id, data)
        return result, 200, security_headers()

