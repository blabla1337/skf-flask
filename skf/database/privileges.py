from skf.database import db

class Privilege(db.Model):

    __tablename__ = 'privileges'
    
    id = db.Column(db.Integer, primary_key=True)
    privilege = db.Column(db.String(255), nullable=False)

    def __init__(self, privilege):
        self.privilege = privilege

    def __repr__(self):
    	return self.privilege


