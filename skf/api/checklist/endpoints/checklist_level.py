
from flask import request
from flask_restplus import Resource
from sqlalchemy.orm.exc import NoResultFound
from skf.api.security import log, security_headers
from skf.api.checklist.serializers import checklist, level, message
from skf.api.restplus import api
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/level')
class ChecklistItem(Resource):

    @api.expect(level)
    @api.marshal_list_with(checklist)
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
            categories_levels = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = lvl)).group_by(checklists_kb.checklistID).all()
            return categories_levels, 200, security_headers()
        except NoResultFound:
            log("User triggered empty result set requesting specific checklist items based on level", "LOW", "INFO")
        except:
            log("User triggered error requesting specific checklist items based on level", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()
                
