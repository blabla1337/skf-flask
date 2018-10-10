
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import get_checklist_item_question_pre
from skf.api.checklist.serializers import checklist_items, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/question_pre/<int:questionID>')
@api.doc(params={'questionID': 'The checklist items questionID'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, questionID):
        """
        Returns a checklist item based on question pre identifier.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = get_checklist_item_question_pre(questionID)
        return result, 200, security_headers()
