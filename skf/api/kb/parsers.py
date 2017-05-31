from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()

authorization = reqparse.RequestParser()
authorization.add_argument('Authorization', location='headers', required=True, help='Authorization JWT token')

id_arguments = reqparse.RequestParser()