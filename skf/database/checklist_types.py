
from skf.database import db


class checklist_types(db.Model):
    checklist_type = db.Column(db.Integer, primary_key=True)
    checklist_name = db.Column(db.Text)
    checklist_description = db.Column(db.Text)

    def __init__(self, checklist_name, checklist_description):
        self.checklist_name = checklist_name
        self.checklist_description = checklist_description

