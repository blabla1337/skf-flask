
from skf.database import db

'''
--
-- Table structure for table `questions`
--
drop table if exists `questions`;
CREATE TABLE `questions` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);
'''

class Question(db.Model):
	
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    checklist_type = db.Column(db.Integer, nullable=False)

    def __init__(self, question, checklist_type):
        self.question = question
        self.checklist_type = checklist_type
