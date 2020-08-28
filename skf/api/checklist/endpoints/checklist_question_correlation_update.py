from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import update_checklist_question_correlation
from skf.api.checklist.serializers import message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/update/item/correlation/<int:id>/question/<int:question_id>')
@api.doc(params={'id': 'The checklist item id'})
@api.response(404, 'Validation error', message)
class ChecklistQuestionCorrelationUpdate(Resource):

    @api.expect(authorization)
    @api.response(400, 'No results found', message)
    def get(self, id, question_id):
        """
        Update a checklist item correlated to question
        * Privileges required: **edit**
        """
        val_num(id)
        val_num(question_id)
        validate_privilege(self, 'edit')
        result = update_checklist_question_correlation(id, question_id)
        return result, 200, security_headers()
