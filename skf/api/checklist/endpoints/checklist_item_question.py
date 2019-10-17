
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import get_checklist_item_question_sprint
from skf.api.checklist.serializers import checklist_items, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/question_sprint/<int:questionID>')
@api.doc(params={'questionID': 'The checklist item questionID'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, questionID):
        """
        Returns a list of checklist items correlated to question sprint identifier
        * Privileges required: **read**
        """
        validate_privilege(self, 'read')
        result = get_checklist_item_question_sprint(questionID)
        return result, 200, security_headers()
