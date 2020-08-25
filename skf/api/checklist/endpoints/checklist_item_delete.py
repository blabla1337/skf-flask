from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import delete_checklist_item
from skf.api.checklist.serializers import checklist_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/delete/item/<string:checklist_id>')
@api.doc(params={'checklist_id': 'The unique identifier of the checklist item (2.1, 10.1.2 etc)', 'checklist_type': 'The checklist type (0: ASVS lvl1, 1: ASVS lvl2, 2: ASVS lvl3, 3: MASVS lvl1, etc)'})
@api.response(404, 'Validation error', message)
class ChecklistItemDelete(Resource):
    
    @api.expect(authorization)
    @api.response(400, 'No results found', message)
    def delete(self, checklist_id):
        """
        Delete a checklist item.
        * Privileges required: **delete**
        """
        val_alpha_num_special(checklist_id)
        validate_privilege(self, 'delete')
        result = delete_checklist_item(checklist_id)
        return result, 200, security_headers()
