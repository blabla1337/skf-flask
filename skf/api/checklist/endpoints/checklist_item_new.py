from flask import request
from flask_restplus import Resource
from skf.api.checklist.business import create_checklist_item
from skf.api.checklist.serializers import checklist_create_update, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/new/item/type/<int:checklist_type>')
@api.doc(params={'checklist_type': 'The checklist type (0: ASVS lvl1, 1: ASVS lvl2, 2: ASVS lvl3, 3: MASVS lvl1, etc)'})
@api.response(404, 'Validation error', message)
class ChecklistItemNew(Resource):

    @api.expect(checklist_create_update)
    @api.response(400, 'No results found', message)
    def put(self, checklist_type):
        data = request.json
        val_alpha_num_special(data.get('content'))
        val_alpha_num_special(data.get('checklist_id'))
        val_num(data.get('question_id'))
        val_num(data.get('kb_id'))
        val_num(data.get('maturity'))
        val_num(checklist_type)
        result = create_checklist_item(checklist_type, data)
        return result, 200, security_headers()
