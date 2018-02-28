import os
from skf import settings
from shutil import copyfile
from flask import Flask
from sqlite3 import dbapi2 as sqlite3


app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(os.path.join(app.root_path, settings.DATABASE))
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    try:
        if (os.path.exists(os.path.join(app.root_path, settings.DATABASE))):
            os.remove(os.path.join(app.root_path, settings.DATABASE))
        open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a')
        if (os.path.exists(os.path.join(app.root_path, 'db.sqlite_schema'))):
            os.remove(os.path.join(app.root_path, 'db.sqlite_schema'))
        copyfile(os.path.join(app.root_path, "schema.sql"), os.path.join(app.root_path, 'db.sqlite_schema'))
        init_md_checklists()
        init_md_code_examples()
        init_md_knowledge_base()
        db = connect_db()
        with app.open_resource(os.path.join(app.root_path, 'db.sqlite_schema'), mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        return True
    except Exception as e:
        print('Exception in file db_tools, method init_db: ' + e)
        return False


def update_db():
    """Update the database."""
    try:
        if (os.path.exists(os.path.join(app.root_path, 'db.sqlite_schema'))):
            os.remove(os.path.join(app.root_path, 'db.sqlite_schema'))
        db = connect_db()
        db.execute("DELETE FROM kb_items")
        db.execute("DELETE FROM code_items")
        db.execute("DELETE FROM checklists")
        db.commit()

        init_md_checklists()
        init_md_code_examples()
        init_md_knowledge_base()

        with app.open_resource(os.path.join(app.root_path, 'db.sqlite_schema'), mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        return True
    except Exception as e:
        print('Exception in file db_tools, method update_db: ' + e)
        return False


def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if not hasattr(g, settings.DATABASE):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_md_knowledge_base():
    """Converts markdown knowledge-base items to DB."""
    kb_dir = os.path.join(app.root_path, 'markdown/knowledge_base')
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
                query = "INSERT OR REPLACE INTO kb_items (kbID, content, title) VALUES ('"+kbID+"','"+content_escaped+"', '"+title+"'); \n"
                with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                        myfile.write(query)
        print('Initialized the markdown knowledge-base.')
        return True
    except Exception as e:
        print('Exception in file db_tools, method init_md_knowledge_base: ' + e)
        return False


def init_md_code_examples():
    """Converts markdown code-example items to DB."""
    kb_dir = os.path.join(app.root_path, 'markdown/code_examples/')
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
                    query = "INSERT OR REPLACE INTO code_items (content, title, code_lang) VALUES ('"+content_escaped+"', '"+title+"', '"+lang+"'); \n"
                    with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                            myfile.write(query)
        print('Initialized the markdown code-example.')
        return True
    except Exception as e:
        print('Exception in file db_tools, method init_md_code_examples: ' + e)
        return False


def init_md_checklists():
    """Converts markdown checklists items to DB."""
    kb_dir = os.path.join(app.root_path, 'markdown/checklists/')
    try:
        #checklists = ['asvs', 'pcidss', 'custom']
        checklists = ['asvs', 'custom', 'masvs']
        for checklist in checklists:
            if checklist == "asvs":
                for filename in os.listdir(kb_dir+checklist):
                    if filename.endswith(".md"):
                        name_raw = filename.split("-")
                        level = name_raw[4].replace("_", " ")
                        kbid_raw = name_raw[6].split(".")
                        kb_id = kbid_raw[0]
                        if level == "0":
                            # For the ASVS categories
                            file = os.path.join(kb_dir+checklist, filename)
                            data = open(file, 'r')
                            file_content = data.read()
                            data.close()
                            checklistID_raw = file_content.split(":")
                            checklistID = checklistID_raw[0]
                            checklistID = checklistID.lstrip('V')
                            checklistID = checklistID+".0"
                        else :
                            # For the ASVS items
                            file = os.path.join(kb_dir+checklist, filename)
                            data = open(file, 'r')
                            file_content = data.read()
                            data.close()
                            checklistID_raw = file_content.split(" ")
                            checklistID = checklistID_raw[0]
                        file = os.path.join(kb_dir+checklist, filename)
                        data = open(file, 'r')
                        file_content = data.read()
                        data.close()
                        content = file_content.split(' ', 1)[1]
                        content_escaped = content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))
                        query = "INSERT OR REPLACE INTO checklists (checklistID, content, level, kbID) VALUES ('"+checklistID+"', '"+content_escaped+"', '"+level+"', '"+kb_id+"'); \n"
                        with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                            myfile.write(query)
            if checklist == 'masvs':
                for filename in os.listdir(kb_dir+checklist):
                    if filename.endswith(".md"):
                        name_raw = filename.split("-")
                        level = name_raw[4].replace("_", " ")
                        kbid_raw = name_raw[6].split(".")
                        kb_id = kbid_raw[0]
                        if level == "0":
                            # For the MASVS categories
                            file = os.path.join(kb_dir+checklist, filename)
                            data = open(file, 'r')
                            file_content = data.read()
                            data.close()
                            checklistID_raw = file_content.split(":")
                            checklistID = checklistID_raw[0]
                            checklistID = checklistID.lstrip('V')
                            checklistID = checklistID+".0"
                        else :
                            # For the MASVS items
                            file = os.path.join(kb_dir+checklist, filename)
                            data = open(file, 'r')
                            file_content = data.read()
                            data.close()
                            checklistID_raw = file_content.split(" ")
                            checklistID = checklistID_raw[0]     
                        file = os.path.join(kb_dir+checklist, filename)
                        data = open(file, 'r')
                        file_content = data.read()
                        data.close()
                        content = file_content.split(' ', 1)[1]
                        content_escaped = content.translate(str.maketrans({"'":  r"''", "-":  r"", "#":  r""}))
                        query = "INSERT OR REPLACE INTO checklists (checklistID, content, level, kbID) VALUES ('"+checklistID+"', '"+content_escaped+"', '"+level+"', '"+kb_id+"'); \n"
                        with open(os.path.join(app.root_path, 'db.sqlite_schema'), 'a') as myfile:
                                myfile.write(query)
        print('Initialized the markdown checklists.')
        return True
    except Exception as e:
        print('Exception in file db_tools, method init_md_checklists: ' + e)
        return False