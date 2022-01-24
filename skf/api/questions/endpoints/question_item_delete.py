from flask import request
from flask_restplus import Resource
from skf.api.questions.business import delete_question
from skf.api.questions.serializers import question_item, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('questions', description='Operations related to questions')

@ns.route('/item/delete/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintDelete(Resource):

    @api.response(404, 'No results found', message)
    def delete(self, id):
        val_num(id)
        result = delete_question(id)
        return result, 200, security_headers()

