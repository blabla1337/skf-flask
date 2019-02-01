
from skf.database import db


class questions_pre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    checklist_type = db.Column(db.Integer)

    def __init__(self, question, checklist_type):
        self.question = question
        self.checklist_type = checklist_type
