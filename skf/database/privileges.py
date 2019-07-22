
from skf.database import db

'''
drop table if exists `privileges`;
CREATE TABLE `privileges` (
`privilegeID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilege` varchar(255) NOT NULL
);
'''

class Privilege(db.Model):

    __tablename__ = 'privileges'

    id = db.Column(db.Integer, primary_key=True)
    
    privilege = db.Column(db.String(255), nullable=False)

    def __init__(self, privilege):
        self.privilege = privilege


