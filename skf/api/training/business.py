from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special
from flask import current_app as app
from functools import cache
import sys, json, yaml


@cache
def get_training_profiles():
    result = {}
    with app.open_resource('training/profiles.yml') as f:
        p_yaml = yaml.safe_load(f.read())
        p_json = json.dumps(p_yaml)
        result = json.loads(p_json)
    return result

@cache
def get_training_profile_items():
    log("User requested list training profiles", "LOW", "PASS")
    result = {}
    training_profiles = get_training_profiles()
    for profile in training_profiles['profiles']:
        if 'courses' in profile:
            del profile['courses']
    result = training_profiles
    return result

@cache
def get_training_profile_item(id):
    log("User requested training profile item", "LOW", "PASS")
    result = None
    training_profiles = get_training_profiles()
    for profile in training_profiles['profiles']:
        if profile['id'] == id:
            result = profile
            for course in profile['courses']:
                if 'courseFile' in course:
                    del course['courseFile']
            break
    return result
