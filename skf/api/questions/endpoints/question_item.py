
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.questions.business import get_question_by_id
from skf.api.questions.serializers import question_item, message
from skf.api.questions.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_alpha, val_alpha_num, val_alpha_num_special

ns = api.namespace('questions', description='Operations related to question items')

@ns.route('/item/<int:question_id>')
@api.doc(params={'question_id': 'The question id to get info from'})
@api.response(404, 'Validation error', message)
class QuestionCollection(Resource):

    @api.marshal_with(question_item)
    #@api.expect(authorization)
    @api.response(400, 'No results found', message)
    def get(self, question_id):
        """
        Returns single question item by id
        * Privileges required: **none**
        """
        #validate_privilege(self, 'manage')
        result = get_question_by_id(question_id)
        return result, 200, security_headers()

