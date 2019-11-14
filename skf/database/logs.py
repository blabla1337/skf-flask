
from skf.database import db

'''
--
-- Table structure for table `logs`
--
drop table if exists `logs`;
CREATE TABLE `logs` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`date` varchar(255) NOT NULL,
`time` varchar(255) NOT NULL,
`threat` varchar(255) NOT NULL,
`ip` varchar(255) NOT NULL,
`user_id` varchar(255) NOT NULL,
`status` varchar(255) NOT NULL,
`message` varchar(255) NOT NULL
);
'''

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

    def __init__(self, date, time, threat, ip, message, status):
        self.date = date
        self.time = time
        self.threat = threat
        self.ip = ip
        self.message = message
        self.status = status

