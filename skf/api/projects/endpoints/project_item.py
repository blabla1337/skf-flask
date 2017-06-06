
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import get_project_item
from skf.api.projects.serializers import project, message
from skf.api.projects.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error', message)
class ProjectItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(project)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a project item.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        user_id = select_userid_jwt(self)
        result = get_project_item(id, user_id)
        return result, 200, security_headers()
           
