from skf.database import db


class chatbot_log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)

    def __init__(self, question):
        self.question = question
