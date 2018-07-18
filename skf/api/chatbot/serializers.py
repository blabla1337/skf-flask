from flask_restplus import fields
from skf.api.restplus import api


question_chatbot = api.model('question_chatbot', {
    'question': fields.String(required=True, description='The question for the chatbot to answer'),
    'question_option': fields.Integer(required=False, description='The extra option if chatbot didnt have direct hit'),
    'question_lang': fields.String(required=False, description='The extra option if chatbot didnt have code lang hit'),
    
})

question_answer = api.model('question_answer', {
    'answer': fields.String(required=True, description='The answer from the chatbot'),
    'answer_options': fields.Integer(required=False, description='The extra option if chatbot didnt have direct hit'),
    'answer_lang': fields.String(required=False, description='The extra option if chatbot didnt have code lang hit'),
    
})

question_response = api.inherit('List of option items', {
    'options': fields.List(fields.Nested(question_answer))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
