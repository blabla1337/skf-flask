import logging

from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.user.business import activate_user
from skf.api.user.serializers import activate
from skf.api.user.parsers import user_activation_arguments
from skf.api.restplus import api
from skf.database.models import users

log = logging.getLogger(__name__)

ns = api.namespace('user/activate', description='Operations related to activation of users')


@ns.route('/<int:id>')
class userActivation(Resource):

    @api.expect(user_activation_arguments)
    @api.marshal_with(activate)
    def put(self, id):
        """
        Activate an user.
        """
        data = request.json
        sys.exit(data)
        activate_user(id, data)
        return None, 200, security_headers()
