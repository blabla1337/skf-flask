
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import get_sprint_item
from skf.api.sprints.serializers import sprint, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error')
class ProjectSprintItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(sprint)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a sprint item.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        user_id = select_userid_jwt(self)
        result = get_sprint_item(id, user_id)
        return result, 200, security_headers()
