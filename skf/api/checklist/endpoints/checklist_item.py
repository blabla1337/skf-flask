
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item
from skf.api.checklist.serializers import checklist, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/<float:checklistID>/type/<int:checklist_type>')
@api.doc(params={'checklistID': 'The checklist item checklistID (eg. 1.1)', 'checklist_type': 'The checklist type (0: ASVS, 1: MASVS)'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    def get(self, checklistID, checklist_type):
        """
        Returns a checklist item.
        * Privileges required: **none**
        """
        result = get_checklist_item(checklistID, checklist_type)
        return result, 200, security_headers()
