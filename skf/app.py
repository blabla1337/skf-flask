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
from skf.db_tools import init_md_checklists, init_md_knowledge_base, init_md_code_examples, init_db
from skf.api.user.endpoints.create import ns as users_create_namespace
from skf.api.user.endpoints.activate import ns as users_activate_namespace
from skf.api.user.endpoints.login import ns as users_login_namespace
from skf.api.kb.endpoints.kb_items import ns as kb_items_namespace
from skf.api.code.endpoints.code_items import ns as code_items_namespace
from skf.api.checklist.endpoints.checklist_items import ns as checklist_items_namespace
from skf.api.projects.endpoints.project_items import ns as project_items_namespace
from skf.api.restplus import api
from skf.database import db



app = Flask(__name__)
# TO DO FIX WILDCARD ONLY ALLOW NOW FOR DEV
cors = CORS(app, resources={r"/*": {"origins": "*"}})
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    """Configure the SKF app."""
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['TESTING'] = settings.TESTING


def initialize_app(flask_app):
    """Initialize the SKF app."""
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(users_create_namespace)
    api.add_namespace(users_activate_namespace)
    api.add_namespace(users_login_namespace)
    api.add_namespace(kb_items_namespace)
    api.add_namespace(checklist_items_namespace)
    api.add_namespace(project_items_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


@app.cli.command('initdb')
def initdb_command():
    """Creates the database with all the Markdown files."""
    init_db()
    print('Initialized the database.')


def main():
    """Main SKF method"""
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
