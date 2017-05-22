
from skf.database import db


class question_sprint_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    question_sprint_ID = db.Column(db.Integer)
    result = db.Column(db.Text)


    def __init__(self, projectID, question_sprint_ID, result):
        self.projectID = projectID
        self.question_sprint_ID = question_sprint_ID
        self.result = result
