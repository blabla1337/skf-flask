
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, select_userid_jwt, val_num, val_alpha_num
from skf.api.questions.business import store_pre_questions, update_pre_questions
from skf.api.questions.serializers import question, store_list_items_pre, update_list_items_pre, message
from skf.api.questions.parsers import authorization, id_arguments
from skf.api.restplus import api
from skf.database.questions_pre import questions_pre

ns = api.namespace('questions_pre', description='Operations related to question pre items')


@ns.route('/items')
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


@ns.route('/store')
class QuestionPreStoreCollection(Resource):

    @api.expect(authorization, store_list_items_pre)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self):
        """
        Store list of question pre items.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        data = request.json
        try:
            store_pre_questions(user_id, data)
            log("User stored new pre question list", "MEDIUM", "PASS")
            return {'message': 'Pre questions successfully created'}, 200, security_headers()
        except:
            log("User triggered error creating new pre question list", "MEDIUM", "FAIL")
            return {'message': 'Pre questions not stored'}, 400, security_headers()


@ns.route('/update/<int:id>')
class QuestionPreUpdateCollection(Resource):

    @api.expect(authorization, update_list_items_pre)
    @api.marshal_with(message, 'Success')
    @api.response(400, 'Validation Error', message)
    def put(self, id):
        """
        Update list of question pre items.
        Privileges required: edit
        """
        validate_privilege(self, 'edit')
        user_id = select_userid_jwt(self)
        val_num(id)
        data = request.json
        log("User updated pre question list", "MEDIUM", "PASS")
        update_pre_questions(id, user_id, data)
        return {'message': 'Pre questions successfully updated'}, 200, security_headers()


            