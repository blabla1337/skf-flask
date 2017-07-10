
from skf.database import db


class question_pre_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    question_pre_ID = db.Column(db.Integer)
    result = db.Column(db.Text)


    def __init__(self, projectID, question_pre_ID, result):
        self.projectID = projectID
        self.question_pre_ID = question_pre_ID
        self.result = result
