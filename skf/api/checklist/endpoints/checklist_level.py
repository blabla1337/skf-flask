
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_items_lvl
from skf.api.checklist.serializers import checklist_items, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/level/<int:level>')
@api.doc(params={'level': 'The checklist level'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.marshal_list_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, level):
        """
        Returns list of checklist items based on level.
        * Privileges required: **none**
        """
        lvl = level
        result = get_checklist_items_lvl(lvl)
        return result, 200, security_headers()
