from flask import request
from flask_restplus import Resource
from skf.api.questions.business import new_question
from skf.api.questions.serializers import question_item, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('questions', description='Operations related to question sprint items')

@ns.route('/item/new')
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(question_item)
    @api.response(400, 'No results found', message)
    def put(self):
        data = request.json
        val_alpha_num(data.get('question'))
        result = new_question(data)
        return result, 200, security_headers()

