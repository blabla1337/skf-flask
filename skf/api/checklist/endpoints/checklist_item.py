
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_item
from skf.api.checklist.serializers import checklist, message
from skf.api.checklist.parsers import id_arguments
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/<float:id>')
@api.response(404, 'Validation error')
class ChecklistItem(Resource):

    @api.expect(id_arguments)
    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    def get(self, id):
        """
        Returns a checklist item.
        * Privileges required: **none**
        * Specify the ID of the checklist item in the request URL path.
        """
        result = get_checklist_item(id)
        return result, 200, security_headers()
