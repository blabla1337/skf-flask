
from skf.database import db


class users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    privilegeID = db.Column(db.Integer)
    accessToken = db.Column(db.Integer)
    userName = db.Column(db.Text)
    password = db.Column(db.Text)
    access = db.Column(db.Text)
    activated = db.Column(db.Text)
    email = db.Column(db.Text)


    def __init__(self, privilegeID, accessToken, userName, password, access, activated, email):
        self.privilegeID = privilegeID
        self.accessToken = accessToken
        self.userName = userName
        self.password = password
        self.access = access
        self.activated = activated
        self.email = email
