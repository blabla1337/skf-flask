from skf.database import db
#from skf.database.projects import projectmembers

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    privilege_id = db.Column(db.Integer, db.ForeignKey('privileges.id'), nullable=False)
    privilege = db.relationship("Privilege", backref=db.backref('users'))
    accessToken = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=True, unique=True)
    password = db.Column(db.Text, nullable=True)
    access = db.Column(db.Boolean, nullable=False)
    activated = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    groups = db.relationship('Group', back_populates='members')
    #group = db.relationship('GroupMember', back_populates='member')

    def __init__(self, email, accessToken='', username='', password='', access=False, activated=False):
        self.accessToken = accessToken
        self.username = username
        self.password = password
        self.access = access
        self.activated = activated
        self.email = email

    def __repr__(self):
        return "<User> {}| {} activated:{} access:{} email:{}>)".format(
           self.id, self.username, self.activated, self.access, self.email)
