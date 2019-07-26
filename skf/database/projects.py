from skf.database import db

'''
--
-- Table structure for table `projects`
--
drop table if exists `projects`;
CREATE TABLE `projects` (
`projectID` INTEGER PRIMARY KEY AUTOINCREMENT,
`userID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`projectName` varchar(250) NOT NULL,
`projectVersion` varchar(250) NOT NULL,
`projectDesc` text NOT NULL,
`ownerID` int(11) NOT NULL,
`timestamp` timestamp NOT NULL
);
'''

class Project(db.Model):
    
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    '''
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id], backref=db.backref('projects'))

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship("User", foreign_keys=[owner_id], backref=db.backref('owned_projects'))

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    group = db.relationship("Group", backref=db.backref('projects', uselist=False))
    '''
    
    projectName = db.Column(db.Text, nullable=False)
    projectVersion = db.Column(db.Text, nullable=False)
    projectDesc = db.Column(db.Text, nullable=False)

    timestamp = db.Column(db.Text, nullable=False)


    def __init__(self, projectName, projectVersion, projectDesc, timestamp):
        self.projectName = projectName
        self.projectVersion = projectVersion
        self.projectDesc = projectDesc
        self.timestamp = timestamp


