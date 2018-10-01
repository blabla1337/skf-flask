
from skf.database import db


class checklist_types(db.Model):
    checklist_type = db.Column(db.Integer, primary_key=True)
    checklist_name = db.Column(db.Text)

    def __init__(self, checklist_name):
        self.checklist_name = checklist_name
        
