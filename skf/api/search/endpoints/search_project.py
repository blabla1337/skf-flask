from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.search.business import search_project
from skf.api.search.serializers import message, project
from skf.api.restplus import api
from skf.api.search.parsers import authorization
import json

ns = api.namespace('search', description='Operations related to the search functionality')

@ns.route('/project/<string:search_string>')
@api.response(404, 'Validation error', message)
class SearchProject(Resource):

    @api.expect(authorization)
    @api.marshal_with(project)
    @api.response(400, 'No results found', message)
    def get(self, search_string):
        """
        Returns list of search project hits.
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        result = search_project(search_string)
        return result, 200, security_headers()
 