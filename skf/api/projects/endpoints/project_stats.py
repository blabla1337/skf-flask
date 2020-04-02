
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import stats_project
from skf.api.projects.serializers import message, project_stats
from skf.api.projects.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/stats/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error', message)
class ProjectStats(Resource):

    @api.expect(authorization)
    @api.marshal_with(project_stats)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns project stats.
        * Privileges required: **read**
        """
        val_num(id)
        validate_privilege(self, 'read')
        result = stats_project(id)
        return result, 200, security_headers()

