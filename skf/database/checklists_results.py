
from skf.database import db


class checklists_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklistID = db.Column(db.Integer)
    projectID = db.Column(db.Integer)
    sprintID = db.Column(db.Integer)
    status = db.Column(db.Integer)
    comment = db.Column(db.Text)
    preItem = db.Column(db.Integer)
    

    def __init__(self, checklistID, projectID, sprintID, status, comment, preItem):
        self.checklistID = checklistID
        self.projectID = projectID
        self.sprintID = sprintID
        self.status = status
        self.comment = comment
        self.preItem = preItem

