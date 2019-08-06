#!/usr/bin/env python3

# Convert initial data from schema.sql to SQLAlchemy Python statements
# Usage: ./sql2orm.py > initial_data.py
import sys
import re
import csv

def line2dict(line):

	(a,b) = line.split('VALUES')

	p = re.compile("\((.*)\)")
	m = p.search(a)

	for row in csv.reader([m.group(1)], quotechar='`'):
		keys = [x.strip().strip("`") for x in row]

	p = re.compile("\((.*)\)")
	m = p.search(b)
	for row in csv.reader([m.group(1)], quotechar="'", delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
		values = [x.strip("'") for x in row]

	values = [v.replace('\'','\\') for v in values]

	return dict(zip(keys, values))

def header():
	return """

import datetime
from skf.database import db
from skf.database.privileges import Privilege
from skf.database.users import User
from skf.database.groups import Group
from skf.database.questions import Question
from skf.database.checklist_types import ChecklistType
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklists_results import ChecklistResult
from skf.database.code_items import CodeItem
from skf.database.comments import Comment
from skf.database.groupmembers import GroupMember
from skf.database.kb_items import KBItem
from skf.database.lab_items import LabItem
from skf.database.logs import Log
from skf.database.project_sprints import ProjectSprint
from skf.database.projects import Project
from skf.database.question_results import QuestionResult

def load_initial_data():

#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (1, "edit:read:manage:delete", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (2, "edit:read:delete", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (3, "edit:read", 1))
#   INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (4, "read", 1))
    try:
        p = Privilege('edit:read:manage:delete')
        db.session.add(p)
        db.session.add(Privilege('edit:read:delete'))
        db.session.add(Privilege('edit:read'))
        db.session.add(Privilege('read'))  

#   INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "False", "False", "example@owasp.org", 1))
        user = User(userName='admin', accessToken=1234, email="example@owasp.org")
        user.privilege = p
        db.session.add(user)

#   INSERT OR REPLACE INTO `groups` (`groupID`, `ownerID`, `groupName`) VALUES (1, 1, "privateGroup", 1))
        group = Group('privateGroup', datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
#   INSERT OR REPLACE INTO `groupMembers` (`memberID`, `userID`, `groupID`, `ownerID`) VALUES (1, 1, 1, 1, 1)
        group.members.append(user)
        group.owner = user
        db.session.add(group)

#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 1", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.", 1))
#   INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS LEVEL 2", "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.", 1))
        db.session.add(ChecklistType(name='ASVS LEVEL 1', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))
        db.session.add(ChecklistType(name='ASVS LEVEL 2', description='The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.'))

"""


def footer():
	return """
        db.session.commit()
        return True

    except:
        db.session.rollback()
        raise
"""

def output(line=''):
	print("        " + line)

def main():

	print(header())
	filename = sys.argv[1] if len(sys.argv)>1 else "schema.sql" 
	f = open(filename, "r")

	for line in f:
		if "INSERT" in line:
			if "`questions`" in line:
				d = line2dict(line)
				output("q = Question('{}', {})".format(d['question'], d['checklist_type']))
				output("db.session.add(q)")
				output("db.session.commit()")
				output()

			elif "checklists_kb" in line:

				d = line2dict(line)
				#print(d)
				output("c = ChecklistKB('{}', '{}', {}, {}, {});".format(
					d['checklistID'],
					d['content'],
					d['checklist_type'],
					True if d['include_always'].lower()=='true' else False,
					d['cwe']
				))
				output("c.question_id = {}".format(d['question_ID']))
				output("c.kb_id = {}".format(d['kbID']))
				output("db.session.add(c)")
				output("db.session.commit()")
				output()
				#def __init__(self, checklist_id, content, checklist_type, include_always, cwe):
			elif "`lab_items`" in line:
				d = line2dict(line)
				output("db.session.add(LabItem('{}','{}', {}))".format(d['title'],d['link'],d['level']))
				output("db.session.commit()")
				output()


			elif "`users`" in line:
				pass
			elif "`groups`" in line:
				pass
			elif "`groupMembers`" in line:
				pass
			elif "`privileges`" in line:
				pass
			elif "`checklist_types`" in line:
				pass
			else:
				raise Exception("Unknown object: {}".format(line))
	print(footer())


if __name__ == "__main__":
	main()