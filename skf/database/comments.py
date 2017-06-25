
from skf.database import db 


class comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sprintID = db.Column(db.Integer)
    checklistID = db.Column(db.Integer)
    userID = db.Column(db.Integer)
    status = db.Column(db.Integer)
    comment = db.Column(db.Text)
    date = db.Column(db.Integer)
    userID = db.Column(db.String, db.ForeignKey("users.userID"))
    user_items = db.relationship("users", foreign_keys=[userID])

    def __init__(self, sprintID, checklistID, userID, status, comment, date):
        self.sprintID = sprintID
        self.checklistID = checklistID
        self.userID = userID
        self.status = status
        self.comment = comment
        self.date = date