from flask_restplus import fields
from skf.api.restplus import api

labs_code = api.model('labs', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a code Lab'),
    'code_example': fields.String(required=True, description='Code lab example to be validated'),
    'solution': fields.Integer(required=True, description='The correct solution based on integer'),
    'code_type': fields.String(required=True, description='The coding type for example, php, asp, java'),
    'hint': fields.String(required=True, description='The hint/solution of the example'),
})

lab_items_code = api.inherit('List of code lab items', {
    'items': fields.List(fields.Nested(labs_code))
})

labs_code_solutions = api.model('labs', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a code Lab Vulnerability'),
    'vuln': fields.String(required=True, description='Code lab solution for vulnerability'),
})

lab_items_solutions = api.inherit('List of code lab solutions items', {
    'items': fields.List(fields.Nested(labs_code_solutions))
})

labs_code_status = api.model('labs', {
    'status': fields.String(required=True, description='Code lab solution status for vulnerability'),
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})

