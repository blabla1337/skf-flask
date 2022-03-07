from skf.api.security import log, val_num, val_float, val_alpha_num, val_alpha_num_special
from flask import current_app as app
from functools import cache
import sys, json, yaml, copy


def _get_content_from_yml(path):
    result = {}
    with app.open_resource(path) as f:
        c_yaml = yaml.safe_load(f.read())
        c_json = json.dumps(c_yaml)
        result = json.loads(c_json)
    return result

@cache
def _get_training_profiles():
    result = _get_content_from_yml('training/profiles.yml')
    return result

@cache
def _get_training_courses():
    result = {}
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        for course in profile['courses']:
            if 'courseFile' in course:
                del course['courseFile']
            result[course['id']] = course
    return result

@cache
def _get_training_course_files():
    result = {}
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        for course in profile['courses']:
            if 'courseFile' in course:
                result[course['id']] = course['courseFile']
    return result


@cache
def get_training_profile_items():
    log("User requested list training profiles", "LOW", "PASS")
    result = {}
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        if 'courses' in profile:
            del profile['courses']
    result = training_profiles
    return result

@cache
def get_training_profile_item(id):
    log("User requested training profile item", "LOW", "PASS")
    result = None
    training_profiles = copy.deepcopy(_get_training_profiles())
    for profile in training_profiles['profiles']:
        if profile['id'] == id:
            result = profile
            for course in profile['courses']:
                if 'courseFile' in course:
                    del course['courseFile']
            break
    return result

@cache
def get_training_course_info(id):
    log("User requested training course item", "LOW", "PASS")
    result = None
    training_courses = _get_training_courses()
    if id in training_courses:
        result = training_courses[id]
    return result

@cache
def get_training_course_item(id):
    log("User requested training course item", "LOW", "PASS")
    result = None
    course_files = _get_training_course_files()
    if id in course_files:
        result = _get_content_from_yml(course_files[id])
    return result

