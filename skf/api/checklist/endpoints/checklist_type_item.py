from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_type_by_id
from skf.api.checklist.serializers import checklist_type, message
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist_types', description='Operations related to checklist types')

@ns.route('/type/<int:checklist_type_id>')
@api.response(404, 'Validation error', message)
class ChecklistCollection(Resource):

    @api.marshal_with(checklist_type)
    @api.response(400, 'No results found', message)
    def get(self, checklist_type_id):
        """
        Returns a single checklist types content by the checklist type id
        * Privileges required: **none**
        """
        val_num(checklist_type_id)
        result = get_checklist_type_by_id(checklist_type_id)
        return result, 200, security_headers()