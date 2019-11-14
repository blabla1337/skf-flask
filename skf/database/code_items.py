
from skf.database import db

'''
--
-- Table structure for table `code_items`
--
drop table if exists `code_items`;
CREATE TABLE `code_items` (
`code_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL,
`code_lang` varchar(250) NOT NULL
);
'''

class CodeItem(db.Model):

    __tablename__ = 'code_items'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    code_lang = db.Column(db.Text, nullable=False)

    def __init__(self, content, title, lang):
    	self.content = content
    	self.title = title
    	self.code_lang = lang
