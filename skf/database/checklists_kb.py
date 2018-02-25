
from skf.database import db
from skf.database.checklists import checklists


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
    checklistID = db.Column(db.String, db.ForeignKey("checklists.checklistID"))
    checklist_items = db.relationship("checklists",
        primaryjoin="and_(checklists_kb.checklistID==checklists.checklistID,"
            "checklists_kb.kbID==checklists.kbID)")
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])
