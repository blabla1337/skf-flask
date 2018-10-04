
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.questions_sprint.business import get_sprint_items
from skf.api.questions_sprint.serializers import question_items, message
from skf.api.restplus import api

ns = api.namespace('questions_sprint', description='Operations related to question items')


@ns.route('/items/<int:checklist_type>')
@api.doc(params={'checklist_type': 'The question checklist type used for sprint process step'})
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(question_items)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def get(self, checklist_type):
        """
        Returns list of question items.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = get_sprint_items(checklist_type)
        return result, 200, security_headers()

