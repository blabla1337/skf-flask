
from skf.database import db

'''
--
-- Table structure for table `checklist_types`
--
drop table if exists `checklist_types`;
CREATE TABLE `checklist_types` (
`checklist_type` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_description` varchar(255) NOT NULL,
`checklist_name` varchar(255) NOT NULL
);
'''

class ChecklistType(db.Model):
	
    __tablename__ = 'checklist_types'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

