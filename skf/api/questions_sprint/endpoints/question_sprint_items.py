
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.questions_sprint.business import get_sprint_items
from skf.api.questions_sprint.serializers import question_items, question_sprint_item, message
from skf.api.restplus import api

ns = api.namespace('questions_sprint', description='Operations related to question items')


@ns.route('/items')
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(question_sprint_item)
    @api.marshal_with(question_items)
    @api.response(400, 'No results found', message)
    def post(self):
        """
        Returns list of question items.
        * Privileges required: **none**
        """
        data = request.json
        result = get_sprint_items(data)
        return result, 200, security_headers()

