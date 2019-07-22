
from skf.database import db 

'''
--
-- Table structure for table `comments`
--
drop table if exists `comments`;
CREATE TABLE `comments` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`sprintID` int(11) NOT NULL,
`checklistID` varchar(255) NOT NULL,
`userID` int(11) NOT NULL, 
`status` int(11) NOT NULL,  
`comment` varchar(255),
`date` varchar(255) NOT NULL
);
'''

class Comment(db.Model):
    
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    sprint_id = db.Column(db.Integer, db.ForeignKey('project_sprints.id'), nullable=False)
    sprint = db.relationship('ProjectSprint', backref=db.backref('comments'))

    checklist_id = db.Column(db.Integer, db.ForeignKey("checklists_kb.id"), nullable=False)
    checklist = db.relationship('ChecklistKB', backref=db.backref('commments'))

    status = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    date = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", backref=db.backref("comments"))

    def __init__(self, status, comment, date):
        self.status = status
        self.comment = comment
        self.date = date