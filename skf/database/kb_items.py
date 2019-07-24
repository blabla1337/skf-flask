
from skf.database import db

'''
--
-- Table structure for table `kb_items`
--
drop table if exists `kb_items`;
CREATE TABLE `kb_items` (
`kbID` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL
);
'''

class KBItem(db.Model):
	
    __tablename__ = 'kb_items'
    
    id = db.Column(db.Integer, primary_key=True)
    kb_id = db.Column(db.Integer) #, unique=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    
    def __init__(self, title, content, kb_id=''):
        self.kb_id = kb_id
        self.title = title
        self.content = content