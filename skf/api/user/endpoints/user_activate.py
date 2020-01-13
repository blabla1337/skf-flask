
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.user.business import activate_user
from skf.api.user.serializers import activate, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('user', description='Operations related to users')


@ns.route('/activate/<int:id>')
@api.doc(params={'id': 'The user id'})
@api.response(404, 'Validation error', message)
class userActivation(Resource):

    @api.expect(activate)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        data = request.json
        val_num(data.get('accessToken'))
        val_alpha_num_special(data.get('username'))
        val_num(id)
        result = activate_user(id, data)
        return result, 200, security_headers()

