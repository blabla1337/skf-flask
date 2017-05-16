
from flask import request
from flask_restplus import Resource
from skf.api.security import log, security_headers, validate_privilege, val_num, val_alpha_num
from skf.api.checklist.serializers import checklist, level, message
from skf.api.checklist.parsers import authorization, id_arguments, pagination_arguments
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
        categories = checklists_kb.query.order_by(asc(checklists_kb.checklistID)).all()
        log("User requested list of checklist items", "LOW", "PASS")
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
            log("User requested specific checklist item", "LOW", "PASS")
            return checklists_kb.query.filter(checklists_kb.checklistID == id).one(), 200, security_headers()
        except:
            log("User triggered error requesting specific checklist item", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()
            

@ns.route('/level')
class ChecklistItem(Resource):

    @api.expect(level)
    @api.marshal_with(checklist)
    @api.response(400, 'Validation Error', message)
    def post(self):
        """
        Returns list of checklist items based on level.
        Privileges required: none
        """
        data = request.json
        lvl = data.get('level')
        try:
            log("User requested list of checklist items based on level", "LOW", "PASS")
            categories_levels = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = lvl)).all()        
            return categories_levels, 200, security_headers()
        except:
            log("User triggered error requesting specific checklist items based on level", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()