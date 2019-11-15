from skf.database import db

'''
--
-- Table structure for table `checklists_results`
--
drop table if exists `checklists_results`;
CREATE TABLE `checklists_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_id` varchar(255) NOT NULL,
`project_id` int(11) NOT NULL,
`sprint_id` int(11) NOT NULL,
`status` int(11) NOT NULL,
`kb_id` int(11)
);
'''

class ChecklistResult(db.Model):
    
    __tablename__ = 'checklists_results'

    id = db.Column(db.Integer, primary_key=True)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklists_kb.id'), nullable=True)
    checklist_item = db.relationship("ChecklistKB", backref=db.backref(''))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
    project = db.relationship("Project", backref=db.backref(''))
    sprint_id = db.Column(db.Integer, db.ForeignKey('project_sprints.sprint_id'), nullable=True)
    sprint = db.relationship("ProjectSprint", backref=db.backref(''))
    status = db.Column(db.Integer, nullable=True)
    kb_id = db.Column(db.Integer, db.ForeignKey("kb_items.kb_id"), nullable=True)
    kb_items = db.relationship("KBItem", backref=db.backref(''))  
    checklist_type_id = db.Column(db.Integer, db.ForeignKey("checklist_types.id"))
    checklist_type = db.relationship('ChecklistType', backref=db.backref(""))

    def __init__(self, status):
        self.status = status

