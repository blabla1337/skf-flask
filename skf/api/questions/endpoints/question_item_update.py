
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions.business import update_question
<<<<<<< HEAD
from skf.api.questions.serializers import question_item, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions', description='Operations related to questions')

=======
from skf.api.questions.serializers import question_item_update, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('questions', description='Operations related to questions')


>>>>>>> origin/master
@ns.route('/item/update/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionSprintCollection(Resource):

<<<<<<< HEAD
    @api.expect(authorization, question_item)
=======
    @api.expect(authorization, question_item_update)
>>>>>>> origin/master
    @api.response(404, 'No results found', message)
    def put(self, id):
        """
        Update question sprint item.
        * Privileges required: **edit**
        """
<<<<<<< HEAD
        validate_privilege(self, 'edit')
        data = request.json
=======
        data = request.json
        val_num(id)
        val_num(data.get('checklist_type'))
        val_alpha_num_special(data.get('question'))
        validate_privilege(self, 'edit')
>>>>>>> origin/master
        result = update_question(id, data)
        return result, 200, security_headers()

