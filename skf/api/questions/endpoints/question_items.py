
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.questions.business import get_questions
from skf.api.questions.serializers import question_items, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions', description='Operations related to question items')


@ns.route('/items/<int:checklist_type>')
@api.doc(params={'checklist_type': 'The question checklist type used for sprint process step'})
@api.response(404, 'Validation error', message)
class QuestionCollection(Resource):

    @api.marshal_with(question_items)
    #@api.expect(authorization)
    @api.response(400, 'No results found', message)
    def get(self, checklist_type):
        """
        Returns list of question items.
        * Privileges required: **none**
        """
        #validate_privilege(self, 'manage')
        result = get_questions(checklist_type)
        return result, 200, security_headers()

