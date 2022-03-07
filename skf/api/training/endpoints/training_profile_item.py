from flask_restplus import Resource
from skf.api.training.business import get_training_profile_item
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/item/<string:id>')
@ns.doc(params={'id': 'The profile'})
class TrainingProfileCollection(Resource):

    @api.response(400, 'No results found')
    def get(self, id):
        val_alpha_num(id)
        result = get_training_profile_item(id)
        return result, 200, security_headers()
