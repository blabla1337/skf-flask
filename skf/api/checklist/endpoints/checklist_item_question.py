
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import get_checklist_item_question_sprint
from skf.api.checklist.serializers import checklist_items, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/question_sprint/<int:question_id>')
@api.doc(params={'questionID': 'The checklist item questionID'})
@api.response(404, 'Validation error', message)
class ChecklistItemQuestion(Resource):

    @api.expect(authorization)
    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, question_id):
        """
        Returns a list of checklist items correlated to question sprint identifier
        * Privileges required: **read**
        """
        val_num(question_id)
        validate_privilege(self, 'read')
        result = get_checklist_item_question_sprint(question_id)
        return result, 200, security_headers()
