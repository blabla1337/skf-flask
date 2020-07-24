
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.projects.business import update_project
from skf.api.projects.serializers import project_update, message
from skf.api.projects.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('project', description='Operations related to projects')

@ns.route('/update/<int:project_id>')
@api.doc(params={'project_id': 'The project id'})
@api.response(404, 'Validation error', message)
class KBItemUpdate(Resource):

    @api.expect(authorization, project_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, project_id):
        """
        Update a project item.
        * Privileges required: **edit**
        """
        data = request.json
        val_num(project_id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        val_alpha_num_special(data.get('version'))
        validate_privilege(self, 'edit')
        result = update_project(project_id, data)
        return result, 200, security_headers()

