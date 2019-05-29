
from skf.database import db


class projects(db.Model):
    projectID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    groupID = db.Column(db.Integer)
    projectName = db.Column(db.Text)
    projectVersion = db.Column(db.Text)
    projectDesc = db.Column(db.Text)
    ownerID = db.Column(db.Integer)
    timestamp = db.Column(db.Text)


    def __init__(self, userID, groupID, projectName, projectVersion, projectDesc, ownerID, timestamp):
        self.userID = userID
        self.groupID = groupID
        self.projectName = projectName
        self.projectVersion = projectVersion
        self.projectDesc = projectDesc
        self.ownerID = ownerID
        self.timestamp = timestamp


