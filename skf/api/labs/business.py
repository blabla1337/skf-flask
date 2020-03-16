from skf.database import db
from skf.database.lab_items import LabItem
from skf.api.security import log, val_num, val_alpha_num
import time
from flask import render_template, Blueprint, jsonify, request, current_app
from skf.api.labs.deployment_tasks import SKFLabDeployment
from skf.api.labs.deletion_tasks import SKFLabDelete

def get_labs():
    log("User requested list of kb items", "LOW", "PASS")
    result = LabItem.query.order_by(LabItem.level.asc()).paginate(1, 500, False)
    return result


def deploy_labs(instance_name):
    rpc = SKFLabDeployment()
    response = rpc.call(instance_name)
    return response


def delete_labs(instance_name):
    rpc = SKFLabDelete()
    response = rpc.call(instance_name)
    return response

