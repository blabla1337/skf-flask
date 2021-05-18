
from skf.database import db

class LabItemCode(db.Model):
	
    __tablename__ = 'lab_items_code'

    id = db.Column(db.Integer, primary_key=True)
    code_example = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Integer, nullable=False)
    code_type = db.Column(db.Text, nullable=False)
    hint = db.Column(db.Text, nullable=False)
    code_type = db.Column(db.Text, nullable=False)

    def __init__(self, code_example, solution, code_type):
        self.code_example = code_example
        self.solution = solution
        self.code_type = code_type

