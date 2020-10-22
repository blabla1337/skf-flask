<<<<<<< HEAD
import logging.config, os, datetime
=======
import os
import sys 
import datetime
>>>>>>> origin/master
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
from skf.database.checklist_category import ChecklistCategory
from skf.initial_data import load_initial_data

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

def clear_db():
<<<<<<< HEAD
    log.info("Clearing the database")
=======
    print("Clearing the database")
>>>>>>> origin/master
    try:
        db.drop_all()
        db.session.commit()
    except:
<<<<<<< HEAD
        log.info("Error occurred clearing the database")
=======
        print("Error occurred clearing the database")
>>>>>>> origin/master
        db.session.rollback()
        raise


def init_db(testing=False):
    """Initializes the database.""" 
    try:
<<<<<<< HEAD
        log.info("Initializing the database")
        db.create_all()
        prerequisits()
        init_md_code_examples()
        init_md_testing_examples()
        init_md_knowledge_base()
        load_initial_data()
    except:
        db.session.remove()
        log.info("Database is already existsing, nothing to do")
=======
        print("Initializing the database")
        db.create_all()
        prerequisits()
        init_md_knowledge_base()
        init_md_code_examples()
        load_initial_data()
    except:
        db.session.remove()
        print("Database is already existsing, nothing to do")
>>>>>>> origin/master


def clean_db(testing=False):
    """Clean and Initializes the database.""" 
<<<<<<< HEAD
    log.info("Clean and Initializing the database")
    clear_db()
=======
    clear_db()
    print("Clean and Initializing the database")
>>>>>>> origin/master
    db.create_all()
    prerequisits()
    init_md_code_examples()
    init_md_testing_examples()
    init_md_knowledge_base()
    load_initial_data()
    db.session.commit()
<<<<<<< HEAD


def update_db():
    """Update the database."""
    log.info("Update the database")
=======

def update_db():
    """Update the database."""
>>>>>>> origin/master
    KBItem.query.delete()
    CodeItem.query.delete()
    db.session.commit()
    init_md_code_examples()
    init_md_knowledge_base()
<<<<<<< HEAD


def init_md_knowledge_base():
    """Converts markdown knowledge-base items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/knowledge_base/')
    kb_dir_types = ['web', 'mobile']
    try:
        checklist_category_id = 0
        for kb_type in kb_dir_types:
            checklist_category_id += 1
            for filename in os.listdir(kb_dir+kb_type):
                if filename.endswith(".md"):
                    name_raw = filename.split("-")
                    kb_id = name_raw[0].replace("_", " ")
                    title = name_raw[3].replace("_", " ")
                    file = os.path.join(kb_dir+kb_type, filename)
                    data = open(file, 'r')
                    file_content = data.read()
                    data.close()
                    content = file_content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))
                    try:
                        item = KBItem(title, content, kb_id)
                        item.checklist_category_id = checklist_category_id
                        if (kb_id == "1"):
                            item.checklist_category_id = None
                        db.session.add(item)
                        db.session.commit()
                    except IntegrityError as e:
                        raise
        log.info("Initialized the markdown knowledge-base.")
=======

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
>>>>>>> origin/master
        return True
    except:
        raise


def init_md_code_examples():
    """Converts markdown code-example items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/code_examples/web/')
<<<<<<< HEAD
    code_langs = ['asp-needs-reviewing', 'java-needs-reviewing', 'php-needs-reviewing', 'flask', 'django-needs-reviewing', 'go-needs-reviewing', 'ruby-needs-reviewing', 'nodejs-express-needs-reviewing']
=======
    code_langs = ['asp', 'java', 'php', 'flask', 'django', 'go', 'ruby', 'nodejs-express']
>>>>>>> origin/master
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
<<<<<<< HEAD
        log.info("Initialized the markdown code-examples.")
        return True
    except:
        raise


def init_md_testing_examples():
    """Converts markdown testing code-example items to DB."""
    kb_dir = os.path.join(current_app.root_path, 'markdown/code_examples/web/')
    code_langs = ['testing']
    try:
        for lang in code_langs:
            for filename in sorted(os.listdir(kb_dir+lang)):
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
        log.info("Initialized the markdown code-examples.")
=======
        print('Initialized the markdown code-examples.')
>>>>>>> origin/master
        return True
    except:
        raise


def prerequisits():
    try:
        category = ChecklistCategory("Web applications", "category for web collection")
        db.session.add(category)
        db.session.commit()
        category = ChecklistCategory("Mobile applications", "category for mobile collection")
        db.session.add(category)
        db.session.commit()
<<<<<<< HEAD
        category = ChecklistCategory("Custom checklist", "category for custom checklist collection")
        db.session.add(category)
        db.session.commit()
        log.info("Initialized the prerequisits.")
=======
>>>>>>> origin/master
        return True
    except:
        raise
