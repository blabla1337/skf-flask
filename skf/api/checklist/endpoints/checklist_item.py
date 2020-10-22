
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item
from skf.api.checklist.serializers import checklist_item, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/<int:id>')
@api.doc(params={'id': 'The ID of the checklist item'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.marshal_with(checklist_item)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a single checklist item.
        * Privileges required: **none**
        """
        val_num(id)
        result = get_checklist_item(id)
        return result, 200, security_headers()
