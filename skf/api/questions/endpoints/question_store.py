from flask import request
from flask_restplus import Resource
from skf.api.questions.business import store_questions
from skf.api.questions.serializers import store_list_items, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('questions', description='Operations related to question items')

@ns.route('/store/<int:maturity>')
@api.response(404, 'Validation error', message)
class QuestionSprintStoreCollection(Resource):

    @api.expect(store_list_items)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'No results found', message)
    def put(self, maturity):
        data = request.json
        result = store_questions(maturity, data)
        return result, 200, security_headers()
