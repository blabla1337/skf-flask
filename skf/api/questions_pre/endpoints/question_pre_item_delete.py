
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege, select_userid_jwt
from skf.api.questions_pre.business import delete_pre_question
from skf.api.questions_pre.serializers import question_pre_item_update, message
from skf.api.questions_pre.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('questions_pre', description='Operations related to question pre items')


@ns.route('/item/delete/<int:id>')
@api.doc(params={'id': 'The unique question id'})
@api.response(404, 'Validation error', message)
class QuestionpreDelete(Resource):

    @api.expect(authorization)
    @api.response(404, 'No results found', message)
    def delete(self, id):
        """
        Delete question pre item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = delete_pre_question(id)
        return result, 200, security_headers()

