
from skf.database import db
from skf.database.groupmembers import GroupMember

class Group(db.Model):

    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref("owned_groups"), uselist=False)
    groupName = db.Column(db.String(255), nullable=False)
    members = db.relationship('User', secondary=GroupMember, back_populates='groups')
    timestamp = db.Column(db.Text)

    def __init__(self, groupName, timestamp):
    	self.groupName = groupName
    	self.timestamp = timestamp

