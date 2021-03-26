import time, random
from random import randint
from skf.database import db
from skf.database.lab_items import LabItem
from skf.database.lab_items_code import LabItemCode
from skf.database.lab_items_code_options import LabItemCodeOptions
from skf.api.security import log, val_num, val_alpha_num
from flask import render_template, Blueprint, jsonify, request, current_app
from skf.api.labs.deployment_tasks import SKFLabDeployment
from skf.api.labs.deletion_tasks import SKFLabDelete

def get_labs():
    log("User requested list of kb items", "LOW", "PASS")
    result = LabItem.query.order_by(LabItem.level.asc()).paginate(1, 2500, False)
    return result


def get_labs_code(code_type):
    log("User requested list of code review items", "LOW", "PASS")
    result = LabItemCode.query.filter(LabItemCode.code_type == code_type).paginate(1, 2500, False)
    return result


def get_labs_code_types():
    log("User requested list of code review items", "LOW", "PASS")
    result = LabItemCode.query.filter_by(LabItemCode.code_type).distinct()
    for bla in result.items:
        print(bla)
    #result = LabItemCode.query.order_by(LabItemCode.code_type.asc()).distinct().paginate(1, 2500, False)
    return result


def get_labs_code_sol(solutions_id):
    log("User requested list of code labs solution items", "LOW", "PASS")
    count = LabItemCodeOptions.query.count()
    sol_list = list(range(1, count))
    if solutions_id in sol_list: 
        sol_list.remove(solutions_id)
    rand_sol = random.sample(sol_list, 4)
    result = LabItemCodeOptions.query.filter((LabItemCodeOptions.id == solutions_id) | (LabItemCodeOptions.id == rand_sol[1]) | (LabItemCodeOptions.id == rand_sol[2]) | (LabItemCodeOptions.id == rand_sol[3])).paginate(1, 2500, False)
    return result


def get_labs_code_status(code_id, solution_id):
    log("User requested status of code item with solution", "LOW", "PASS")
    result = LabItemCode.query.filter((LabItemCode.id == code_id) & (LabItemCode.solution == solution_id)).count()
    if result > 0:
        return {'status': 'correct'}
    else:
        return {'status': 'incorrect'}


def deploy_labs(instance_name, userid):
    rpc = SKFLabDeployment()
    body = instance_name + ":" + str(userid)
    response = rpc.call(body)
    return response


def delete_labs(instance_name, userid):
    rpc = SKFLabDelete()
    body = instance_name + ":" + str(userid)
    response = rpc.call(body)
    return response
