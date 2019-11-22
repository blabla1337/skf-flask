from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist_category.business import create_checklist_category
from skf.api.checklist_category.serializers import checklist, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist_category', description='Operations related to checklist category')

@ns.route('/new')
@api.response(404, 'Validation error', message)
class ChecklistCategoryCreate(Resource):

    @api.expect(authorization, checklist)
    @api.response(400, 'No results found', message)
    def put(self):
        """
        Create a new checklist category.
        * Privileges required: **edit**
        """
        validate_privilege(self, 'edit')
        data = request.json
        result = create_checklist_category(data)
        return result, 200, security_headers()
