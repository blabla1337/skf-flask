from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, val_num
from skf.api.labs.business import get_labs_code_status
from skf.api.labs.serializers import labs_code_status, message
from skf.api.restplus import api

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@ns.route('/code/items/code/<int:code_id>/solution/<int:solution_id>')
@api.doc(params={'code_id': 'The unique id of the code item', 'solution_id': 'The unique id of the code item solution'})
@api.response(404, 'Validation error', message)
class LabCollectionCodeStatus(Resource):
    @api.marshal_with(labs_code_status)
    @api.response(400, 'No results found', message)
    def get(self, code_id, solution_id):
        """
        Returns status if solution was correct for code item.
        * Privileges required: **none**
        """
        val_num(code_id)
        val_num(solution_id)
        result = get_labs_code_status(code_id, solution_id)
        return result, 200, security_headers()
 