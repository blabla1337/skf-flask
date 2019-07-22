
from skf.database import db
#from skf.database.projects import projectmembers

'''
drop table if exists `users`;
CREATE TABLE `users` (
`userID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilegeID` int(11) NOT NULL,
`userName` varchar(255) NOT NULL UNIQUE,
`email` varchar(255) NOT NULL UNIQUE,
`password` varchar(255) NOT NULL,
`accessToken` int(11) NOT NULL UNIQUE,
`activated` varchar(255),
`access` varchar(255) NOT NULL
);
'''

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    privilege_id = db.Column(db.Integer, db.ForeignKey('privileges.id'), nullable=False)
    privilege = db.relationship("Privilege", backref=db.backref('users'))
    
    accessToken = db.Column(db.Integer, unique=True, nullable=False)
    userName = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    access = db.Column(db.Boolean, nullable=False)
    activated = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(255), unique=True)
    groups = db.relationship('Group', back_populates='members')
    #group = db.relationship('GroupMember', back_populates='member')


    def __init__(self, accessToken, userName, email, password='', access=False, activated=False):
        self.accessToken = accessToken
        self.userName = userName
        self.password = password
        self.access = access
        self.activated = activated
        self.email = email
