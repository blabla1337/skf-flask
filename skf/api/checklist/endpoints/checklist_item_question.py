
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import get_checklist_item_question
from skf.api.checklist.serializers import checklist, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/question/<int:questionID>')
@api.doc(params={'questionID': 'The checklist item questionID'})
@api.response(404, 'Validation error', message)
class ChecklistItem(Resource):

    @api.expect(authorization)
    @api.marshal_with(checklist)
    @api.response(400, 'No results found', message)
    def get(self, questionID):
        """
        Returns a checklist item.
        * Privileges required: **manage**
        """
        validate_privilege(self, 'manage')
        result = get_checklist_item_question(questionID)
        return result, 200, security_headers()
