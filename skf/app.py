# -*- coding: utf-8 -*-
"""
    Security Knowledge Framework is an expert system application
    that uses OWASP Application Security Verification Standard, code examples
    and helps developers in pre-development & post-development.
    Copyright (C) 2017 Glenn ten Cate, Riccardo ten Cate
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import logging.config, os, re

from flask import Flask, Blueprint
from flask_cors import CORS, cross_origin
from skf import settings
from skf.db_tools import init_md_checklists, init_md_knowledge_base, init_md_code_examples, init_db, update_db
from skf.api.projects.endpoints.project_items import ns as project_namespace
from skf.api.projects.endpoints.project_item import ns as project_namespace
from skf.api.projects.endpoints.project_delete import ns as project_namespace
from skf.api.projects.endpoints.project_new import ns as project_namespace
from skf.api.projects.endpoints.project_stats import ns as project_namespace
from skf.api.projects.endpoints.project_update import ns as project_namespace
from skf.api.sprints.endpoints.sprint_item import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_delete import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_new import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_stats import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_update import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_results import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_results_audit import ns as sprints_namespace
from skf.api.sprints.endpoints.sprint_results_audit_export import ns as sprints_namespace
from skf.api.checklist.endpoints.checklist_items import ns as checklist_namespace
from skf.api.checklist.endpoints.checklist_item import ns as checklist_namespace
from skf.api.checklist.endpoints.checklist_level import ns as checklist_namespace
from skf.api.code.endpoints.code_items import ns as code_namespace
from skf.api.code.endpoints.code_item import ns as code_namespace
from skf.api.code.endpoints.code_item_update import ns as code_namespace
from skf.api.code.endpoints.code_items_lang import ns as code_namespace
from skf.api.user.endpoints.user_create import ns as users_namespace
from skf.api.user.endpoints.user_activate import ns as users_namespace
from skf.api.user.endpoints.user_login import ns as users_namespace
from skf.api.user.endpoints.user_list import ns as users_namespace
from skf.api.user.endpoints.user_manage import ns as users_namespace
from skf.api.kb.endpoints.kb_items import ns as kb_namespace
from skf.api.kb.endpoints.kb_item import ns as kb_namespace
from skf.api.kb.endpoints.kb_item_update import ns as kb_namespace
from skf.api.questions_pre.endpoints.question_pre_items import ns as questions_pre_namespace
from skf.api.questions_pre.endpoints.question_pre_store import ns as questions_pre_namespace
from skf.api.questions_pre.endpoints.question_pre_update import ns as questions_pre_namespace
from skf.api.questions_sprint.endpoints.question_sprint_items import ns as questions_sprint_namespace
from skf.api.questions_sprint.endpoints.question_sprint_store import ns as questions_sprint_namespace
from skf.api.questions_post.endpoints.question_post_items import ns as questions_post_namespace
from skf.api.questions_post.endpoints.question_post_store import ns as questions_post_namespace
from skf.api.comment.endpoints.comment_items import ns as comment_namespace
from skf.api.comment.endpoints.comment_new import ns as comment_namespace

from skf.api.restplus import api
from skf.database import db


app = Flask(__name__)
# TO DO FIX WILDCARD ONLY ALLOW NOW FOR DEV
cors = CORS(app, resources={r"/*": {"origins": settings.ORIGINS}})
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    """Configure the SKF app."""
    #cannot use SERVER_NAME because it will mess up the routing
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['TESTING'] = settings.TESTING
    flask_app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG


def initialize_app(flask_app):
    """Initialize the SKF app."""
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(kb_namespace)
    api.add_namespace(code_namespace)
    api.add_namespace(users_namespace)
    api.add_namespace(project_namespace)
    api.add_namespace(comment_namespace)
    api.add_namespace(sprints_namespace)
    api.add_namespace(checklist_namespace)
    api.add_namespace(questions_pre_namespace)
    api.add_namespace(questions_post_namespace)
    api.add_namespace(questions_sprint_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


@app.cli.command('initdb')
def initdb_command():
    """Creates the database with all the Markdown files."""
    init_db()
    print('Initialized the database.')


@app.cli.command('updatedb')
def initdb_command():
    """Update the database with the markdown files."""
    update_db()
    print('Markdown files updated in the database.')


def main():
    """Main SKF method"""
    initialize_app(app)

    print(app.debug)
    if app.debug == False:
        if  settings.JWT_SECRET == '':
            log.info('>>>>> Configure the JWT_SECRET in the settings.py file and choose an unique 128 character long secret <<<<<')
        else:
            log.info('>>>>> Starting development server http://'+settings.FLASK_HOST+":"+str(settings.FLASK_PORT)+' <<<<<')
            app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=app.debug)
    if app.debug == True:
        if  settings.JWT_SECRET == '':
            log.info('>>>>> Starting development server http://'+settings.FLASK_HOST+":"+str(settings.FLASK_PORT)+' <<<<<')
            app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=app.debug)        


if __name__ == "__main__":
    main()
