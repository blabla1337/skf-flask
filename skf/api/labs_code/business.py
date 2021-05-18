import time, random
from random import choice
from skf.database import db
from skf.database.lab_items import LabItem
from skf.database.lab_items_code import LabItemCode
from skf.database.lab_items_code_options import LabItemCodeOptions
from skf.database.lab_items_code_finished_by_user import LabItemCodeFinishedByUser
from skf.api.security import log, val_num, val_alpha_num
from flask import render_template, Blueprint, jsonify, request, current_app
from flask_restplus import abort


def get_random_code_lab(user_id, code_type):
    log("User requested list of code review items", "LOW", "PASS")
    try:
        finished_labs = list_of_labs_finished_by_user(user_id)
        total_labs = code_labs_total_per_code_type(code_type)
        random_id = randomize_id_for_code_lab_challenge(finished_labs, total_labs)
        lab = LabItemCode.query.filter(LabItemCode.code_type == code_type).filter(LabItemCode.id == random_id).first()
        questions = get_labs_code_sol(lab.solution)
        json_response = convert_to_json(lab, questions)
        return json_response
    except:
        raise abort(404, message='no more challanges found!')


def verify_user_answer(user_id, code_id, solution_id):
    log("User requested status of code item with solution", "LOW", "PASS")
    result = LabItemCode.query.filter((LabItemCode.id == code_id) & (LabItemCode.solution == solution_id)).count()
    if result > 0:
        update_finished_labs_table(user_id, code_id)
        return {'status': 'correct'}
    else:
        return {'status': 'incorrect'}


def update_finished_labs_table(user_id, challenge_id):
    log("User updates finished labs table", "LOW", "PASS")
    try:
        result = LabItemCodeFinishedByUser(user_id, challenge_id)
        db.session.add(result)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'challenge not marked as solved')
    return {'message': 'challenge marked as solved'}


def code_labs_total_per_code_type(code_type):
    return LabItemCode.query.filter(LabItemCode.code_type ==  code_type).count()


def list_of_labs_finished_by_user(user_id):
    lab_id_list = []
    finished_labs = LabItemCodeFinishedByUser.query.filter(LabItemCodeFinishedByUser.user_id == user_id).all()
    for value in finished_labs:
        lab_id_list.append(value.challenge_id)
    return lab_id_list


def randomize_id_for_code_lab_challenge(finished_labs, total_labs):
    if len(finished_labs) >= total_labs:
         raise "no more challenges left!"
    else:
        random_lab = random.randint(1, total_labs)
    while random_lab in finished_labs:
        random_lab = random.randint(1, total_labs)
    return random_lab


def get_labs_code_sol(solutions_id):
    log("User requested list of code labs solution items", "LOW", "PASS")
    count = LabItemCodeOptions.query.count()
    sol_list = list(range(1, count))
    if solutions_id in sol_list: 
        sol_list.remove(solutions_id)
    rand_sol = random.sample(sol_list, 4)
    result = LabItemCodeOptions.query.filter((LabItemCodeOptions.id == solutions_id) | (LabItemCodeOptions.id == rand_sol[1]) | (LabItemCodeOptions.id == rand_sol[2]) | (LabItemCodeOptions.id == rand_sol[3])).paginate(1, 2500, False)
    return result

def convert_to_json(lab, answers):
    response = {
    "lab":{
        "id": lab.id,  
        "code_example": lab.code_example,
        "hint": lab.code_example,    
        "code_type": lab.code_type,    
    },
    "answers":[
        {"answer_1_id": answers.items[0].id, "answer_1": answers.items[0].vuln},
        {"answer_2_id": answers.items[1].id, "answer_2": answers.items[1].vuln},
        {"answer_3_id": answers.items[2].id, "answer_3": answers.items[2].vuln},
        {"answer_4_id": answers.items[3].id, "answer_4": answers.items[3].vuln},
        ]
    }
    return response