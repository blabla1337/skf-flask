
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import delete_sprint
from skf.api.sprints.serializers import message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintItemDelete(Resource):

    @api.expect(authorization)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        """
        Deletes sprint item.
        * Privileges required: **delete**
        """
        validate_privilege(self, 'delete')
        user_id = select_userid_jwt(self)
        result = delete_sprint(id, user_id)
        return result, 200, security_headers()
