
from flask_restplus import Resource
from skf.api.checklist.business import get_checklist_item_question_sprint
from skf.api.checklist.serializers import checklist_items, message
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/question_sprint/<int:question_id>')
@api.doc(params={'questionID': 'The checklist item questionID'})
@api.response(404, 'Validation error', message)
class ChecklistItemQuestion(Resource):

    @api.marshal_with(checklist_items)
    @api.response(400, 'No results found', message)
    def get(self, question_id):
        val_num(question_id)
        result = get_checklist_item_question_sprint(question_id)
        return result, 200, security_headers()
