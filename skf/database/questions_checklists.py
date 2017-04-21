
from skf.database import db


class questions_checklists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer)
    checklistID = db.Column(db.Integer)
    level = db.Column(db.Integer)

    def __init__(self, questionID, checklistID, level):
        self.questionID = questionID
        self.checklistID = checklistID
        self.level = level

    def __repr__(self):
        return '<questions_checklists %r>' % self.id
