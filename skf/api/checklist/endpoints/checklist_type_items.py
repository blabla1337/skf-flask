from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item_types
from skf.api.checklist.serializers import checklist_type_items, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist_types', description='Operations related to checklist types')

@ns.route('/types/<int:id>')
@api.response(404, 'Validation error', message)
class ChecklistCollection(Resource):

    @api.marshal_with(checklist_type_items)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns list of checklist types.
        * Privileges required: **none**
        """
        val_num(id)
        result = get_checklist_item_types(id)
        return result, 200, security_headers()
