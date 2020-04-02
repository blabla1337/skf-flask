from skf.database import db

class Question(db.Model):
	
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    checklist_type = db.Column(db.Integer, nullable=False)

    def __init__(self, question, checklist_type):
        self.question = question
        self.checklist_type = checklist_type
