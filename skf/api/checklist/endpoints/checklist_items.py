
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num, val_alpha_num
from skf.api.checklist.serializers import checklist, message
from skf.api.checklist.parsers import authorization, id_arguments
from skf.api.restplus import api
from skf.database.checklists_kb import checklists_kb
from skf.database.checklists import checklists

ns = api.namespace('checklist/items', description='Operations related to checklist items')


@ns.route('/')
class ChecklistCollection(Resource):

    @api.expect()
    @api.marshal_with(checklist)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of checklist items.
        Privileges required: none
        """
        categories = checklists_kb.query.all()
        log("User requested list of checklist items", "LOW", "PASS", self)
        return categories, 200, security_headers()


@ns.route('/<float:id>')
class ChecklistItem(Resource):

    @api.expect(id_arguments)
    @api.marshal_with(checklist)
    @api.response(400, 'Validation Error', message)
    def get(self, id):
        """
        Returns a checklist item.
        Privileges required: none
        """
        try:
            log("User requested specific checklist item", "LOW", "PASS", self)
            return checklists_kb.query.filter(checklists_kb.checklistID == id).one(), 200, security_headers()
        except:
            log("User triggered error requesting specific checklist item", "LOW", "FAIL", self)
            return {'message': 'Validation error'}, 400, security_headers()
            