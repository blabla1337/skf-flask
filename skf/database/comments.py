
from skf.database import db 


class comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    sprintID = db.Column(db.Integer)
    checklistID = db.Column(db.Integer)
    userID = db.Column(db.Integer)
    status = db.Column(db.Integer)
    comment = db.Column(db.Text)


    def __init__(self, projectID, sprintID, checklistID, userID, status, comment):
        self.projectID = projectID
        self.sprintID = sprintID
        self.checklistID = checklistID
        self.userID = userID
        self.status = status
        self.comment = comment