
from flask import request
from flask_restplus import Resource
from sqlalchemy.orm.exc import NoResultFound
from skf.api.security import log, security_headers
from skf.api.checklist.serializers import checklist, message
from skf.api.restplus import api
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/items')
class ChecklistCollection(Resource):

    @api.expect()
    @api.marshal_with(checklist)
    @api.response(400, 'Validation Error', message)
    def get(self):
        """
        Returns list of checklist items.
        Privileges required: none
        """
        try:
            log("User requested list of checklist items", "LOW", "PASS")
            categories = checklists_kb.query.all()
            return categories, 200, security_headers()
        except NoResultFound:
            print("No results")
            # Deal with that as well
        except:
            log("User triggered error requesting list of checklist items", "LOW", "FAIL")
            return {'message': 'Validation error'}, 400, security_headers()

