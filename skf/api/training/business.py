from skf.database import db
from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special
# from skf.database.training import Profile, Course, Topic, Category
# from sqlalchemy import desc, asc
from flask import current_app as app
from functools import cache
import sys, json, yaml


@cache
def get_training_profiles():
    log("User requested list training profiles", "LOW", "PASS")
    with app.open_resource('training/profiles.yml') as f:
        result = json.dumps(yaml.safe_load(f.read()))
    return result
