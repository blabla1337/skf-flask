from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import delete_checklist_item
from skf.api.checklist.serializers import message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/delete/item/<int:id>')
@api.doc(params={'id': 'DB id of the checklist item'})
@api.response(404, 'Validation error', message)
class ChecklistItemDelete(Resource):
    
    @api.expect(authorization)
    @api.response(400, 'No results found', message)
    def delete(self, id):
        """
        Delete a checklist item.
        * Privileges required: **delete**
        """
        val_num(id)
        validate_privilege(self, 'delete')
        result = delete_checklist_item(id)
        return result, 200, security_headers()
