from skf.database import db

class Project(db.Model):
    
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    '''
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id], backref=db.backref('projects'))

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship("User", foreign_keys=[owner_id], backref=db.backref('owned_projects'))

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    group = db.relationship("Group", backref=db.backref('projects', uselist=False))
    '''
    
    name = db.Column(db.Text, nullable=False)
    version = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    timestamp = db.Column(db.Text, nullable=False)


    def __init__(self, name, version, description, timestamp):
        self.name = name
        self.version = version
        self.description = description
        self.timestamp = timestamp


