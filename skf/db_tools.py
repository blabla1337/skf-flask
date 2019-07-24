import os
import datetime
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from shutil import copyfile
from skf.database import db
#from skf.database.kb_items import KBItem
from skf.database.users import User
from skf.database.groups import Group
from skf.database.privileges import Privilege
from skf.database.kb_items import KBItem
from skf.database.code_items import CodeItem
from skf.database.checklist_types import ChecklistType

#from sqlite3 import dbapi2 as sqlite3

def connect_db():
    """Connects to the specific database."""
    #rv = sqlite3.connect(os.path.join(app.root_path, settings.DATABASE))
    #rv.row_factory = sqlite3.Row
    #return rv
    return True

def load_initial_data():

#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (1, "edit:read:manage:delete");
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (2, "edit:read:delete");
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (3, "edit:read");
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (4, "read");
    try:
        p = Privilege('edit:read:manage:delete')
        db.session.add(p)
        db.session.add(Privilege('edit:read:delete'))
        db.session.add(Privilege('edit:read'))
        db.session.add(Privilege('read'))  

#   INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "False", "False", "example@owasp.org");
        user = User(userName='admin', accessToken=1234, email="example@owasp.org")
        user.privilege = p
        db.session.add(user)

#   INSERT OR REPLACE INTO `groups` (`groupID`, `ownerID`, `groupName`) VALUES (1, 1, "privateGroup");
        group = Group('privateGroup', datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
#   INSERT OR REPLACE INTO `groupMembers` (`memberID`, `userID`, `groupID`, `ownerID`) VALUES (1, 1, 1, 1);
        group.members.append(user)
        group.owner = user
        db.session.add(group)

#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 1", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.");
#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 2", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.");
        db.session.add(ChecklistType(name='ASVS LEVEL 1', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))
        db.session.add(ChecklistType(name='ASVS LEVEL 2', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def load_test_data():
    try:

        for i in range(1, 5):
            db.session.add(KBItem("test title kb item {}".format(i), "test content kb item {}".format(i)))
            db.session.commit()

        for lang in ["php", "asp"]:
            for i in [1, 2]:
                db.session.add(CodeItem(lang, "test php code item 1", "test php content code item {}".format(i)))

        for i in [1, 2]:
            db.session.add(Question(i, "test-question-sprint"))

        db.session.add(ChecklistType("empty-checklist-for-testing", "TBD"))
        db.session.add(ChecklistType("filled-checklist-for-testing", "TBD"))

        checklist_kb = ChecklistKB('1.0','test content checklist item 1', False, 123)
        checklist_kb.question_id = 2
        checklist_kb.kb_id = 2
        checklist_kb.checklist_type = 1
        db.session.add(checklist_kb)

        checklist_kb = ChecklistKB('1.1','test content checklist item 1', False, 123)
        checklist_kb.question_id = 2
        checklist_kb.kb_id = 2
        checklist_kb.checklist_type = 1
        db.session.add(checklist_kb)

        checklist_kb = ChecklistKB('1.2','test content checklist item 2', True, 124)
        checklist_kb.question_id = 0
        checklist_kb.kb_id = 1
        checklist_kb.checklist_type = 1
        db.session.add(checklist_kb)

        checklist_kb = ChecklistKB('1.3','test content checklist item 3', True, 125)
        checklist_kb.question_id = 0
        checklist_kb.kb_id = 1
        checklist_kb.checklist_type = 1
        db.session.add(checklist_kb)

        checklist_kb = ChecklistKB('1.4','test content checklist item 4', False, 126)
        checklist_kb.question_id = 2
        checklist_kb.kb_id = 2
        checklist_kb.checklist_type = 1
        db.session.add(checklist_kb)

        db.session.commit()
        return True

    except Exception as e:
        db.session.rollback()
        return False

def clear_db():
    try:
        db.drop_all()
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def init_db(testing=False):
    """Initializes the database.""" 

    if testing == True:

        db.drop_all()
        db.session.commit()
        return load_initial_data() & load_test_data()

    else:

        db.drop_all()
        db.session.commit()
        db.create_all()
        db.session.commit()

        return load_initial_data() & init_md_code_examples() & init_md_knowledge_base()   

def update_db():
    """Update the database."""
    KBItem.query.delete()
    CodeItem.query.delete()
    db.session.commit()

    init_md_code_examples()
    init_md_knowledge_base()


'''
def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if not hasattr(g, settings.DATABASE):
        g.sqlite_db = connect_db()
    return g.sqlite_db
'''

def init_md_knowledge_base():
    """Converts markdown knowledge-base items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/knowledge_base')
    try:
        for filename in os.listdir(kb_dir):
            if filename.endswith(".md"):
                name_raw = filename.split("-")
                kbID = name_raw[0].replace("_", " ")
                title = name_raw[3].replace("_", " ")
                file = os.path.join(kb_dir, filename)
                data = open(file, 'r')
                file_content = data.read()
                data.close()
                content_escaped = file_content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))

                #query = "INSERT OR REPLACE INTO kb_items (kbID, content, title) VALUES ('"+kbID+"','"+content_escaped+"', '"+title+"'); \n"
                #with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                #        myfile.write(query)
                try:
                    item = KBItem(kbID, content_escaped, title)
                    db.session.add(item)
                    db.session.commit()

                except IntegrityError as e:
                    print(e)
                    pass

        print('Initialized the markdown knowledge-base.')
        return True

    except Exception as e:
        print(e)
        return False


def init_md_code_examples():
    """Converts markdown code-example items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/code_examples/')
    code_langs = ['asp', 'java', 'php', 'flask', 'django', 'go', 'ruby']
    try:
        for lang in code_langs:
            for filename in os.listdir(kb_dir+lang):
                if filename.endswith(".md"):
                    name_raw = filename.split("-")
                    title = name_raw[3].replace("_", " ")
                    file = os.path.join(kb_dir+lang, filename)
                    data = open(file, 'r')
                    file_content = data.read()
                    data.close()
                    content_escaped = file_content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))

                    #query = "INSERT OR REPLACE INTO code_items (content, title, code_lang) VALUES ('"+content_escaped+"', '"+title+"', '"+lang+"'); \n"
                    #with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                    #        myfile.write(query)
                    try:
                        item = CodeItem(content_escaped, title, lang)
                        db.session.add(item)
                        db.session.commit()

                    except IntegrityError as e:
                        print(e)
                        pass

        print('Initialized the markdown code-examples.')
        return True

    except Exception as e:
        print(e)
        return False
