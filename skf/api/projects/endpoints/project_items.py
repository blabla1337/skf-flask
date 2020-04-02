
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.projects.business import get_project_items
from skf.api.projects.serializers import page_of_project_items, message
from skf.api.projects.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('project', description='Operations related to project items')


@ns.route('/items')
@api.response(404, 'Validation error', message)
class ProjectCollection(Resource):

    @api.expect(authorization)
    @api.marshal_with(page_of_project_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of project items.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        result = get_project_items()        
        return result, 200, security_headers()

