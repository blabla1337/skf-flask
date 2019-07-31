
from skf.database import db

'''
--
-- Table structure for table `project_sprints`
--
drop table if exists `project_sprints`;
CREATE TABLE `project_sprints` (
`sprintID` INTEGER PRIMARY KEY AUTOINCREMENT,
`projectID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`sprintName` varchar(250) NOT NULL,
`sprintDesc` varchar(250) NOT NULL
);
'''

class ProjectSprint(db.Model):
    
    __tablename__ = "project_sprints"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship('Group', backref=db.backref("sprints"))

    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship('Project', backref=db.backref("sprints"))


    def __init__(self, sprintName, sprintDesc):
        self.name = name
        self.description = description
 