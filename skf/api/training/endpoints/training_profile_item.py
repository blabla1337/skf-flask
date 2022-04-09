from flask_restplus import Resource
from skf.api.training.business import get_training_profile_item
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/profile/<string:profile_id>')
@ns.doc(params={'profile_id': 'The profile id'})
class TrainingProfile(Resource):

    @api.response(400, 'No results found')
    def get(self, profile_id):
        val_alpha_num_special(profile_id)
        result = get_training_profile_item(profile_id)
        return result, 200, security_headers()
