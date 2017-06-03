
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import new_sprint
from skf.api.sprints.serializers import sprint_new, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/new')
@api.response(404, 'Validation error')
class ProjectSprintItemNew(Resource):

    @api.expect(authorization, sprint_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new sprint item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = new_sprint(user_id, data)
        return result, 200, security_headers()
