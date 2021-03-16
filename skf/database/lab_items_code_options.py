
from skf.database import db

class LabItemCodeOptions(db.Model):
	
    __tablename__ = 'lab_items_code_options'

    id = db.Column(db.Integer, primary_key=True)
    vuln = db.Column(db.Text, nullable=False)

    def __init__(self, vuln):
        self.vuln = vuln

