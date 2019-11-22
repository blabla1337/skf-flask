from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import create_checklist_type
from skf.api.checklist.serializers import checklist_type, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/create/type/<int:category_id>')
@api.response(404, 'Validation error', message)
class ChecklistCreate(Resource):

    @api.expect(authorization, checklist_type)
    @api.response(400, 'No results found', message)
    def put(self, category_id):
        """
        Create a new checklist type.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        result = create_checklist_type(data, category_id)
        return result, 200, security_headers()
