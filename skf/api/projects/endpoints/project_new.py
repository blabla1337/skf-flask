
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import new_project
from skf.api.projects.serializers import project_new, message
from skf.api.projects.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/new')
@api.response(404, 'Validation error', message)
class ProjectItemNew(Resource):

    @api.expect(authorization, project_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new project item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = new_project(user_id, data)   
        return result, 200, security_headers()

