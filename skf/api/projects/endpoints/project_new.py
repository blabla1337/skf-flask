from flask import request
from flask_restplus import Resource
from skf.api.projects.business import new_project
from skf.api.projects.serializers import project_new, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to project items')

@ns.route('/new')
@api.response(404, 'Validation error', message)
class ProjectItemNew(Resource):

    @api.expect(project_new)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self):
        data = request.json
        val_alpha_num_special(data.get('name'))
        val_alpha_num(data.get('version'))
        val_alpha_num_special(data.get('description'))
        result = new_project(data)   
        return result, 200, security_headers()

