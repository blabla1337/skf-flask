from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import delete_checklist_item
from skf.api.checklist.serializers import checklist_update, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/delete/item/<int:checklist_id>')
@api.doc(params={'checklist_id': 'The unique identifier of the checklist item'})
@api.response(404, 'Validation error', message)
class ChecklistItemUpdate(Resource):

    @api.expect(authorization)
    @api.response(400, 'No results found', message)
    def delete(self, checklist_id):
        """
        Delete a checklist item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = delete_checklist_item(checklist_id)
        return result, 200, security_headers()
