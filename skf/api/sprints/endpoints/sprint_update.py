from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import update_sprint
from skf.api.sprints.serializers import sprint_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintItemUpdate(Resource):
    
    @api.expect(sprint_update)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, id):
        data = request.json
        val_num(id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        result = update_sprint(id, data)
        return result, 200, security_headers()

