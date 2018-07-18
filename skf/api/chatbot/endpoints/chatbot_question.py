from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.chatbot.business import answer
from skf.api.chatbot.serializers import question_response, question_chatbot, message
from skf.api.restplus import api

ns = api.namespace('chatbot', description='Operations related to the chatbot interactions')


@ns.route('/question')
@api.response(404, 'Validation error', message)
class ChatbotQuestion(Resource):

    @api.expect(question_chatbot)
    @api.marshal_with(question_response)
    @api.response(400, 'No results found', message)
    def post(self):
        """
        Returns a answer on a question.
        * Privileges required: **none**
        """
        data = request.json
        data_q=data.get('question')
        #3intent_r=data.get('intent')
        
        #if intent_r is None:
         #     result1,intent_r = answer(data_q,None)
        #else:
        result1 = answer(data_q)              
        
        if type(result1)!=str:
              result={}
              result["options"] = [{"answer": result1[i],"answer_options": i,"answer_intent":None} for i in result1]
              return result, 200, security_headers()   
        else:
              result={ "options": [{"answer": result1 ,"answer_options": 0,"answer_intent":None}] }
              return result, 200, security_headers()

