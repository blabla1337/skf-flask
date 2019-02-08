from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import create_checklist_type
from skf.api.checklist.serializers import checklist_type, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/create/type')
@api.response(404, 'Validation error', message)
class ChecklistCreate(Resource):

    @api.expect(authorization, checklist_type)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create a new checklist type.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        data = request.json
        result = create_checklist_type(data)
        return result, 200, security_headers()
