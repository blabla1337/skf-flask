from skf.database import db
from skf.database.lab_items import LabItem
from skf.api.security import log, val_num, val_alpha_num
import time
import redis
from rq import Queue, Connection
from flask import render_template, Blueprint, jsonify, request, current_app
from skf.api.labs.deployment_tasks import SKFRPC

def get_labs():
    log("User requested list of kb items", "LOW", "PASS")
    result = LabItem.query.order_by(LabItem.level.asc()).paginate(1, 500, False)
    return result


def deploy_labs():
    rpc = SKFRPC()
    response = rpc.call("hello-world.yaml")
    return response


