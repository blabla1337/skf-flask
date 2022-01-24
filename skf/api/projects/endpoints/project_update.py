from flask import request
from flask_restplus import Resource
from skf.api.projects.business import update_project
from skf.api.projects.serializers import project_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to projects')

@ns.route('/update/<int:project_id>')
@api.doc(params={'project_id': 'The project id'})
@api.response(404, 'Validation error', message)
class KBItemUpdate(Resource):

    @api.expect(project_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, project_id):
        data = request.json
        val_num(project_id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        val_alpha_num_special(data.get('version'))
        result = update_project(project_id, data)
        return result, 200, security_headers()

