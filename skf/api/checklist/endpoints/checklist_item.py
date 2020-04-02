
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item
from skf.api.checklist.serializers import checklist_update, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/<string:checklist_id>/type/<int:checklist_type>')
@api.doc(params={'checklist_id': 'The checklist item checklist_id (eg. 1.1)', 'checklist_type': 'The checklist type (0: ASVS lvl1, 1: ASVS lvl2, 2: ASVS lvl3, 3: MASVS lvl1, etc)'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.marshal_with(checklist_update)
    @api.response(400, 'No results found', message)
    def get(self, checklist_id, checklist_type):
        """
        Returns a checklist item.
        * Privileges required: **none**
        """
        val_alpha_num_special(checklist_id)
        val_num(checklist_type)
        result = get_checklist_item(checklist_id, checklist_type)
        return result, 200, security_headers()
