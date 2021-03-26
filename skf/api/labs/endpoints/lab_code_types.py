from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.labs.business import get_labs_code_types
from skf.api.labs.serializers import lab_code_items_types, message
from skf.api.restplus import api

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@ns.route('/code/items/types')
@api.doc(params={'code_type': 'The code type items based on name for example: php, asp, java'})
@api.response(404, 'Validation error', message)
class LabCollectionCode(Resource):
    @api.marshal_with(lab_code_items_types)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of code review lab types.
        * Privileges required: **none**
        """
        result = get_labs_code_types()
        return result, 200, security_headers()
 