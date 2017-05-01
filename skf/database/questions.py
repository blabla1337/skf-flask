
from skf.database import db


class questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    include_always = db.Column(db.Integer)
    include_first = db.Column(db.Integer)

    def __init__(self, question, include_always, include_first):
        self.question = question
        self.include_always = include_always
        self.include_first = include_first

