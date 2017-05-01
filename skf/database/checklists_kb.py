
from skf.database import db


class checklists_kb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionID = db.Column(db.Integer)
    codeID_php = db.Column(db.Integer)
    codeID_asp = db.Column(db.Integer)
    codeID_java = db.Column(db.Integer)
    codeID_python = db.Column(db.Integer)
    checklistID = db.Column(db.Integer, db.ForeignKey("checklists.checklistID"))
    checklist_items = db.relationship("checklists", foreign_keys=[checklistID])
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])


    def __init__(self, checklistID, questionID, kbID, testguideID, cweID, nistID, codeID_php, codeID_asp, codeID_java, codeID_python, kb_items, checklist_items):
        self.checklistID = checklistID
        self.questionID = questionID
        self.codeID_php = codeID_php
        self.codeID_asp = codeID_asp
        self.codeID_java = codeID_java
        self.codeID_python = codeID_python
        self.kb_items = kb_items
        self.checklist_items = checklist_items

