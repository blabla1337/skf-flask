
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.questions_pre.business import get_pre_items
from skf.api.questions_pre.serializers import question_items, message
from skf.api.restplus import api

ns = api.namespace('questions_pre', description='Operations related to question pre items')


@ns.route('/items')
@api.response(404, 'Validation error', message)
class QuestionPreCollection(Resource):

    @api.marshal_with(question_items)
    @api.response(400, 'No results found', message)
    def get(self):
        """
        Returns list of question pre items.
        * Privileges required: **none**
        """
        result = get_pre_items()
        return result, 200, security_headers()
