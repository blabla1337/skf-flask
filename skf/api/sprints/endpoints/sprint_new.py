from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import new_sprint
from skf.api.sprints.serializers import sprint_new, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/new')
@api.response(404, 'Validation error', message)
class ProjectSprintItemNew(Resource):

    @api.expect(sprint_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        data = request.json
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        val_num(data.get('project_id'))
        result = new_sprint(data)
        return result, 200, security_headers()
