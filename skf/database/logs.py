
from skf.database import db


class logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    time = db.Column(db.Integer)
    threat = db.Column(db.Text)
    ip = db.Column(db.Text)
    userID = db.Column(db.Text)
    message = db.Column(db.Text)
    status = db.Column(db.Text)

    def __init__(self, date, time, threat, ip, userID, message, status):
        self.date = date
        self.time = time
        self.threat = threat
        self.ip = ip
        self.userID = userID
        self.message = message
        self.status = status

    def __repr__(self):
        return '<logs %r>' % self.id
