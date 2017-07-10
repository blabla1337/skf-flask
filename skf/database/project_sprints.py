
from skf.database import db


class project_sprints(db.Model):
    sprintID = db.Column(db.Integer, primary_key=True)
    sprintName = db.Column(db.Text)
    sprintDesc = db.Column(db.Text)
    groupID = db.Column(db.Integer)
    projectID = db.Column(db.Integer)


    def __init__(self, sprintName, sprintDesc, groupID, projectID):
        self.sprintName = sprintName
        self.sprintDesc = sprintDesc
        self.groupID = groupID
        self.projectID = projectID
 