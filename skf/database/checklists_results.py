
from skf.database import db

'''
--
-- Table structure for table `checklists_results`
--
drop table if exists `checklists_results`;
CREATE TABLE `checklists_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255) NOT NULL,
`projectID` int(11) NOT NULL,
`sprintID` int(11) NOT NULL,
`status` int(11) NOT NULL,
`kbID` int(11)
);
'''

class ChecklistResult(db.Model):
    
    __tablename__ = 'checklist_results'

    id = db.Column(db.Integer, primary_key=True)

    checklist_id = db.Column(db.Integer, db.ForeignKey('checklists_kb.id'), nullable=False)
    checklist_items = db.relationship("ChecklistKB", backref=db.backref('checklist_results'))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = db.relationship("Project", backref=db.backref('checklist_results'))

    sprint_id = db.Column(db.Integer, db.ForeignKey('project_sprints.id'), nullable=False)
    sprint = db.relationship("ProjectSprint", backref=db.backref('checklist_results'))

    status = db.Column(db.Integer, nullable=False)
    
    kb_id = db.Column(db.Integer, db.ForeignKey("kb_items.id"))
    kb_items = db.relationship("KBItem", backref=db.backref('checklist_results'))  
    

    def __init__(self, status):
        self.status = status

