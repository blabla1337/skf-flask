
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import new_sprint
from skf.api.sprints.serializers import sprint_new, message
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha_num, val_alpha_num_special

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/new')
@api.response(404, 'Validation error', message)
class ProjectSprintItemNew(Resource):

    @api.expect(authorization, sprint_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create new sprint item.
        * Privileges required: **edit**
        """
        data = request.json
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        val_num(data.get('project_id'))
        validate_privilege(self, 'edit')
        result = new_sprint(data)
        return result, 200, security_headers()
