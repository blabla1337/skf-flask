from skf.database import db


class Log(db.Model):
    
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer,nullable=False)
    threat = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship('User', backref=db.backref("logs"))
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)

    def __init__(self, date, time, threat, ip, message, status, user_id):
        self.date = date
        self.time = time
        self.threat = threat
        self.ip = ip
        self.message = message
        self.status = status
        self.user_id = user_id

