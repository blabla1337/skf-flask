from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import update_checklist_item
from skf.api.checklist.serializers import checklist_create_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/update/item/<int:id>')
@api.doc(params={'id': 'The checklist item db ID '})
@api.response(404, 'Validation error', message)
class ChecklistItemUpdate(Resource):

    @api.expect(authorization, checklist_create_update)
    @api.response(400, 'No results found', message)
    def put(self, id):
        """
        Update a checklist item.
        * Privileges required: **edit**
        """
        data = request.json
        val_num(checklist_type)
        val_num(id)
        val_num(data.get('maturity'))
        val_num(data.get('question_id'))
        val_alpha_num_special(data.get('add_resources'))
        val_num(data.get('kb_id'))
        val_alpha_num(data.get('include_always'))
        val_alpha_num_special(data.get('content'))
        validate_privilege(self, 'edit')
        result = update_checklist_item(id, checklist_type, data)
        return result, 200, security_headers()
