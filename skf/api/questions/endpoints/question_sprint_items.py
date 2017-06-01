
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, select_userid_jwt, val_num, val_alpha_num
from skf.api.questions.business import store_sprint_questions
from skf.api.questions.serializers import question, store_list_items_sprint, message
from skf.api.questions.parsers import authorization, id_arguments
from skf.api.restplus import api
from skf.database.questions import questions

ns = api.namespace('questions_sprint', description='Operations related to question items')


@ns.route('/items')
class QuestionCollection(Resource):

    @api.marshal_with(question)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of question items.
        Privileges required: none
        """
        question_items = questions.query.all()
        log("User requested list of question items", "LOW", "PASS")
        return question_items, 200, security_headers()


@ns.route('/store')
class QuestionSprintStoreCollection(Resource):

    @api.expect(authorization, store_list_items_sprint)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self):
        """
        Store list of question sprint items.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        store_sprint_questions(user_id, data)
        log("User stored new sprint question list", "MEDIUM", "PASS")
        return {'message': 'Sprint questions successfully created'}, 200, security_headers()
