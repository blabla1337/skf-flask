
from skf.database import db


class questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)


    def __init__(self, question):
        self.question = question


