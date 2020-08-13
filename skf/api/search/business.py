import time, json
from skf.database import db
from skf.api.security import log, val_num, val_alpha_num
from skf.database.kb_items import KBItem
from skf.database.lab_items import LabItem
from skf.database.code_items import CodeItem
from skf.database.checklists_kb import ChecklistKB
from skf.database.project_sprints import ProjectSprint 


def search_kb(search_string):
    log("User requested search of kb items", "LOW", "PASS")
    search = "%{}%".format(search_string)
    return  KBItem.query.filter(KBItem.content.like(search)).all()


def search_lab(search_string):
    log("User requested search of lab items", "LOW", "PASS")
    search = "%{}%".format(search_string)
    lab_result = LabItem.query.filter(LabItem.title.like(search)).all()
    return lab_result


def search_code(search_string):
    log("User requested search of kb items", "LOW", "PASS")
    search = "%{}%".format(search_string)
    code_result = CodeItem.query.filter(CodeItem.title.like(search)).all()
    return code_result


def search_checklist(search_string):
    log("User requested search of kb items", "LOW", "PASS")
    search = "%{}%".format(search_string)
    checklist_result = ChecklistKB.query.filter(ChecklistKB.content.like(search)).all()
    return checklist_result


def search_project(search_string):
    log("User requested search of kb items", "LOW", "PASS")
    search = "%{}%".format(search_string)
    project_result = ProjectSprint.query.filter(ProjectSprint.description.like(search)).all()
    return project_result

