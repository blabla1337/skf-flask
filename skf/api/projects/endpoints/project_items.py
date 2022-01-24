from flask import request
from flask_restplus import Resource
from skf.api.projects.business import get_project_items
from skf.api.projects.serializers import page_of_project_items, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('project', description='Operations related to project items')

@ns.route('/items')
@api.response(404, 'Validation error', message)
class ProjectCollection(Resource):

    @api.marshal_with(page_of_project_items)
    @api.response(400, 'No results found', message)
    def get(self):
        result = get_project_items()        
        return result, 200, security_headers()

