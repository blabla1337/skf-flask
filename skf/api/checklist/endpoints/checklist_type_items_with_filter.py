
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item_types_with_filter
from skf.api.checklist.serializers import checklist_type_items, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/types/<int:maturity>')
@api.doc(params={'maturity': 'The checklist type naturity level'})
@api.response(404, 'Validation error', message)
class ChecklistCollection(Resource):

    @api.marshal_with(checklist_type_items)
    @api.response(400, 'No results found', message)
    def get(self, maturity):
        """
        Returns list of checklist types.
        * Privileges required: **none**
        """
        result = get_checklist_item_types_with_filter(maturity)
        return result, 200, security_headers()
