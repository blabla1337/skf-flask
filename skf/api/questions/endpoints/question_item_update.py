from flask import request
from flask_restplus import Resource
from skf.api.questions.business import update_question
from skf.api.questions.serializers import question_item, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('questions', description='Operations related to questions')

@ns.route('/item/update/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

    @api.expect(question_item)
    @api.response(404, 'No results found', message)
    def put(self, id):
        data = request.json
        result = update_question(id, data)
        return result, 200, security_headers()

