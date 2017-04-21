
from skf.database import db


class checklists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklistID = db.Column(db.Integer)
    content = db.Column(db.Text)
    level = db.Column(db.Integer)
    testguideID = db.Column(db.Integer)
    cweID = db.Column(db.Integer)
    nistID = db.Column(db.Integer)

    def __init__(self, checklistID, content, level, testguideID, cweID, nistID):
        self.checklistID = checklistID
        self.content = content
        self.level = level
        self.testguideID = testguideID
        self.userID = userID
        self.cweID = cweID
        self.nistID = nistID

    def __repr__(self):
        return '<checklists %r>' % self.id
