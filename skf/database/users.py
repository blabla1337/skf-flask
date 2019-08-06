
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
    userName = db.Column(db.String(255), nullable=True, unique=True)
    password = db.Column(db.Text, nullable=True)
    access = db.Column(db.Boolean, nullable=False)
    activated = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(255), unique=True)
    groups = db.relationship('Group', back_populates='members')
    #group = db.relationship('GroupMember', back_populates='member')


    def __init__(self, email, accessToken='', userName='', password='', access=False, activated=False):
        self.accessToken = accessToken
        self.userName = userName
        self.password = password
        self.access = access
        self.activated = activated
        self.email = email

    def __repr__(self):
        return "<User> {}| {} activated:{} access:{} email:{}>)".format(
           self.id, self.userName, self.activated, self.access, self.email)

Authorization token: for user with ID 2 : 57152349
riccardo@zerocopter.com

Authorization token: for user with ID 3 : 23106284
aa@zerocopter.com