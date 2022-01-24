from flask import request
from flask_restplus import Resource
from skf.api.checklist.business import update_checklist_type
from skf.api.checklist.serializers import checklist_type, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist_types', description='Operations related to checklist types')

@ns.route('/update/<int:id>')
@api.doc(params={'id': 'The checklist type id'})
@api.response(404, 'Validation error', message)
class ChecklistUpdate(Resource):

    @api.expect(checklist_type)
    @api.response(400, 'No results found', message)
    def put(self, id):
        data = request.json
        val_num(id)
        val_alpha_num_special(data.get('name'))
        val_alpha_num_special(data.get('description'))
        result = update_checklist_type(id, data)
        return result, 200, security_headers()
