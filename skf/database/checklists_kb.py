
from skf.database import db


class checklists_kb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_ID = db.Column(db.Integer)
    question_ID = db.Column(db.Integer)
    include_always = db.Column(db.String)
    checklistID = db.Column(db.String)
    content = db.Column(db.String)
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])
    checklist_type = db.Column(db.Integer)
    cwe = db.Column(db.Integer)

    def __init__(self, checklistID, content, kbID, checklist_type, include_always, question_ID, cwe):
        self.question_ID = question_ID
        self.include_always = include_always
        self.checklistID = checklistID
        self.checklist_type = checklist_type
        self.content = content
        self.kbID = kbID
        self.cwe = cwe        
