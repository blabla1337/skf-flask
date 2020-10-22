
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist.business import get_checklist_item_questions_git
from skf.api.checklist.serializers import checklist_items_questions, message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special

ns = api.namespace('checklist', description='Operations related to checklist items')

@ns.route('/item/gitplugin/<int:checklist_type>')
@api.response(404, 'Validation error', message)
class ChecklistItemQuestions(Resource):
<<<<<<< HEAD
    
=======
>>>>>>> origin/master
    @api.marshal_with(checklist_items_questions)
    @api.response(400, 'No results found', message)
    def get(self, checklist_type):
        """
        Returns a list of checklist items, questions, knowledgebase items correlated to a checklist type
        * Privileges required: **none**
        """
        val_num(checklist_type)
        result = get_checklist_item_questions_git(checklist_type)
        return result, 200, security_headers()
