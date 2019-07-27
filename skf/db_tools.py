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
from skf.initial_data import load_initial_data

#from sqlite3 import dbapi2 as sqlite3

def connect_db():
    """Connects to the specific database."""
    #rv = sqlite3.connect(os.path.join(app.root_path, settings.DATABASE))
    #rv.row_factory = sqlite3.Row
    #return rv
    return True

def load_initial_data():

#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (1, "edit:read:manage:delete", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (2, "edit:read:delete", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (3, "edit:read", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (4, "read", 1))
    try:
        p = Privilege('edit:read:manage:delete')
        db.session.add(p)
        db.session.add(Privilege('edit:read:delete'))
        db.session.add(Privilege('edit:read'))
        db.session.add(Privilege('read'))  

#   INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "False", "False", "example@owasp.org", 1))
        user = User(userName='admin', accessToken=1234, email="example@owasp.org")
        user.privilege = p
        db.session.add(user)

#   INSERT OR REPLACE INTO `groups` (`groupID`, `ownerID`, `groupName`) VALUES (1, 1, "privateGroup", 1))
        group = Group('privateGroup', datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
#   INSERT OR REPLACE INTO `groupMembers` (`memberID`, `userID`, `groupID`, `ownerID`) VALUES (1, 1, 1, 1, 1)
        group.members.append(user)
        group.owner = user
        db.session.add(group)

#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 1", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.", 1))
#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 2", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.", 1))
        db.session.add(ChecklistType(name='ASVS LEVEL 1', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))
        db.session.add(ChecklistType(name='ASVS LEVEL 2', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))


        db.session.add(Question("Does the sprint implement changes that affect and change CI/CD?", 1))
        db.session.add(Question("Does the sprint implement changes that affect authentication/authorization?", 1))
        db.session.add(Question("Does the sprint implement changes that affect session management?", 1))
        db.session.add(Question("Does the sprint implement changes that affect access control systems?", 1))
        db.session.add(Question("Does the sprint make use/implement an ORM framework? (object relational model)", 1))
        db.session.add(Question("Does the sprint implement functions that handle user supplied input? (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc)", 1))
        db.session.add(Question("Does the sprint implement functions that forward or redirect your users trough the application?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize wysiwyg editors?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize templating engines or single page apps such as (Angular, React)", 1))
        db.session.add(Question("Does the sprint implement functions that allow for SVG scriptable content to be uploaded/posted?", 1))
        db.session.add(Question("Does the sprint implement functions that reflect user supplied input on the side of the client?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize raw SQL queries?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize LDAP?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize OS commands?", 1))
        db.session.add(Question("Does the sprint implement functions that get/grabs files from the file system?", 1))
        db.session.add(Question("Does the sprint implement functions that parse or digests XML?", 1))
        db.session.add(Question("Does the sprint implement/change functions with native code (C, C++)", 1))
        db.session.add(Question("Does the sprint implement functions that deserializes objects (JSON, XML and YAML)", 1))
        db.session.add(Question("Does the sprint implement functions that process sensitive data?", 1))
        db.session.add(Question("Does the sprint imlement functions that require secure random values", 1))
        db.session.add(Question("Does the sprint implement functions that impact logging?", 1))
        db.session.add(Question("Does the sprint implement/changes TLS configuration?", 1))
        db.session.add(Question("Does the sprint implement functions that allow users to upload/download files?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize GraphQL", 1))
        db.session.add(Question("Does the sprint implement functions that store sensitive information?", 1))
        db.session.add(Question("Does the sprint implement functions that allow users to send emails?", 1))
        db.session.add(Question("Is the application in need of an architectural review?", 1))
        db.session.add(Question("Is the application in need of a review of configurations and settings?", 1))
        db.session.add(Question("Are you building on an application that has API features?", 1))
        db.session.add(Question("Does this sprint introduce functions with critical business logic that needs to be reviewed?", 1))
        db.session.add(Question("Does the sprint introduce change/affect on password policies?", 1))
        db.session.add(Question("Does the sprint introduce changes that affect OTP?", 1))

        db.session.add(Question("Does the sprint implement changes that affect and change CI/CD?", 2))
        db.session.add(Question("Does the sprint implement changes that affect authentication/authorization?", 2))
        db.session.add(Question("Does the sprint implement changes that affect session management?", 2))
        db.session.add(Question("Does the sprint implement changes that affect access control systems?", 2))
        db.session.add(Question("Does the sprint make use/implement an ORM framework? (object relational model)", 2))
        db.session.add(Question("Does the sprint implement functions that handle user supplied input? (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc)", 2))
        db.session.add(Question("Does the sprint implement functions that forward or redirect your users trough the application?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize wysiwyg editors?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize templating engines or single page apps such as (Angular, React)", 2))
        db.session.add(Question("Does the sprint implement functions that allow for SVG scriptable content to be uploaded/posted?", 2))
        db.session.add(Question("Does the sprint implement functions that reflect user supplied input on the side of the client?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize raw SQL queries?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize LDAP?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize OS commands?", 2))
        db.session.add(Question("Does the sprint implement functions that get/grabs files from the file system?", 2))
        db.session.add(Question("Does the sprint implement functions that parse or digests XML?", 2))
        db.session.add(Question("Does the sprint implement/change functions with native code (C, C++)", 2))
        db.session.add(Question("Does the sprint implement functions that deserializes objects (JSON, XML and YAML)", 2))
        db.session.add(Question("Does the sprint implement functions that process sensitive data?", 2))
        db.session.add(Question("Does the sprint imlement functions that require secure random values", 2))
        db.session.add(Question("Does the sprint implement functions that impact logging?", 2))
        db.session.add(Question("Does the sprint implement/changes TLS configuration?", 2))
        db.session.add(Question("Does the sprint implement functions that allow users to upload/download files?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize GraphQL", 2))
        db.session.add(Question("Does the sprint implement functions that store sensitive information?", 2))
        db.session.add(Question("Does the sprint implement functions that allow users to send emails?", 2))
        db.session.add(Question("Is the application in need of an architectural review?", 2))
        db.session.add(Question("Is the application in need of a review of configurations and settings?", 2))
        db.session.add(Question("Are you building on an application that has API features?", 2))
        db.session.add(Question("Does this sprint introduce functions with critical business logic that needs to be reviewed?", 2))
        db.session.add(Question("Does the sprint introduce change/affect on password policies?", 2))
        db.session.add(Question("Does the sprint introduce changes that affect OTP?", 2))

        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def load_test_data():
    print("****** TEST DATA *******")
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
        clear_db()
        db.create_all()
        db.session.commit()

        load_initial_data()
        init_md_code_examples()
        init_md_knowledge_base()

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
                kb_id = name_raw[0].replace("_", " ")
                title = name_raw[3].replace("_", " ")
                file = os.path.join(kb_dir, filename)
                data = open(file, 'r')
                file_content = data.read()
                data.close()
                content = file_content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))

                #query = "INSERT OR REPLACE INTO kb_items (kbID, content, title) VALUES ('"+kbID+"','"+content_escaped+"', '"+title+"', 1) \n"
                #with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                #        myfile.write(query)
                try:
                    item = KBItem(title, content, kb_id)
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

                    #query = "INSERT OR REPLACE INTO code_items (content, title, code_lang) VALUES ('"+content_escaped+"', '"+title+"', '"+lang+"', 1) \n"
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