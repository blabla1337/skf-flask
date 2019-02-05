
from skf.database import db


class questions_pre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
