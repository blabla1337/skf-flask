from flask import request
from flask_restplus import Resource
from skf.api.questions.business import get_question_by_id
from skf.api.questions.serializers import question_item, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('questions', description='Operations related to question items')

@ns.route('/item/<int:question_id>')
@api.doc(params={'question_id': 'The question id to get info from'})
@api.response(404, 'Validation error', message)
class QuestionCollection(Resource):

    @api.marshal_with(question_item)
    @api.response(400, 'No results found', message)
    def get(self, question_id):
        result = get_question_by_id(question_id)
        return result, 200, security_headers()

