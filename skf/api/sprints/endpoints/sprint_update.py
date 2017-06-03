
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, select_userid_jwt, val_num
from skf.api.sprints.business import new_sprint, update_sprint, delete_sprint, stats_sprint
from skf.api.sprints.serializers import sprint, sprint_update, sprint_new, message, sprint_stats
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error')
class ProjectSprintItemUpdate(Resource):

    @api.expect(authorization, sprint_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Update a sprint item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        result = update_sprint(id, user_id, data)
        return result, 200, security_headers()

