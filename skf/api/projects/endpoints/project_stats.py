from flask import request
from flask_restplus import Resource
from skf.api.projects.business import stats_project
from skf.api.projects.serializers import message, project_stats
from skf.api.projects.parsers import authorization
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to project items')

@ns.route('/stats/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error', message)
class ProjectStats(Resource):

    @api.marshal_with(project_stats)
    @api.response(400, 'No results found', message)
    def get(self, id):
        val_num(id)
        result = stats_project(id)
        return result, 200, security_headers()

