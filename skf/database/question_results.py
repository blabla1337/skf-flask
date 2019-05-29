
from skf.database import db


class question_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    sprintID = db.Column(db.Integer)
    question_ID = db.Column(db.Integer)
    result = db.Column(db.Text)
    checklist_type = db.Column(db.Integer)


    def __init__(self, projectID, sprintID, question_ID, result, checklist_type):
        self.projectID = projectID
        self.sprintID = sprintID
        self.question_ID = question_ID
        self.result = result
        self.checklist_type = checklist_type
