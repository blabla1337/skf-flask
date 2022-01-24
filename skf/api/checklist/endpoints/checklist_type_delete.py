from flask import request
from flask_restplus import Resource
from skf.api.checklist.business import delete_checklist_type
from skf.api.checklist.serializers import message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist_types', description='Operations related to checklist types')

@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The checklist type id'})
@api.response(404, 'Validation error', message)
class ChecklistDelete(Resource):

    @api.response(400, 'No results found', message)
    def delete(self, id):
        val_num(id)
        result = delete_checklist_type(id)
        return result, 200, security_headers()
