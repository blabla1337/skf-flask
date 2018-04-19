
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.sprints.business import stats_sprint
from skf.api.sprints.serializers import message, sprint_stats
from skf.api.sprints.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('sprint', description='Operations related to sprint items')


@ns.route('/stats/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error', message)
class ProjectSprintStats(Resource):

    @api.expect(authorization)
    @api.marshal_with(sprint_stats)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns sprints stats.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        user_id = select_userid_jwt(self)
        result = stats_sprint(id)
        return result, 200, security_headers()
