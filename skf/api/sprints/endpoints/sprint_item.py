from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import get_sprint_item
from skf.api.sprints.serializers import sprint, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintItem(Resource):

    @api.marshal_with(sprint)
    @api.response(400, 'No results found', message)
    def get(self, id):
        val_num(id)
        result = get_sprint_item(id)
        return result, 200, security_headers()
