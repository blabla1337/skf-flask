
from skf.database import db


class checklists_kb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_pre_ID = db.Column(db.Integer)
    question_sprint_ID = db.Column(db.Integer)
    codeID_php = db.Column(db.Integer)
    codeID_asp = db.Column(db.Integer)
    codeID_java = db.Column(db.Integer)
    codeID_python = db.Column(db.Integer)
    include_always = db.Column(db.Boolean)
    include_first = db.Column(db.Boolean)
    checklistID = db.Column(db.Integer, db.ForeignKey("checklists.checklistID"))
    checklist_items = db.relationship("checklists", foreign_keys=[checklistID])
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])


    def __init__(self, checklistID, question_pre_ID, question_sprint_ID, kbID, codeID_php, codeID_asp, codeID_java, codeID_python, include_always, include_first, kb_items, checklist_items):
        self.checklistID = checklistID
        self.question_pre_ID = question_pre_ID
        self.question_sprint_ID = question_sprint_ID
        self.codeID_php = codeID_php
        self.codeID_asp = codeID_asp
        self.codeID_java = codeID_java
        self.codeID_python = codeID_python
        self.kb_items = kb_items
        self.include_always = include_always
        self.include_first = include_first
        self.checklist_items = checklist_items

