
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import update_sprint
from skf.api.sprints.serializers import sprint_update, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintItemUpdate(Resource):

    @api.expect(authorization, sprint_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Update a sprint item.
        * Privileges required: **edit**
        """
        val_num(id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = update_sprint(id, user_id, data)
        return result, 200, security_headers()

