from flask import request
from flask_restplus import Resource
from skf.api.sprints.business import delete_sprint
from skf.api.sprints.serializers import message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('sprint', description='Operations related to sprint items')

@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The sprint id'})
@api.response(404, 'Validation error', message)
class ProjectSprintItemDelete(Resource):

    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def delete(self, id):
        val_num(id)
        result = delete_sprint(id)
        return result, 200, security_headers()
