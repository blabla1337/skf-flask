
from skf.database import db


class checklists_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklistID = db.Column(db.Integer)
    projectID = db.Column(db.Integer)
    sprintID = db.Column(db.Integer)
    status = db.Column(db.Integer)
    checklistID = db.Column(db.String, db.ForeignKey("checklists.checklistID"))
    checklist_items = db.relationship("checklists", foreign_keys=[checklistID])
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])  
    

    def __init__(self, checklistID, projectID, sprintID, status, kbID):
        self.checklistID = checklistID
        self.projectID = projectID
        self.sprintID = sprintID
        self.status = status
        self.kbID = kbID

