from flask import request
from flask_restplus import Resource
from skf.api.checklist.business import update_checklist_item
from skf.api.checklist.serializers import checklist_create_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/update/item/<int:id>')
@api.doc(params={'id': 'The checklist item db ID '})
@api.response(404, 'Validation error', message)
class ChecklistItemUpdate(Resource):

    @api.expect(checklist_create_update)
    @api.response(400, 'No results found', message)
    def put(self, id):
        data = request.json
        val_num(id)
        val_num(data.get('maturity'))
        val_num(data.get('question_id'))
        val_alpha_num_special(data.get('add_resources'))
        val_num(data.get('kb_id'))
        val_alpha_num_special(data.get('content'))
        result = update_checklist_item(id, data)
        return result, 200, security_headers()
