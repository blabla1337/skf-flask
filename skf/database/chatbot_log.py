
from skf.database import db

class ChatbotLog(db.Model):
	
    __tablename__ = 'chatbot_log'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)

    def __init__(self, question):
        self.question = question
