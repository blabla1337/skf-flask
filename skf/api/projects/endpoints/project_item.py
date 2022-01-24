from flask import request
from flask_restplus import Resource
from skf.api.projects.business import get_project_item
from skf.api.projects.serializers import project_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to kb items')

@ns.route('/item/<int:id>')
@api.doc(params={'id': 'The project item id'})
@api.response(404, 'Validation error', message)
class Project(Resource):

    @api.expect(get_project_item)
    @api.marshal_with(project_update)
    @api.response(400, 'No results found', message)
    def get(self, id):
        val_num(id)
        result = get_project_item(id)
        return result, 200, security_headers()

