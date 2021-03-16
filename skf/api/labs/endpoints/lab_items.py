
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.labs.business import get_labs
from skf.api.labs.serializers import lab_items, message
from skf.api.restplus import api

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@ns.route('/items')
@api.response(404, 'Validation error', message)
class LabCollection(Resource):
    @api.marshal_with(lab_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of labs.
        * Privileges required: **none**
        """
        result = get_labs()
        return result, 200, security_headers()
 