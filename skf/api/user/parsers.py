from flask_restplus import reqparse

user_activation_arguments = reqparse.RequestParser()
user_activation_arguments.add_argument('accessToken', type=str, required=True, default='1234', help='Authentication token that was generated')
user_activation_arguments.add_argument('email', type=str, required=True, default='example@owasp.org', help='Email of the user')
user_activation_arguments.add_argument('password', type=str, required=True, help='Password of the user')
user_activation_arguments.add_argument('repassword', type=str, required=True, help='Retyped password')
