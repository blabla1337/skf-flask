from flask_restplus import Resource
from skf.api.training.business import get_training_profiles
from skf.api.restplus import api
from skf.api.security import *

ns = api.namespace('training', description='Operations related to training items')

@ns.route('/items')
class TrainingProfileCollection(Resource):

    @api.response(400, 'No results found')
    def get(self):
        result = get_training_profiles()
        return result, 200, security_headers()
