from skf.database import db

GroupMember = db.Table('groupmembers',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')))
