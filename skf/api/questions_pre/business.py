from skf.database import db
from skf.database.projects import projects
from skf.database.checklists_kb import checklists_kb
from skf.database.questions_pre import questions_pre
from skf.database.project_sprints import project_sprints
from skf.database.checklists_results import checklists_results
from skf.database.question_pre_results import question_pre_results
from skf.database.question_sprint_results import question_sprint_results
from skf.api.security import log, val_num, val_alpha


def get_pre_items():
    log("User requested list of question pre items", "LOW", "PASS")
    result = questions_pre.query.paginate(1, 500, False)
    return result


def store_pre_questions(user_id, data):
    log("User stored new pre question list", "MEDIUM", "PASS")
    val_num(user_id)
    question = data.get('questions')
    val_num(question[0]['projectID'])
    project_id = question[0]['projectID']
    project_results = project_sprints.query.filter(project_sprints.projectID == project_id).one()
    sprint_id = project_results.sprintID
    projects_result = projects.query.filter(projects.projectID == project_id).one()
    project_lvl = projects_result.level
    status = 1
    pre_item = "True"
    for result in data.get('questions'):
        val_num(result['question_pre_ID'])
        val_alpha(result['result'])
        val_num(result['projectID'])
        question_pre_ID = result['question_pre_ID']
        question_result = result['result']
        question_project_id = result['projectID']
        questions = question_pre_results(question_project_id, question_pre_ID, question_result)
        db.session.add(questions)
        db.session.commit()
        questions_results = question_pre_results.query.filter(question_pre_results.projectID == question_project_id).filter(question_pre_results.result == "False").all()
    for results in questions_results:
        project_id = results.projectID
        questionpreID = results.question_pre_ID
        if project_lvl == 1:
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == questionpreID).filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 2:
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == questionpreID).filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 3:
            checklists = checklists_kb.query.filter(checklists_kb.question_pre_ID == questionpreID).filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists:
            checklists_query = checklists_results(row.checklistID, project_id, sprint_id, status, pre_item, row.kbID)
            db.session.add(checklists_query)
            db.session.commit()
    if project_lvl == 1:
        checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    elif project_lvl == 2:
        checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    elif project_lvl == 3:
        checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    for row in checklists_first:
        checklists_query_first = checklists_results(row.checklistID, question_project_id, sprint_id, status, pre_item, row.kbID)
        db.session.add(checklists_query_first)
        db.session.commit()
    return {'message': 'Pre questions successfully created'}


def update_pre_questions(project_id, user_id, data):
    log("User updated pre question list", "MEDIUM", "PASS")
    val_num(user_id)
    val_num(project_id)
    clear_question_pre_rows = db.session.query(question_pre_results).filter(question_pre_results.projectID == project_id)
    clear_question_pre_rows.delete(synchronize_session=False)
    clear_checklists_results_rows = db.session.query(checklists_results).filter(checklists_results.preItem == 'True').filter(checklists_results.projectID == project_id)
    clear_checklists_results_rows.delete(synchronize_session=False)
    db.session.commit()
    project_results = project_sprints.query.filter(project_sprints.projectID == project_id).one()
    sprint_id = project_results.sprintID
    projects_result = projects.query.filter(projects.projectID == project_id).one()
    project_lvl = projects_result.level
    status = 1
    pre_item = "True"
    for result in data.get('questions'):
        val_num(result['question_pre_ID'])
        val_alpha(result['result'])
        question_pre_ID = result['question_pre_ID']
        question_result = result['result']
        questions = question_pre_results(project_id, question_pre_ID, question_result)
        db.session.add(questions)
        db.session.commit()
        questions_results = question_pre_results.query.filter(question_pre_results.projectID == project_id).filter(question_pre_results.result == "False").all()
    for results in questions_results:
        projectID = results.projectID
        questionpreID = results.question_pre_ID
        if project_lvl == 1:
            checklists = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 2:
            checklists = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 3:
            checklists = checklists_kb.query.filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        for row in checklists:
            checklists_query = checklists_results(row.checklistID, projectID, sprint_id, status, pre_item, row.kbID)
            db.session.add(checklists_query)
            db.session.commit()
        if project_lvl == 1:
            checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 2:
            checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
        elif project_lvl == 3:
            checklists_first = checklists_kb.query.filter(checklists_kb.include_first == "True").filter(checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).order_by(checklists_kb.checklistID).all()
    for row in checklists_first:
        checklists_query_first = checklists_results(row.checklistID, projectID, sprint_id, status, pre_item, row.kbID)
        db.session.add(checklists_query_first)
        db.session.commit()
    return {'message': 'Pre questions successfully updated'}


