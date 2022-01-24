from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import get_sprint_results
from skf.api.sprints.serializers import sprint_results, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/results/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintResultItem(Resource):

    @api.marshal_with(sprint_results)
    @api.response(400, 'No results found', message)
    def get(self, id):
        result = get_sprint_results(id)
        return result, 200, security_headers()
