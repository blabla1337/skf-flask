
from skf.database import db

'''
--
-- Table structure for table `chatbot_log`
--
drop table if exists `chatbot_log`;
CREATE TABLE `chatbot_log` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`question` varchar(255)
); 
'''

class ChatbotLog(db.Model):
	
    __tablename__ = 'chatbot_log'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)

    def __init__(self, question):
        self.question = question
