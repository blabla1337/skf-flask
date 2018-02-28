
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item
from skf.api.checklist.serializers import checklist, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/<float:id>,<int:id_checklist>')
@api.doc(params={'id': 'The checklist item id'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    # id_checklist
    # 1 = ASVS
    # 2 = MASVS
    def get(self, id, id_checklist):
        """
        Returns a checklist item.
        * Privileges required: **none**
        """
        result = get_checklist_item(id, id_checklist)
        return result, 200, security_headers()
