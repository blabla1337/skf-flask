
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_items
from skf.api.checklist.serializers import checklist_items, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/items')
@api.response(404, 'Validation error')
class ChecklistCollection(Resource):

    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of checklist items.
        * Privileges required: **none**
        """
        result = get_checklist_items()
        return result, 200, security_headers()

