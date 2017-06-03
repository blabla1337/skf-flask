
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import update_project
from skf.api.projects.serializers import project_update, message
from skf.api.projects.parsers import pagination_arguments, authorization
from skf.api.restplus import api

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error')
class ProjectItemUpdate(Resource):

    @api.expect(authorization, project_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Update a project item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = update_project(id, user_id, data)
        return result, 200, security_headers()

