from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('bool', type=bool, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[1, 5, 10, 20, 30, 40, 50, 100, 500],
                                  default=500, help='Results per page {error_msg}')

authorization = reqparse.RequestParser()
authorization.add_argument('Authorization', location='headers', required=True, help='Authorization JWT token')

id_arguments = reqparse.RequestParser()

code_lang_arguments = reqparse.RequestParser()
code_lang_arguments.add_argument('code_lang', type=str, required=True, choices=["php", "asp", "java", "python"],
                                  default='php', help='Code language selection')