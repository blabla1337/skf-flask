
from skf.database import db


class questions_sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
