
from skf.database import db


class groupmembers(db.Model):
    memberID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    groupID = db.Column(db.Integer)
    ownerID = db.Column(db.Integer)
    timestamp = db.Column(db.Text)
