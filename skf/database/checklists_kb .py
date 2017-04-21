
from skf.database import db


class checklists_kb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklistID = db.Column(db.Integer)
    questionID = db.Column(db.Integer)
    kbID = db.Column(db.Integer)
    codeID_php = db.Column(db.Integer)
    codeID_asp = db.Column(db.Integer)
    codeID_java = db.Column(db.Integer)
    codeID_python = db.Column(db.Integer)

    def __init__(self, checklistID, questionID, kbID, codeID_php, codeID_asp, codeID_java, codeID_python):
        self.checklistID = checklistID
        self.questionID = questionID
        self.kbID = kbID
        self.codeID_php = codeID_php
        self.codeID_asp = codeID_asp
        self.codeID_java = codeID_java
        self.codeID_python = codeID_python

    def __repr__(self):
        return '<checklists_kb %r>' % self.id
