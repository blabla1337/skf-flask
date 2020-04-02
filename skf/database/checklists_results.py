from skf.database import db

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
    evidence = db.Column(db.Text, nullable=True)
    resolved = db.Column(db.Boolean, nullable=True)

    def __init__(self, status, evidence, resolved):
        self.status = status
        self.evidence = evidence
        self.resolved = resolved
