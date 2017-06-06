
from skf.database import db


class privileges(db.Model):
    privilegeID = db.Column(db.Integer, primary_key=True)
    privilege = db.Column(db.Text)
