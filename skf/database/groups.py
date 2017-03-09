
from skf.database import db


class groups(db.Model):
    groupID = db.Column(db.Integer, primary_key=True)
    ownerID = db.Column(db.Integer)
    groupName = db.Column(db.Text)
    timestamp = db.Column(db.Text)

    def __init__(self, groupID, ownerID, groupName, timestamp):
        self.groupID = groupID
        self.ownerID = ownerID
        self.groupName = groupName
        self.timestamp = timestamp

    def __repr__(self):
        return '<groups %r>' % self.groupID
