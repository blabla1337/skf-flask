from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import create_checklist_item
from skf.api.checklist.serializers import checklist_create, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/new/item/<string:checklist_id>/type/<int:checklist_type>')
@api.doc(params={'checklist_id': 'The checklist item checklistID (eg. 1.1)', 'checklist_type': 'The checklist type (0: ASVS lvl1, 1: ASVS lvl2, 2: ASVS lvl3, 3: MASVS lvl1, etc)'})
@api.response(404, 'Validation error', message)
class ChecklistItemNew(Resource):

    @api.expect(authorization, checklist_create)
    @api.response(400, 'No results found', message)
    def put(self, checklist_id, checklist_type):
        """
        Create new checklist item.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        result = create_checklist_item(checklist_id, checklist_type, data)
        return result, 200, security_headers()
