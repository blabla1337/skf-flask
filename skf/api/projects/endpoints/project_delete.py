
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import delete_project
from skf.api.projects.serializers import message
from skf.api.projects.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error')
class ProjectItemDelete(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        """
        Deletes project item.
        * Privileges required: **delete**
        """
        validate_privilege(self, 'delete')
        user_id = select_userid_jwt(self)
        result = delete_project(id, user_id)
        return result, 200, security_headers()
