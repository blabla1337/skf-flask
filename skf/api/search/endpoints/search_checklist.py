import json
from flask import request
from flask_restplus import Resource
from skf.api.search.business import search_checklist
from skf.api.search.serializers import message, checklist
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('search', description='Operations related to the search functionality')

@ns.route('/checklist/<string:search_string>')
@api.response(404, 'Validation error', message)
class SearchChecklist(Resource):

    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    def get(self, search_string):
        result = search_checklist(search_string)
        return result, 200, security_headers()
 