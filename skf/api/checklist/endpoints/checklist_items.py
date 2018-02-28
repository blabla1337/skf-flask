
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_items
from skf.api.checklist.serializers import checklist_items, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/items/<int:id_checklist>')
@api.doc(params={'id_checklist': 'The checklist id (1: ASVS, 2: MASVS)'})
@api.response(404, 'Validation error', message)
class ChecklistCollection(Resource):

    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, id_checklist):
        """
        Returns list of checklist items.
        * Privileges required: **none**
        """
        result = get_checklist_items(id_checklist)
        return result, 200, security_headers()
