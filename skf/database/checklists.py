
from skf.database import db 


class checklists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checklistID = db.Column(db.Text)
    content = db.Column(db.Text)
    level = db.Column(db.Integer)


    def __init__(self, checklistID, content, level):
        self.checklistID = checklistID
        self.content = content
        self.level = level

 