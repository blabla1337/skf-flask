
from skf.database import db


class questions_pre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    checklist_type = db.Column(db.Text)
    checklist_level = db.Column(db.Text)

    def __init__(self, question, checklist_type, checklist_level):
        self.question = question
        self.checklist_type = checklist_type
        self.checklist_level = checklist_level