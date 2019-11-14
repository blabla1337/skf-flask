

from skf.database import db

'''
class GroupMember(db.Model):

    __tablename__ = 'groupmembers'

    #id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    user = db.relationship('User', back_populates="members", foreign_keys=[user_id])

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    group = db.relationship('Group', back_populates="groups", foreign_keys=[group_id])

    #owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #owner = db.relationship('User', back_populates="group", foreign_keys=[owner_id])

    timestamp = db.Column(db.Text)


    #def __init__(self, memberID, user_id, group_id, owner_id, timestamp):
    #    self.member_id = memberID
    #    self.user_id = user_id
    #    self.group_id = group_id
    #    self.owner_id = owner_id
    #    self.timestamp = timestamp
'''

# TODO: Implement association pattern to include timestamp and owner

GroupMember = db.Table('groupmembers',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')))
