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


        db.session.add(Question("Does the sprint implement changes that affect and change CI/CD?", 1))
        db.session.add(Question("Does the sprint implement changes that affect authentication/authorization?", 1))
        db.session.add(Question("Does the sprint implement changes that affect session management?", 1))
        db.session.add(Question("Does the sprint implement changes that affect access control systems?", 1))
        db.session.add(Question("Does the sprint make use/implement an ORM framework? (object relational model)", 1))
        db.session.add(Question("Does the sprint implement functions that handle user supplied input? (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc)", 1))
        db.session.add(Question("Does the sprint implement functions that forward or redirect your users trough the application?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize wysiwyg editors?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize templating engines or single page apps such as (Angular, React)", 1))
        db.session.add(Question("Does the sprint implement functions that allow for SVG scriptable content to be uploaded/posted?", 1))
        db.session.add(Question("Does the sprint implement functions that reflect user supplied input on the side of the client?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize raw SQL queries?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize LDAP?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize OS commands?", 1))
        db.session.add(Question("Does the sprint implement functions that get/grabs files from the file system?", 1))
        db.session.add(Question("Does the sprint implement functions that parse or digests XML?", 1))
        db.session.add(Question("Does the sprint implement/change functions with native code (C, C++)", 1))
        db.session.add(Question("Does the sprint implement functions that deserializes objects (JSON, XML and YAML)", 1))
        db.session.add(Question("Does the sprint implement functions that process sensitive data?", 1))
        db.session.add(Question("Does the sprint imlement functions that require secure random values", 1))
        db.session.add(Question("Does the sprint implement functions that impact logging?", 1))
        db.session.add(Question("Does the sprint implement/changes TLS configuration?", 1))
        db.session.add(Question("Does the sprint implement functions that allow users to upload/download files?", 1))
        db.session.add(Question("Does the sprint implement functions that utilize GraphQL", 1))
        db.session.add(Question("Does the sprint implement functions that store sensitive information?", 1))
        db.session.add(Question("Does the sprint implement functions that allow users to send emails?", 1))
        db.session.add(Question("Is the application in need of an architectural review?", 1))
        db.session.add(Question("Is the application in need of a review of configurations and settings?", 1))
        db.session.add(Question("Are you building on an application that has API features?", 1))
        db.session.add(Question("Does this sprint introduce functions with critical business logic that needs to be reviewed?", 1))
        db.session.add(Question("Does the sprint introduce change/affect on password policies?", 1))
        db.session.add(Question("Does the sprint introduce changes that affect OTP?", 1))

        db.session.add(Question("Does the sprint implement changes that affect and change CI/CD?", 2))
        db.session.add(Question("Does the sprint implement changes that affect authentication/authorization?", 2))
        db.session.add(Question("Does the sprint implement changes that affect session management?", 2))
        db.session.add(Question("Does the sprint implement changes that affect access control systems?", 2))
        db.session.add(Question("Does the sprint make use/implement an ORM framework? (object relational model)", 2))
        db.session.add(Question("Does the sprint implement functions that handle user supplied input? (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc)", 2))
        db.session.add(Question("Does the sprint implement functions that forward or redirect your users trough the application?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize wysiwyg editors?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize templating engines or single page apps such as (Angular, React)", 2))
        db.session.add(Question("Does the sprint implement functions that allow for SVG scriptable content to be uploaded/posted?", 2))
        db.session.add(Question("Does the sprint implement functions that reflect user supplied input on the side of the client?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize raw SQL queries?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize LDAP?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize OS commands?", 2))
        db.session.add(Question("Does the sprint implement functions that get/grabs files from the file system?", 2))
        db.session.add(Question("Does the sprint implement functions that parse or digests XML?", 2))
        db.session.add(Question("Does the sprint implement/change functions with native code (C, C++)", 2))
        db.session.add(Question("Does the sprint implement functions that deserializes objects (JSON, XML and YAML)", 2))
        db.session.add(Question("Does the sprint implement functions that process sensitive data?", 2))
        db.session.add(Question("Does the sprint imlement functions that require secure random values", 2))
        db.session.add(Question("Does the sprint implement functions that impact logging?", 2))
        db.session.add(Question("Does the sprint implement/changes TLS configuration?", 2))
        db.session.add(Question("Does the sprint implement functions that allow users to upload/download files?", 2))
        db.session.add(Question("Does the sprint implement functions that utilize GraphQL", 2))
        db.session.add(Question("Does the sprint implement functions that store sensitive information?", 2))
        db.session.add(Question("Does the sprint implement functions that allow users to send emails?", 2))
        db.session.add(Question("Is the application in need of an architectural review?", 2))
        db.session.add(Question("Is the application in need of a review of configurations and settings?", 2))
        db.session.add(Question("Are you building on an application that has API features?", 2))
        db.session.add(Question("Does this sprint introduce functions with critical business logic that needs to be reviewed?", 2))
        db.session.add(Question("Does the sprint introduce change/affect on password policies?", 2))
        db.session.add(Question("Does the sprint introduce changes that affect OTP?", 2))
"""


def footer():
	return """
        db.session.commit()
        return True

    except:
        db.session.rollback()
        return False
"""

def output(line=''):
	print("        " + line)

def main():

	print(header())
	filename = sys.argv[1] if len(sys.argv)>1 else "schema.sql" 
	f = open(filename, "r")

	for line in f:
		if "INSERT" in line:
			if "checklists_kb" in line:

				d = line2dict(line)
				#print(d)
				output("c = ChecklistKB('{}', '{}', {}, {});".format(
					d['checklistID'], d['content'], d['cwe'], True if d['include_always'].lower()=='true' else False))
				output("c.question_id = {}".format(d['question_ID']))
				output("c.kb_id = {}".format(d['kbID']))
				output("c.checklist_type = {}".format(d['checklist_type']))
				output("db.session.add(c)")
				output()
			elif "`lab_items`" in line:

				d = line2dict(line)
				output("db.session.add(LabItem('{}','{}', {}))".format(d['title'],d['link'],d['level']))

			elif "`questions`" in line:
				d = line2dict(line)
				output("db.session.add(Question({}, '{}'))".format(d['checklist_type'],d['question']))


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