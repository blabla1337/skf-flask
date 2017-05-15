
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num, val_alpha_num
from skf.api.questions.serializers import question, message
from skf.api.questions.parsers import authorization, id_arguments, pagination_arguments
from skf.api.restplus import api
from skf.database.questions_pre import questions_pre

ns = api.namespace('question_pre/items', description='Operations related to question pre items')


@ns.route('/')
class QuestionPreCollection(Resource):

    @api.marshal_with(question)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of question pre items.
        Privileges required: none
        """
        question_items = questions_pre.query.all()
        log("User requested list of question pre items", "LOW", "PASS")
        return question_items, 200, security_headers()


