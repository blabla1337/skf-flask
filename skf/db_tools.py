import os
import sys 
import datetime
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from shutil import copyfile
from skf.database import db
from skf.database.users import User
from skf.database.groups import Group
from skf.database.privileges import Privilege
from skf.database.kb_items import KBItem
from skf.database.code_items import CodeItem
from skf.database.checklist_types import ChecklistType
from skf.initial_data import load_initial_data

def connect_db():
    """Connects to the specific database."""
    #rv = sqlite3.connect(os.path.join(app.root_path, settings.DATABASE))
    #rv.row_factory = sqlite3.Row
    #return rv
    return True

def load_test_data():
    print("Loading test data")
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
    except:
        db.session.rollback()
        raise


def clear_db():
    print("Clearing the database")
    try:
        db.drop_all()
        db.session.commit()
    except:
        print("Error occurred clearing the database")
        db.session.rollback()
        raise


def init_db(testing=False):
    """Initializes the database.""" 
    try:
        print("Initializing the database")
        db.create_all()
        db.session.commit()
        init_md_code_examples()
        init_md_knowledge_base()
        load_initial_data()
    except:
        print("Database is already existsing, nothing to do")


def clean_db(testing=False):
    """Clean and Initializes the database.""" 
    clear_db()
    print("Clean and Initializing the database")
    db.create_all()
    db.session.commit()
    init_md_code_examples()
    init_md_knowledge_base()
    load_initial_data()

def update_db():
    """Update the database."""
    KBItem.query.delete()
    CodeItem.query.delete()
    db.session.commit()
    init_md_code_examples()
    init_md_knowledge_base()

def init_md_knowledge_base():
    """Converts markdown knowledge-base items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/knowledge_base/web')
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
                try:
                    item = KBItem(title, content, kb_id)
                    if (kb_id == "1"):
                        item.checklist_category_id = 0
                    else:
                        item.checklist_category_id = 1
                    db.session.add(item)
                    db.session.commit()
                except IntegrityError as e:
                    raise
        print('Initialized the markdown knowledge-base.')
        return True
    except:
        raise


def init_md_code_examples():
    """Converts markdown code-example items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/code_examples/web/')
    code_langs = ['asp', 'java', 'php', 'flask', 'django', 'go', 'ruby', 'nodejs-express']
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
                    try:
                        item = CodeItem(content_escaped, title, lang)
                        item.checklist_category_id = 1
                        db.session.add(item)
                        db.session.commit()
                    except IntegrityError as e:
                        print(e)
                        pass
        print('Initialized the markdown code-examples.')
        return True
    except:
        raise