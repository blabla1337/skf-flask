from flask import request
from flask_restplus import Resource
from skf.api.projects.business import delete_project
from skf.api.projects.serializers import message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to project items')

@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The project id'})
@api.response(404, 'Validation error', message)
class ProjectItemDelete(Resource):
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        val_num(id)
        result = delete_project(id)
        return result, 200, security_headers()
