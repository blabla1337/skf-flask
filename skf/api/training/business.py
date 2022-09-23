from skf.api.security import log
from skf.database import db
from skf.database.training import Training 
from flask import abort
from flask import current_app as app
from functools import lru_cache
import sys, json, yaml, copy


def _get_content_from_yml(path):
    result = {}
    with app.open_resource(path) as f:
        c_yaml = yaml.safe_load(f.read())
        c_json = json.dumps(c_yaml)
        result = json.loads(c_json)
    return result

@lru_cache(None)
def _get_training_profiles():
    result = _get_content_from_yml('training/profiles.yml')
    return result

@lru_cache(None)
def _get_training_course_files():
    result = {}
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        for course in profile['courses']:
            if 'courseFile' in course:
                result[course['id']] = course['courseFile']
    return result


@lru_cache(None)
def get_training_profile_items():
    log("User requested list training profiles", "LOW", "PASS")
    result = {}
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        if 'courses' in profile:
            del profile['courses']
    result = training_profiles
    return result

@lru_cache(None)
def get_training_profile_item(profile_id):
    log("User requested training profile item", "LOW", "PASS")
    result = None
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        if profile['id'] == profile_id:
            result = profile
            for course in profile['courses']:
                if 'courseFile' in course:
                    del course['courseFile']
            break
    return result

@lru_cache(None)
def get_training_course_item(course_id):
    log("User requested training course item", "LOW", "PASS")
    result = None
    course_files = _get_training_course_files()
    if course_id in course_files:
        result = _get_content_from_yml(course_files[course_id])
    return result

def get_progress(course_id, user_id):
    log("User requested training course progress", "LOW", "PASS")
    try:
        result = [t.category_id for t in \
            Training.query.filter(Training.user_id == user_id, Training.course_id == course_id).all()]
        return {'category_id': result[0]}
    except:
        db.session.rollback()
        return {'message': 'No completed courses found'}

def set_progress(data):
    log("User requested training course progress update", "MEDIUM", "PASS")
    try:
        training = Training(data.get('user_id'), data.get('course_id'), data.get('category_id'))
        db.session.add(training)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(400, 'Training not created')
    return {'message': 'Training successfully created'}
