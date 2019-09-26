

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
        
        db.session.add(ChecklistType(name='Architecture, Design and Threat Modeling Requirements', description='Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a much better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.', visibility=1))
        db.session.add(ChecklistType(name='Authentication Verification Requirements', description='Authentication is the act of establishing, or confirming, someone (or something) as authentic and that claims made by a person or about a device are correct, resistant to impersonation, and prevent recovery or interception of passwords.', visibility=1))
        db.session.add(ChecklistType(name='Session Management Verification Requirements', description='One of the core components of any web-based application or stateful API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.', visibility=1))
        db.session.add(ChecklistType(name='Access Control Verification Requirements', description='Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high level requirements:• Persons accessing resources hold valid credentials to do so.* Users are associated with a well-defined set of roles and privileges.• Role and permission metadata is protected from replay or tampering.', visibility=1))
        db.session.add(ChecklistType(name='Validation, Sanitization and Encoding Verification Requirements', description='The most common web application security weakness is the failure to properly validate input coming from the client or the environment before directly using it without any output encoding. This weakness leads to almost all of the significant vulnerabilities in web applications, such as Cross-Site Scripting (XSS), SQL injection, interpreter injection, locale/Unicode attacks, file system attacks, and buffer overflows.', visibility=1))
        db.session.add(ChecklistType(name='Stored Cryptography Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • All cryptographic modules fail in a secure manner and that errors are handled correctly. • A suitable random number generator is used. • Access to keys is securely managed. V6.1 Data Classification', visibility=1))
        db.session.add(ChecklistType(name='Error Handling and Logging Verification Requirements', description='The primary objective of error handling and logging is to provide useful information for the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.', visibility=1))
        db.session.add(ChecklistType(name='Data Protection Verification Requirements', description='There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.', visibility=1))
        db.session.add(ChecklistType(name='Communications Verification Requirements', description='Leading industry advice on secure TLS configuration changes frequently, often due to catastrophic breaks in existing algorithms and ciphers. Always use the most recent versions of TLS configuration review tools (such as SSLyze or other TLS scanners) to configure the preferred order and algorithm selection. Configuration should be periodically checked to ensure that secure communications configuration is always present and effective.', visibility=1))
        db.session.add(ChecklistType(name='Malicious Code Verification Requirements', description='Finding malicious code is proof of the negative, which is impossible to completely validate. Best efforts should be undertaken to ensure that the code has no inherent malicious code or unwanted functionality.', visibility=1))
        db.session.add(ChecklistType(name='Business Logic Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • The business logic flow is sequential, processed in order, and cannot be bypassed. • Business logic includes limits to detect and prevent automated attacks, such as continuous small funds transfers, or adding a million friends one at a time, and so on. • High value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, repudiation, information disclosure, and elevation of privilege attacks.', visibility=1))
        db.session.add(ChecklistType(name='File and Resources Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • Untrusted file data should be handled accordingly and in a secure manner. • Untrusted file data obtained from untrusted sources are stored outside the web root and with limited permissions.', visibility=1))
        db.session.add(ChecklistType(name='API and Web Service Verification Requirements', description='Ensure that a verified application that uses trusted service layer APIs (commonly using JSON or XML or GraphQL) has: • Adequate authentication, session management and authorization of all web services. • Input validation of all parameters that transit from a lower to higher trust level. • Effective security controls for all API types, including cloud and Serverless API Please read this chapter in combination with all other chapters at this same level; we no longer duplicate authentication or API session management concerns.', visibility=1))
        db.session.add(ChecklistType(name='Configuration Verification Requirements', description='Ensure that a verified application has: • A secure, repeatable, automatable build environment. • Hardened third party library, dependency and configuration management such that out of date or insecure components are not included by the application. • A secure-by-default configuration, such that administrators and users have to weaken the default security posture. Configuration of the application out of the box should be safe to be on the Internet, which means a safe out of the box configuration.', visibility=1))
        db.session.commit()
        
        
        '''
        Questionaire for ASVS
        '''

        #1 -- 1.1
        q = Question('Secure Software Development Lifecycle Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #2 -- 1.2
        q = Question('Authentication Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #3 -- 1.4
        q = Question('Access Control Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #4 -- 1.5
        q = Question('Input and Output Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #5 -- 1.6
        q = Question('Cryptographic Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #6 -- 1.7
        q = Question('Errors, Logging and Auditing Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #7 -- 1.8
        q = Question('Data Protection and Privacy Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #8 -- 1.9
        q = Question('Communications Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #9 -- 1.10
        q = Question('Malicious Software Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #10 -- 2.1
        q = Question('Password security requirements', 2)
        db.session.add(q)
        db.session.commit()

        #11 -- 2.2
        q = Question('General Authenticator Requirements (brute force, authenticator types, 2FA)', 2)
        db.session.add(q)
        db.session.commit()
        
        #12 -- 2.3
        q = Question('Authenticator Lifecycle Requirements (activation codes, FIDO tokens)', 2)
        db.session.add(q)
        db.session.commit()
        
        #13 -- 2.4
        q = Question('Credential Storage Requirements (salting/stretching, pbkdf2, bcrypt)', 2)
        db.session.add(q)
        db.session.commit()
        
        #14 -- 2.5
        q = Question('Credential Recovery Requirements (secret questions, default accounts, recovery tokens)', 2)
        db.session.add(q)
        db.session.commit()
        
        #15 -- 2.6
        q = Question('Look-up Secret Verifier Requirements (revocation, token randomness)', 2)
        db.session.add(q)
        db.session.commit()
        
        #16 -- 2.7 
        q = Question('Out of Band Verifier Requirements (Reset links, SMS tokens)', 2)
        db.session.add(q)
        db.session.commit()
        
        #17 -- 2.8 
        q = Question('Single or Multi Factor One Time Verifier Requirements', 2)
        db.session.add(q)
        db.session.commit()

        #18 -- 2.9
        q = Question('Cryptographic Software and Devices Verifier Requirements (TPM, HSM)', 2)
        db.session.add(q)
        db.session.commit()

        #19 -- 2.10
        q = Question('Service Authentication Requirements', 2)
        db.session.add(q)
        db.session.commit()

        #20 -- 3.1
        q = Question('Fundamental Session Management Requirements', 3)
        db.session.add(q)
        db.session.commit()

        #21 -- 3.2
        q = Question('Session Binding Requirements', 3)
        db.session.add(q)
        db.session.commit()

        #22 -- 3.3
        q = Question('Session Logout and Timeout Requirements', 3)
        db.session.add(q)
        db.session.commit()

        #23 -- 3.4
        q = Question('Cookie-based Session Management', 3)
        db.session.add(q)
        db.session.commit()

        #24 -- 3.5
        q = Question('Token-based Session Management', 3)
        db.session.add(q)
        db.session.commit()

        #25 -- 3.7 is only 1 item that we should include always
        q = Question('Defenses Against Session Management Exploits', 3)
        db.session.add(q)
        db.session.commit()

        #26 -- 4.1
        q = Question('General Access Control Design', 4)
        db.session.add(q)
        db.session.commit()

        #27 -- 4.2 include always both items
        q = Question('Operation Level Access Control', 4)
        db.session.add(q)
        db.session.commit()

        #28 -- 4.3 include always both items
        q = Question('Other Access Control Considerations', 4)
        db.session.add(q)
        db.session.commit()

        #29 -- 5.1
        q = Question('Input Validation Requirements (parameter binding, url redirects, structure checking credit cards, phone numbers, etc, http request methods)', 5)
        db.session.add(q)
        db.session.commit()

        #30 -- 5.2
        q = Question('Sanitization and Sandboxing Requirements (type/length checking, SSRF, wysiwyg/markdown/bbcode/etc)', 5)
        db.session.add(q)
        db.session.commit()

        #31 -- 5.3 
        q = Question('Outputting user supplied input on the client side (browser)', 5)
        db.session.add(q)
        db.session.commit()

        #32 -- 5.3 
        q = Question('Getting files from the local file system', 5)
        db.session.add(q)
        db.session.commit()

        #33 -- 5.3 
        q = Question('Using data selection or database queries (e.g. SQL, HQL, ORM, NoSQL)', 5)
        db.session.add(q)
        db.session.commit()

        #34 -- 5.3 
        q = Question('Using LDAP', 5)
        db.session.add(q)
        db.session.commit()

        #35 -- 5.3 
        q = Question('Using functions that perfom OS commands', 5)
        db.session.add(q)
        db.session.commit()

        #36 --  5.3
        q = Question('Using XML/Xpath?', 5)
        db.session.add(q)
        db.session.commit()

        #37 -- 5.5
        q = Question('Are you deserializng objects (json, xml, bytestreams, yaml, etc)', 5)
        db.session.add(q)
        db.session.commit()

        #38 -- 6.1 
        q = Question('Are you aware on what type of data classifies to be stored encrypted?', 6)
        db.session.add(q)
        db.session.commit()

        #39 -- 6.2
        q = Question('Are cryptgrapic functions used in the application on par with the latest known to be secure standards?', 6)
        db.session.add(q)
        db.session.commit()

        #40 -- 6.3
        q = Question('Are secure random values or UUIDs that are used in the application tested for sufficient entropy?', 6)
        db.session.add(q)
        db.session.commit()

        #41 -- 6.4
        q = Question('Are secrets managed in a key-vault?', 6)
        db.session.add(q)
        db.session.commit()

        #42 -- 7.1
        q = Question('Is the application logging sensitive information? (credentials, payment details, tokens, etc)', 7)
        db.session.add(q)
        db.session.commit()

        #43 -- 7.2
        q = Question('Do logs exist for authentication/ access control decisions?', 7)
        db.session.add(q)
        db.session.commit()

        #44 -- 7.3
        q = Question('Are logs protected for un-authorized access, injection flaws(also in viewing software), and are timestamps synced to match respective timezones', 7)
        db.session.add(q)
        db.session.commit()

        #45 -- 7.4
        q = Question('Are errors on the application gracefully handled and show non generic error messages?', 7)
        db.session.add(q)
        db.session.commit()

        #46 -- 8.1
        q = Question('General data protection requirements', 8)
        db.session.add(q)
        db.session.commit()

        #47 -- 8.2
        q = Question('Client side data protection requirements (localstorage, session storage, cookies, etc)', 8)
        db.session.add(q)
        db.session.commit()

        #48 -- 8.3
        q = Question('requirements how to handle sensitive private data (personal identifiable infomation)', 8)
        db.session.add(q)
        db.session.commit()

        #49 -- 9.1
        q = Question('Communication security requirements', 9)
        db.session.add(q)
        db.session.commit()

        #50 -- 9.2
        q = Question('Server security communication requirements', 9)
        db.session.add(q)
        db.session.commit()

        #51 -- 10.1
        q = Question('Code integrity controls', 10)
        db.session.add(q)
        db.session.commit()

        #52 -- 10.2
        q = Question('Malicious code search', 10)
        db.session.add(q)
        db.session.commit()

        #53 -- 10.3
        q = Question('Deployed application integrity controls', 10)
        db.session.add(q)
        db.session.commit()

        #54 -- 11.1
        q = Question('Business Logic Security Requirements', 11)
        db.session.add(q)
        db.session.commit()

        #55 -- 12.1
        q = Question('File Upload Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #56 -- 12.2
        q = Question('File Integrity Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #57 -- 12.3
        q = Question('File execution Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #58 -- 12.4
        q = Question('File Storage Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #59 -- 12.5
        q = Question('File download Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #60 -- 12.6
        q = Question('SSRF Protection Requirements', 12)
        db.session.add(q)
        db.session.commit()

        #61 -- 13.1
        q = Question('Generic Web Service Security Verification Requirements', 13)
        db.session.add(q)
        db.session.commit()

        #62 -- 13.2
        q = Question('RESTful Web Service Verification Requirements', 13)
        db.session.add(q)
        db.session.commit()

        #63 -- 13.3
        q = Question('SOAP Web Service Verification Requirements', 13)
        db.session.add(q)
        db.session.commit()

        #64 -- 13.4
        q = Question('GraphQL and other Web Service Data Layer Security Requirements', 13)
        db.session.add(q)
        db.session.commit()

        #65 -- 14.1
        q = Question('Build pipeline configuration', 14)
        db.session.add(q)
        db.session.commit()
        
        #66 -- 14.2
        q = Question('Dependency checking', 14)
        db.session.add(q)
        db.session.commit()

        #67 -- 14.3
        q = Question('Unintended Security Disclosure Requirements', 14)
        db.session.add(q)
        db.session.commit()

        #68 -- 14.4
        q = Question('HTTP Security Headers Requirements', 14)
        db.session.add(q)
        db.session.commit()

        #69 -- 14.5
        q = Question('Validate HTTP Request Header Requirements', 14)
        db.session.add(q)
        db.session.commit()
        
        #70 -- 1.11 
        q = Question('Business Logic Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        #71 -- 1.12
        q = Question('Secure File Upload Architectural Requirementss', 1)
        db.session.add(q)
        db.session.commit()

        #72 -- 1.14
        q = Question('Configuration Architectural Requirements', 1)
        db.session.add(q)
        db.session.commit()

        c = ChecklistKB('1.0', 'Architecture, Design and Threat Modeling Requirements', 1, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.1', 'Verify the use of a secure software development lifecycle that addresses security in all stages of development.', 1, False, None, 2);
        c.question_id = 1
        c.kb_id = 272
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.2', 'Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.', 1, True, 1053, 2);
        c.question_id = 1
        c.kb_id = 164
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.3', 'Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else\s profile', 1, True, 1110, 2);
        c.question_id = 1
        c.kb_id = 273
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.4', 'Verify documentation and justification of all the application\s trust boundaries, components, and significant data flows.', 1, False, 1059,2);
        c.question_id = 1
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.5', 'Verify definition and security analysis of the application\s high-level architecture and all connected remote services. ', 1, False, 1059, 2);
        c.question_id = 1
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.6', 'Verify implementation of centralized, simple (economy of design); vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls.', 1, True, 637, 2);
        c.question_id = 1
        c.kb_id = 184
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.7', 'Verify availability of a secure coding checklist, security requirements, guideline, or policy to all developers and testers.', 1, False, 637, 2);
        c.question_id = 1
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.1', 'Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers.', 1, False, 250, 2);
        c.question_id = 2
        c.kb_id = 126
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.2', 'Verify that communications between application components, including APIs, middleware and data layers, are authenticated. Components should have the least necessary privileges needed.', 1, False, 306, 2);
        c.question_id = 2
        c.kb_id = 126
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.3', 'Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches.', 1, False, 306, 2);
        c.question_id = 2
        c.kb_id = 259
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.4', 'Verify that all authentication pathways and identity management APIs implement consistent authentication security control strength, such that there are no weaker alternatives per the risk of the application.', 1, False, 306, 2);
        c.question_id = 2
        c.kb_id = 85
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.1', 'Verify that trusted enforcement points such as at access control gateways, servers, and serverless functions enforce access controls. Never enforce access controls on the client.', 1, False, 602, 2);
        c.question_id = 3
        c.kb_id = 240
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.2', 'Verify that the chosen access control solution is flexible enough to meet the application\s needs.', 1, False, 284, 2);
        c.question_id = 3
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.3', 'Verify enforcement of the principle of least privilege in functions, data files, URLs, controllers, services, and other resources. This implies protection against spoofing and elevation of privilege.', 1, False, 272, 2);
        c.question_id = 3
        c.kb_id = 126
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.4', 'Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths.', 1, False, 284, 2);
        c.question_id = 3
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.5', 'Verify that attribute or feature-based access control is used whereby the code checks the user\s authorization for a feature/data item rather than just their role.', 1, False, 275, 2);
        c.question_id = 3
        c.kb_id = 274
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.1', 'Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance.', 1, False, 1029, 2);
        c.question_id = 4
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.2', 'Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection.', 1, False, 502, 2);
        c.question_id = 4
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.3', 'Verify that input validation is enforced on a trusted service layer.', 1, False, 602, 2);
        c.question_id = 4
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.4', 'Verify that output encoding occurs close to or by the interpreter for which it is intended.', 1, False, 116, 2);
        c.question_id = 4
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.1', 'Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57.', 1, False, 320, 2);
        c.question_id = 5
        c.kb_id = 275
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.2', 'Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives.', 1, True, 320, 2);
        c.question_id = 5
        c.kb_id = 276
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.3', 'Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data.', 1, False, 320, 2);
        c.question_id = 5
        c.kb_id = 204
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.4', 'Verify that symmetric keys, passwords, or API secrets generated by or shared with clients are used only in protecting low risk secrets, such as encrypting local storage, or temporary ephemeral uses such as parameter obfuscation. Sharing secrets with clients is clear-text equivalent and architecturally should be treated as such.', 1, False, 320, 2);
        c.question_id = 5
        c.kb_id = 277
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.7.1', 'Verify that a common logging format and approach is used across the system.', 1, False, 1009, 2);
        c.question_id = 6
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.7.2', 'Verify that logs are securely transmitted to a preferably remote system for analysis, detection, alerting, and escalation.', 1, False, None, 2);
        c.question_id = 6
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.8.1', 'Verify that all sensitive data is identified and classified into protection levels.', 1, False, None, 2);
        c.question_id = 7
        c.kb_id = 278
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.8.2', 'Verify that all protection levels have an associated set of protection requirements, such as encryption requirements, integrity requirements, retention, privacy and other confidentiality requirements, and that these are applied in the architecture.', 1, False, None, 2);
        c.question_id = 7
        c.kb_id = 278
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.9.1', 'Verify the application encrypts communications between components, particularly when these components are in different containers, systems, sites, or cloud providers.', 1, False, 319, 2);
        c.question_id = 8
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.9.2', 'Verify that application components verify the authenticity of each side in a communication link to prevent person-in-the-middle attacks. For example, application components should validate TLS certificates and chains.', 1, False, 295, 2);
        c.question_id = 8
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.10.1', 'Verify that a source code control system is in use, with procedures to ensure that check-ins are accompanied by issues or change tickets. The source code control system should have access control and identifiable users to allow traceability of any changes.', 1, False, 284, 2);
        c.question_id = 9
        c.kb_id = 279
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.11.1', 'Verify the definition and documentation of all application components in terms of the business or security functions they provide.', 1, False, 1059, 2);
        c.question_id = 70
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.11.2', 'Verify that all high-value business logic flows, including authentication, session management and access control, do not share unsynchronized state.', 1, False, 362, 2);
        c.question_id = 70
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('1.11.3', 'Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.', 1, False, 362, 3);
        c.question_id = 70
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.12.1', 'Verify that user-uploaded files are stored outside of the web root.', 1, False, 552, 2);
        c.question_id = 71
        c.kb_id = 227
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.12.2', 'Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. Implement a suitable content security policy to reduce the risk from XSS vectors or other attacks from the uploaded file.', 1, False, 646, 2);
        c.question_id = 71
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.1', 'Verify the segregation of components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms.', 1, False, 923, 2);
        c.question_id = 72
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.2', 'Verify that if deploying binaries to untrusted devices makes use of binary signatures, trusted connections, and verified endpoints.', 1, False, 494, 2);
        c.question_id = 72
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.3', 'Verify that the build pipeline warns of out-of-date or insecure components and takes appropriate actions.', 1, False, 1104, 2);
        c.question_id = 72
        c.kb_id = 280
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.4', 'Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts.', 1, False, None, 2);
        c.question_id = 72
        c.kb_id = 281
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.5', 'Verify that application deployments adequately sandbox, containerize and/or isolate at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization.', 1, False, 265, 2);
        c.question_id = 72
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.6', 'Verify the application does not use unsupported, insecure, or deprecated client-side technologies such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets.', 1, False, 477, 2);
        c.question_id = 72
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.0', 'Authentication Verification Requirements', 2, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.1.1', 'Verify that user set passwords are at least 12 characters in length. (C6)', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.2', 'Verify that passwords 64 characters or longer are permitted.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.3', 'Verify that passwords can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.4', 'Verify that Unicode characters are permitted in passwords. A single Unicode code point is considered a character, so 12 emoji or 64 kanji characters should be valid and permitted.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.5', 'Verify users can change their password.', 2, False, 620, 1)
        c.question_id = 10
        c.kb_id = 1343
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.6', 'Verify that password change functionality requires the user\s current and new password.', 2, False, 620, 1)
        c.question_id = 10
        c.kb_id = 32
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.7', 'Verify that passwords submitted during account registration, login, and password change are checked against a set of breached passwords either locally (such as the top 1,000 or 10,000 most common passwords which match the system\s password policy) or using an external API. If using an API a zero knowledge proof or other mechanism should be used to ensure that the plain text password is not sent or used in verifying the breach status of the password. If the password is breached, the application must require the user to set a new non-breached password.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 1345
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.8', 'Verify that a password strength meter is provided to help users set a stronger password.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 1344
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.9', 'Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.10', 'Verify that there are no periodic credential rotation or password history requirements.', 2, False, 263, 1)
        c.question_id = 10
        c.kb_id = 295
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.11', 'Verify that "paste" functionality, browser password helpers, and external password managers are permitted.', 2, False, 521,1)
        c.question_id = 10
        c.kb_id = 59
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.12', 'Verify that the user can choose to either temporarily view the entire masked password, or temporarily view the last typed character of the password on platforms that do not have this as native functionality.', 2, False, 521, 1)
        c.question_id = 10
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.1', 'Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. Such controls include blocking the most common breached passwords, soft lockouts, rate limiting, CAPTCHA, ever increasing delays between attempts, IP address restrictions, or risk-based restrictions such as location, first login on a device, recent attempts to unlock the account, or similar. Verify that no more than 100 failed attempts per hour is possible on a single account.', 2, False, 307, 1)
        c.question_id = 11
        c.kb_id = 29
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.2', 'Verify that the use of weak authenticators (such as SMS and email) is limited to secondary verification and transaction approval and not as a replacement for more secure authentication methods. Verify that stronger methods are offered before weak methods, users are aware of the risks, or that proper measures are in place to limit the risks of account compromise.', 2, False, 304, 1)
        c.question_id = 11
        c.kb_id = 115
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.3', 'Verify that secure notifications are sent to users after updates to authentication details, such as credential resets, email or address changes, logging in from unknown or risky locations. The use of push notifications - rather than SMS or email - is preferred, but in the absence of push notifications, SMS or email is acceptable as long as no sensitive information is disclosed in the notification.', 2, False, 620, 1)
        c.question_id = 11
        c.kb_id = 296
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.4', 'Verify impersonation resistance against phishing, such as the use of multi-factor authentication, cryptographic devices with intent (such as connected keys with a push to authenticate), or at higher AAL levels, client-side certificates.', 2, False, 308, 3)
        c.question_id = 11
        c.kb_id = 231
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.5', 'Verify that where a credential service provider (CSP) and the application verifying authentication are separated, mutually authenticated TLS is in place between the two endpoints.', 2, False, 319, 3)
        c.question_id = 11
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.6', 'Verify replay resistance through the mandated use of OTP devices, cryptographic authenticators, or lookup codes.', 2, False, 308, 3)
        c.question_id = 11
        c.kb_id = 290
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.7', 'Verify intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a button press on a FIDO hardware key.', 2, False, 308, 3)
        c.question_id = 11
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.1', 'Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers, and expire after a short period of time. These initial secrets must not be permitted to become the long term password.', 2, False, 330, 1)
        c.question_id = 12
        c.kb_id = 214
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.2', 'Verify that enrollment and use of subscriber-provided authentication devices are supported, such as a U2F or FIDO tokens.', 2, False, 308, 2)
        c.question_id = 12
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.3', 'Verify that renewal instructions are sent with sufficient time to renew time bound authenticators.', 2, False, 287, 2)
        c.question_id = 12
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.1', 'Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one- way key derivation or password hashing function. Key derivation and password hashing functions take a password, a salt, and a cost factor as inputs when generating a password hash.', 2, False, 916, 2)
        c.question_id = 13
        c.kb_id = 51
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.2', 'Verify that the salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored.', 2, False, 916, 2)
        c.question_id = 13
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.3', 'Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations.', 2, False, 916, 2)
        c.question_id = 13
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.4', 'Verify that if bcrypt is used, the work factor SHOULD be as large as verification server performance will allow, typically at least 13', 2, False, 916, 2)
        c.question_id = 13
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.4.5', 'Verify that an additional iteration of a key derivation function is performed, using a salt value that is secret and known only to the verifier. Generate the salt value using an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module).', 2, False, 916, 2)
        c.question_id = 13
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.1', 'Verify that a system generated initial activation or recovery secret is not sent in clear text to the user.', 2, False, 640, 1)
        c.question_id = 14
        c.kb_id = 243
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.2', 'Verify password hints or knowledge-based authentication (so-called "secret questions") are not present.', 2, False, 640, 1)
        c.question_id = 14
        c.kb_id = 87
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.3', 'Verify password credential recovery does not reveal the current password in any way.', 2, False, 640, 1)
        c.question_id = 14
        c.kb_id = 243
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.4', 'Verify shared or default accounts are not present (e.g. "root", "admin", or "sa").', 2, False, 16, 1)
        c.question_id = 14
        c.kb_id = 63
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.5', 'Verify that if an authentication factor is changed or replaced, that the user is notified of this event.', 2, False, 304, 1)
        c.question_id = 14
        c.kb_id = 296
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.6', 'Verify forgotten password, and other recovery paths use a secure recovery mechanism, such as TOTP or other soft token, mobile push, or another offline recovery mechanism. ', 2, False, 640, 1)
        c.question_id = 14
        c.kb_id = 115
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.5.7', 'Verify that if OTP or multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment.', 2, False, 308, 2)
        c.question_id = 14
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.1', 'Verify that lookup secrets can be used only once.', 2, False, 308, 2)
        c.question_id = 15
        c.kb_id = 290
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.2', 'Verify that lookup secrets have sufficient randomness (112 bits of entropy), or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash', 2, False, 330, 2)
        c.question_id = 15
        c.kb_id = 304
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.3', 'Verify that lookup secrets are resistant to offline attacks, such as predictable values.', 2, False, 310, 2)
        c.question_id = 15
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.1', 'Verify that clear text out of band (NIST "restricted") authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first.', 2, False, 287, 1)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.2', 'Verify that the out of band verifier expires out of band authentication requests, codes, or tokens after 10 minutes.', 2, False, 287, 1)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.3', 'Verify that the out of band verifier authentication requests, codes, or tokens are only usable once, and only for the original authentication request.', 2, False, 287, 1)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.4', 'Verify that the out of band authenticator and verifier communicates over a secure independent channel.', 2, False, 523, 1)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.5', 'Verify that the out of band verifier retains only a hashed version of the authentication code.', 2, False, 256, 2)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.6', 'Verify that the initial authentication code is generated by a secure random number generator, containing at least 20 bits of entropy (typically a six digital random number is sufficient).', 2, False, 310, 2)
        c.question_id = 16
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.8.1', 'Verify that time-based OTPs have a defined lifetime before expiring.', 2, False, 613, 1)
        c.question_id = 17
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.8.2', 'Verify that symmetric keys used to verify submitted OTPs are highly protected, such as by using a hardware security module or secure operating system based key storage.', 2, False, 320, 2)
        c.question_id = 17
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.3', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', 2, False, 326, 2)
        c.question_id = 17
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.4', 'Verify that time-based OTP can be used only once within the validity period.', 2, False, 287, 2)
        c.question_id = 17
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.5', 'Verify that if a time-based multi factor OTP token is re-used during the validity period, it is logged and rejected with secure notifications being sent to the holder of the device.', 2, False, 287, 2)
        c.question_id = 17
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.6', 'Verify physical single factor OTP generator can be revoked in case of theft or other loss. Ensure that revocation is immediately effective across logged in sessions, regardless of location.', 2, False, 613, 2)
        c.question_id = 17 
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.7', 'Verify that biometric authenticators are limited to use only as o ✓ 308 5.2.3 secondary factors in conjunction with either something you have and something you know.', 2, False, 308, 3)
        c.question_id = 17 
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.1', 'Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a TPM or HSM, or an OS service that can use this secure storage.', 2, False, 320, 2)
        c.question_id = 18
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.2', 'Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device.', 2, False, 330, 2)
        c.question_id = 18
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.3', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', 2, False, 327, 2)
        c.question_id = 18
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.1', 'Verify that integration secrets do not rely on unchanging passwords, such as API keys or shared privileged accounts.', 2, False, 287, 2)
        c.question_id = 19
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.2', 'Verify that if passwords are required, the credentials are not a default account', 2, False, 255, 2)
        c.question_id = 19
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.3', 'Verify that passwords are stored with sufficient protection to prevent offline recovery attacks, including local system access.', 2, False, 522, 2)
        c.question_id = 19
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.4', 'Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware trusted platform module (TPM), or a hardware security module (L3) is recommended for password storage.', 2, False, 798, 2)
        c.question_id = 19
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.0', 'Session Management Verification Requirements', 3, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.1.1', 'Verify the application never reveals session tokens in URL parameters or error messages.', 3, False, 598, 1)
        c.question_id = 20
        c.kb_id = 91
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.1', 'Verify the application generates a new session token on user authentication.', 3, False, 384, 1)
        c.question_id = 21
        c.kb_id = 58
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.2', 'Verify that session tokens possess at least 64 bits of entropy.', 3, False, 331, 1)
        c.question_id = 21
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.3', 'Verify the application only stores session tokens in the browser using secure methods such as appropriately secured cookies (see section 3.4) or HTML 5 session storage.', 3, False, 539, 1)
        c.question_id = 21
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.2.4', 'Verify that session token are generated using approved cryptographic algorithms', 3, False, 331, 2)
        c.question_id = 21
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.1', 'Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties.', 3, False, 613, 1)
        c.question_id = 22
        c.kb_id = 57
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.2', 'If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period.', 3, False, 613, 1)
        c.question_id = 22
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.3', 'Verify that the application terminates all other active sessions after a successful password change, and that this is effective across the application, federated login (if present); and any relying parties.', 3, False, 613, 2)
        c.question_id = 22
        c.kb_id = 254
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.4', 'Verify that users are able to view and log out of any or all currently active sessions and devices.', 3, False, 613, 2)
        c.question_id = 22
        c.kb_id = 188
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.1', 'Verify that cookie-based session tokens have the \Secure\ attribute set.', 3, False, 614, 1)
        c.question_id = 23
        c.kb_id = 38
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.2', 'Verify that cookie-based session tokens have the \HttpOnly\ attribute set.', 3, False, 1004, 1)
        c.question_id = 23
        c.kb_id = 39
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.3', 'Verify that cookie-based session tokens utilize the \SameSite\ attribute to limit exposure to cross-site request forgery attacks.', 3, False, 16, 1)
        c.question_id = 23
        c.kb_id = 291
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.4', 'Verify that cookie-based session tokens use "__Host-" prefix (see references) to provide session cookie confidentiality.', 3, False, 16, 1)
        c.question_id = 23
        c.kb_id = 292
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.5', 'Verify that if the application is published under a domain name with other applications that set or use session cookies that might override or disclose the session cookies, set the path attribute in cookie-based session tokens using the most precise path possible.', 3, False, 16, 1)
        c.question_id = 23
        c.kb_id = 158
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.1', 'Verify the application does not treat OAuth and refresh tokens — on their own — as the presence of the subscriber and allows users to terminate trust relationships with linked applications.', 3, False, 290, 2)
        c.question_id = 24
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.2', 'Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations.', 3, False, 798, 2)
        c.question_id = 24
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.3', 'Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks.', 3, False, 345, 2)
        c.question_id = 24
        c.kb_id = 297
        db.session.add(c)
        db.session.commit()
        
        '''
        c = ChecklistKB('3.6.1', 'Verify that relying parties specify the maximum authentication time to CSPs and that CSPs re-authenticate the subscriber if they haven't used a session within that period.', 3, False, 16, 3)
        c.question_id = 23
        c.kb_id = 158
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.6.2', 'Verify that CSPs inform relying parties of the last authentication event, to allow RPs to determine if they need to re-authenticate the user.', 1, False, 16, 3)
        c.question_id = 23
        c.kb_id = 158
        db.session.add(c)
        db.session.commit()
        '''

        c = ChecklistKB('3.7.1', 'Verify the application ensures a valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications.', 3, False, 778, 1)
        c.question_id = 25
        c.kb_id = 233
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.0', 'Access Control Verification Requirements', 4, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.1', 'Verify that the application enforces access control rules on a trusted service layer, especially if client-side access control is present and could be bypassed.', 4, False, 602, 1)
        c.question_id = 26
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.2', 'Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized.', 4, False, 639, 1)
        c.question_id = 26
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.3', 'Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', 4, False, 285, 1)
        c.question_id = 26
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.4', 'Verify that the principle of deny by default exists whereby new users/roles start with minimal or no permissions and users/roles do not receive access to new features until access is explicitly assigned. ', 4, False, 276, 1)
        c.question_id = 26
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.5', 'Verify that access controls fail securely including when an exception occurs.', 4, False, 285, 1)
        c.question_id = 26
        c.kb_id = 114
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.2.1', 'Verify that sensitive data and APIs are protected against direct object attacks targeting creation, reading, updating and deletion of records, such as creating or updating someone else\s record, viewing everyone\s records, or deleting all records.', 4, False, 639,1 )
        c.question_id = 27
        c.kb_id = 268
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.2.2', 'Verify that the application or framework enforces a strong anti-CSRF mechanism to protect authenticated functionality, and effective anti-automation or anti-CSRF protects unauthenticated functionality.', 4, False, 352, 1)
        c.question_id = 27
        c.kb_id = 5
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.1', 'Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use.', 4, False, 419, 1)
        c.question_id = 28
        c.kb_id = 231
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.2', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', 4, False, 548, 1)
        c.question_id = 28
        c.kb_id = 61
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.3', 'Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud.', 4, False, 732, 1)
        c.question_id = 28
        c.kb_id = 111
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.0', 'Validation, Sanitization and Encoding Verification Requirements', 5, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.1', 'Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, or environment variables).', 5, False, 235, 1)
        c.question_id = 29
        c.kb_id = 71
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.2', 'Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar.', 5, False, 915, 1)
        c.question_id = 29
        c.kb_id = 147
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.3', 'Verify that all input (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc) is validated using positive validation (whitelisting)', 5, False, 20, 1)
        c.question_id = 29
        c.kb_id = 167
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.4', 'Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as checking that suburb and zip/postcode match).', 5, False, 20, 1)
        c.question_id = 29
        c.kb_id = 234
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.5', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', 5, False, 601, 1)
        c.question_id = 29
        c.kb_id = 67
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.1', 'Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature.', 5, False, 116, 1)
        c.question_id = 30
        c.kb_id = 180
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.2', 'Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length.', 5, False, 138, 1)
        c.question_id = 30
        c.kb_id = 269
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.3', 'Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection.', 5, False, 147, 1)
        c.question_id = 30
        c.kb_id = 270
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.4', 'Verify that the application avoids the use of eval() or other dynamic code execution features. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed.', 5, False, 95, 1)
        c.question_id = 30
        c.kb_id = 4
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.5', 'Verify that the application protects against template injection attacks by ensuring that any user input being included is sanitized or sandboxed.', 5, False, 94, 1)
        c.question_id = 30
        c.kb_id = 267
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.6', 'Verify that the application protects against SSRF attacks, by validating or sanitizing untrusted data or HTTP file metadata, such as filenames and URL input fields, use whitelisting of protocols, domains, paths and ports.', 5, False, 918, 1)
        c.question_id = 30
        c.kb_id = 262
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.7', 'Verify that the application sanitizes, disables, or sandboxes user-supplied SVG scriptable content, especially as they relate to XSS resulting from inline scripts, and foreignObject.', 5, False, 159, 1)
        c.question_id = 30
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.8', 'Verify that the application sanitizes, disables, or sandboxes user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar.', 5, False, 94, 1)
        c.question_id = 30
        c.kb_id = 289
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.1', 'Verify that output encoding is relevant for the interpreter and context required. For example, use encoders specifically for HTML values, HTML attributes, JavaScript, URL Parameters, HTTP headers, SMTP, and others as the context requires, especially from untrusted inputs (e.g. names with Unicode or apostrophes, such as bla or OHara).', 5, False, 116, 1)
        c.question_id = 31
        c.kb_id = 269
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.2', 'Verify that output encoding preserves the user\s chosen character set and locale, such that any Unicode character point is valid and safely handled.', 5, False, 176, 1)
        c.question_id = 31
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.3', 'Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS.', 5, False, 79, 1)
        c.question_id = 31
        c.kb_id = 3
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.4', 'Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from database injection attacks.', 5, False, 89, 1)
        c.question_id = 33
        c.kb_id = 46
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.5', 'Verify that where parameterized or safer mechanisms are not present, context-specific output encoding is used to protect against injection attacks, such as the use of SQL escaping to protect against SQL injection.', 5, False, 89, 1)
        c.question_id = 33
        c.kb_id = 269
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.6', 'Verify that the application projects against JavaScript or JSON injection attacks, including for eval attacks, remote JavaScript includes, CSP bypasses, DOM XSS, and JavaScript expression evaluation.', 5, False, 830, 1)
        c.question_id = 31
        c.kb_id = 181
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.7', 'Verify that the application protects against LDAP Injection vulnerabilities, or that specific security controls to prevent LDAP Injection have been implemented.', 5, False, 943, 1)
        c.question_id = 34
        c.kb_id = 11
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.8', 'Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.', 5, False, 78, 1)
        c.question_id = 35
        c.kb_id = 4
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.9', 'Verify that the application protects against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks.', 5, False, 829, 1)
        c.question_id = 32
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.10', 'Verify that the application protects against XPath injection or XML injection attacks.', 5, False, 643, 1)
        c.question_id = 36
        c.kb_id = 183
        db.session.add(c)
        db.session.commit()

        '''
        c = ChecklistKB('5.4.1', 'VVerify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows.', 1, False, 643, 2)
        c.question_id = 36
        c.kb_id = 183
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('5.4.2', 'Verify that format strings do not take potentially hostile input, and are constant.', 1, False, 643, 2)
        c.question_id = 36
        c.kb_id = 183
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('5.4.3', 'Verify that sign, range, and input validation techniques are used to prevent integer overflows.', 1, False, 643, 2)
        c.question_id = 36
        c.kb_id = 183
        db.session.add(c)
        db.session.commit()
        '''

        c = ChecklistKB('5.5.1', 'Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.', 5, False, 502, 1)
        c.question_id = 37
        c.kb_id = 271
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.2', 'Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XXE.', 5, False, 611,1 )
        c.question_id = 37
        c.kb_id = 6
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.3', 'Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).', 5, False, 502, 1)
        c.question_id = 37
        c.kb_id = 271
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.4', 'Verify that when parsing JSON in browsers or JavaScript-based backends, JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON.', 5, False, 95, 1)
        c.question_id = 37
        c.kb_id = 181
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.0', 'Stored Cryptography Verification Requirements', 6, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.1.1', 'Verify that regulated private data is stored encrypted while at rest, such as personally identifiable information (PII), sensitive personal information, or data assessed likely to be subject to EUs GDPR.', 6, False, 311, 2)
        c.question_id = 38
        c.kb_id = 207
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.1.2', 'Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records.', 6, False, 311, 2)
        c.question_id = 38
        c.kb_id = 207
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.1.3', 'Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records.', 6, False, 311, 2)
        c.question_id = 38
        c.kb_id = 207
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.2.1', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.', 6, False, 310, 1)
        c.question_id = 39
        c.kb_id = 149
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.2', 'Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography.', 6, False, 327, 2)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.2.3', 'Verify that encryption initialization vector, cipher configuration, and block modes are configured securely using the latest advice..', 6, False, 326, 2)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.4', 'Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks.', 6, False, 326, 2)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.5', 'Verify that known insecure block modes (i.e. ECB, etc.), padding modes (i.e. PKCS#1 v1.5, etc.), ciphers with small block sizes (i.e. Triple-DES, Blowfish, etc.), and weak hashing algorithms (i.e. MD5, SHA1, etc.) are not used unless required for backwards compatibility.', 6, False, 326, 2)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.6', 'Verify that nonces, initialization vectors, and other single use numbers must not be used more than once with a given encryption key. The method of generation must be appropriate for the algorithm being used.', 6, False, 326, 2)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.7', 'Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party.', 6, False, 326, 3)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.8', 'Verify that all cryptographic operations are constant-time, with no short-circuit operations in comparisons, calculations, or returns, to avoid leaking information', 6, False, 326, 3)
        c.question_id = 39
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.1', 'Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic modules approved cryptographically secure random number generator when these random values are intended to be not guessable by an attacker.', 6, False, 338, 2)
        c.question_id = 40
        c.kb_id = 118
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.2', 'Verify that random GUIDs are created using the GUID v4 algorithm, and a cryptographically-secure pseudo-random number generator (CSPRNG). GUIDs created using other pseudo-random number generators may be predictable.', 6, False, 338, 2)
        c.question_id = 40
        c.kb_id = 298
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.3', 'Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances..', 6, False, 338, 3)
        c.question_id = 40
        c.kb_id = 205
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.4.1', 'Verify that a secrets management solution such as a key vault is used to securely create, store, control access to and destroy secrets.', 6, False, 798, 2)
        c.question_id = 41
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.4.2', 'Verify that key material is not exposed to the application but instead uses an isolated security module like a vault for cryptographic operations.', 6, False, 320, 2)
        c.question_id = 41
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.0', 'Error Handling and Logging Verification Requirements', 7, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('7.1.1', 'Verify that the application does not log credentials or payment details. Session tokens should only be stored in logs in an irreversible, hashed form.', 7, False, 532, 1);
        c.question_id = 42
        c.kb_id = 78
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.2', 'Verify that the application does not log other sensitive data as defined under local privacy laws or relevant security policy.', 7, False, 532, 1)
        c.question_id = 42
        c.kb_id = 78
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.3', 'Verify that the application logs security relevant events including successful and failed authentication events, access control failures, deserialization failures and input validation failures.', 7, False, 778, 2);
        c.question_id = 42
        c.kb_id = 83
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.4', 'Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens', 7, False, 778, 2);
        c.question_id = 42
        c.kb_id = 99
        db.session.add(c)
        db.session.commit()     

        c = ChecklistKB('7.2.1', 'Verify that all authentication decisions are logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.', 7, False, 778, 2);
        c.question_id = 43
        c.kb_id = 232
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.2.2', 'Verify that all access control decisions can be logged and all failed decisions are logged. This should include requests with relevant metadata needed for security investigations.', 7, False, 285, 2);
        c.question_id = 43
        c.kb_id = 232
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.1', 'Verify that the application appropriately encodes user-supplied data to prevent log injection', 7, False, 117, 2);
        c.question_id = 44
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.2', 'Verify that all events are protected from injection when viewed in log viewing software', 7, False, 117, 2);
        c.question_id = 44
        c.kb_id = 100
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.3', 'Verify that security logs are protected from unauthorized access and modification.', 7, False, 200, 2);
        c.question_id = 44
        c.kb_id = 257
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.4', 'Verify that time sources are synchronized to the correct time and time zone. Strongly consider logging only in UTC if systems are global to assist with post- incident forensic analysis.', 7, False, None, 2);
        c.question_id = 44
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.1', 'Verify that a generic message is shown when an unexpected or security sensitive error occurs, potentially with a unique ID which support personnel can use to investigate.', 7, False, 210, 1);
        c.question_id = 45
        c.kb_id = 15
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.2', 'Verify that exception handling (or a functional equivalent) is used across the codebase to account for expected and unexpected error conditions.', 7, False, 544, 2);
        c.question_id = 45
        c.kb_id = 299
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.3', 'Verify that a last resort error handler is defined which will catch all unhandled exceptions', 7, False, 460, 2);
        c.question_id = 45
        c.kb_id = 299
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.0', 'Error Handling and Logging Verification Requirements', 8, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.1.1', 'Verify the application protects sensitive data from being cached in server components such as load balancers and application caches.', 8, False, 542, 2)
        c.question_id = 46
        c.kb_id = 19
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.2', 'Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.', 8, False, 524, 2)
        c.question_id = 19
        c.kb_id = 145
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.3', 'Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values.', 8, False, 233, 2)
        c.question_id = 46
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.4', 'Verify the application can detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application.', 8, False, 525, 2)
        c.question_id = 46
        c.kb_id = 19
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.5', 'Verify that regular backups of important data are performed and that test restoration of data is performed.', 8, False, 770, 3)
        c.question_id = 46
        c.kb_id = 125
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.6', 'Verify that backups are stored securely to prevent data from being stolen or corrupted.', 8, False, 19, 3)
        c.question_id = 46
        c.kb_id = 300
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.2.1', 'Verify the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers.', 8, False, 525, 1)
        c.question_id = 25
        c.kb_id = 19
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.2.2', 'Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII.', 8, False, 922, 1);
        c.question_id = 47
        c.kb_id = 190
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.2.3', 'Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated.', 8, False, 922, 1);
        c.question_id = 47
        c.kb_id = 190
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.1', 'Verify that sensitive data is sent to the server in the HTTP message body or headers, and that query string parameters from any HTTP verb do not contain sensitive data.', 8, False, 319, 1);
        c.question_id = 48
        c.kb_id = 72
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.2', 'Verify that users have a method to remove or export their data on demand.', 8, False, 212, 1);
        c.question_id = 48
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.3', 'Verify that users are provided clear language regarding collection and use of supplied personal information and that users have provided opt-in consent for the use of that data before it is used in any way.', 8, False, 285, 1);
        c.question_id = 48
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.4', 'Verify that all sensitive data created and processed by the application has been identified, and ensure that a policy is in place on how to deal with sensitive data.', 8, False, 200, 1);
        c.question_id = 48
        c.kb_id = 276
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.5', 'Verify accessing sensitive data is audited (without logging the sensitive data itself), if the data is collected under relevant data protection directives or where logging of access is required.', 8, False, 532, 2)
        c.question_id = 48
        c.kb_id = 235
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.6', 'Verify that sensitive information contained in memory is overwritten as soon as it is no longer required to mitigate memory dumping attacks, using zeroes or random data.', 8, False, 226, 2)
        c.question_id = 48
        c.kb_id = 19
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.7', 'Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity', 8, False, 525, 2)
        c.question_id = 48
        c.kb_id = 135
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.8', 'Verify that sensitive personal information is subject to data retention classification, such that old or out of date data is deleted automatically, on a schedule, or as the situation requires.', 8, False, 285, 2)
        c.question_id = 48
        c.kb_id = 276
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.0', 'Communications Verification Requirements', 9, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.1', 'Verify that secured TLS is used for all client connectivity, and does not fall back to insecure or unencrypted protocols.', 9, False, 319,1 );
        c.question_id = 49
        c.kb_id = 244
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.2', 'Verify using online or up to date TLS testing tools that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred.', 9, False, 326, 1);
        c.question_id = 49
        c.kb_id = 247
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.3', 'Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are disabled, such as SSLv2, SSLv3, or TLS 1.0 and TLS 1.1. The latest version of TLS should be the preferred cipher suite.', 9, False, 326, 1);
        c.question_id = 49
        c.kb_id = 247
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.1', 'Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected.', 9, False, 295, 2);
        c.question_id = 50
        c.kb_id = 101
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.2.2', 'Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols.', 9, False, 319, 2);
        c.question_id = 50
        c.kb_id = 302
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.2.3', 'Verify that all encrypted connections to external systems that involve sensitive information or functions are authenticated.', 9, False, 297, 2);
        c.question_id = 50
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.4', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured.', 9, False, 299, 2);
        c.question_id = 50
        c.kb_id = 139
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.5', 'Verify that backend TLS connection failures are logged', 9, False, 544, 3);
        c.question_id = 50
        c.kb_id = 103
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.0', 'Malicious Code Verification Requirements', 10, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.1.1', 'Verify that a code analysis tool is in use that can detect potentially malicious code, such as time functions, unsafe file operations and network connections.', 10, False, 749, 3);
        c.question_id = 51
        c.kb_id = 301
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.2.1', 'Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the users permission for it to operate before collecting any data.', 10, False, 359, 2);
        c.question_id = 52
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.2', 'Verify that the application does not ask for unnecessary or excessive permissions to privacy related features or sensors, such as contacts, cameras, microphones, or location.', 10, False, 272, 2);
        c.question_id = 52
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.3', 'Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, rootkits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered.', 10, False, 507, 3);
        c.question_id = 52
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.4', 'Verify that the application source code and third party libraries does not contain time bombs by searching for date and time related functions.', 10, False, 511, 3);
        c.question_id = 52
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.5', 'Verify that the application source code and third party libraries does not contain malicious code, such as salami attacks, logic bypasses, or logic bombs.', 10, False, 511, 3);
        c.question_id = 52
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.6', 'Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality.', 10, False, 507, 3);
        c.question_id = 52
        c.kb_id = None
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.3.1', 'Verify that if the application has a client or server auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update.', 10, False, 16, 1);
        c.question_id = 53
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.3.2', 'Verify that the application employs integrity protections, such as code signing or sub-resource integrity. The application must not load or execute code from untrusted sources, such as loading includes, modules, plugins, code, or libraries from untrusted sources or the Internet.', 10, False, 353, 1);
        c.question_id = 53
        c.kb_id = 303
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.3.3', 'Verify that the application has protection from sub-domain takeovers if the application relies upon DNS entries or DNS sub-domains, such as expired domain names, out of date DNS pointers or CNAMEs, expired projects at public source code repos, or transient cloud APIs, serverless functions, or storage buckets (autogen-bucket-id.cloud.example.com) or similar. Protections can include ensuring that DNS names used by applications are regularly checked for expiry or change.', 10, False, 350, 1);
        c.question_id = 53
        c.kb_id = 294
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.0', 'Business Logic Verification Requirements', 11, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.1', 'Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.', 11, False, 841, 1);
        c.question_id = 54
        c.kb_id = 110
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.2', 'Verify the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.', 11, False, 779, 1);
        c.question_id = 54
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.3', 'Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis.', 11, False, 770, 1);
        c.question_id = 54
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.4', 'Verify the application has sufficient anti-automation controls to detect and protect against data exfiltration, excessive business logic requests, excessive file uploads or denial of service attacks.', 11, False, 770, 1);
        c.question_id = 54
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.5', 'Verify the application has business logic limits or validation to protect against likely business risks or threats, identified using threat modelling or similar methodologies.', 11, True, 841, 1);
        c.question_id = 54
        c.kb_id = 164
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.6', 'Verify the application does not suffer from "time of check to time of use" (TOCTOU) issues or other race conditions for sensitive operations.', 11, True, 367, 2);
        c.question_id = 54
        c.kb_id = 293
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.7', 'Verify the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt', 11, True, 754, 2);
        c.question_id = 54
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.8', 'Verify the application has configurable alerting when automated attacks or unusual activity is detected.', 11, False, 390, 2);
        c.question_id = 54
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.0', 'File and Resources Verification Requirements', 12, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.1.1', 'Verify that the application will not accept large files that could fill up storage or cause a denial of service attack.', 12, False, 400, 1);
        c.question_id = 55
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.1.2', 'Verify that compressed files are checked for "zip bombs" - small input files that will decompress into huge files thus exhausting file storage limits.', 12, False, 400, 2);
        c.question_id = 55
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.1.3', 'Verify that a file size quota and maximum number of files per user is enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files.', 12, False, 409, 2);
        c.question_id = 55
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.2.1', 'Verify that files obtained from untrusted sources are validated to be of expected type based on the files content.', 12, False, 434, 2);
        c.question_id = 56
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.3.1', 'Verify that user-submitted filename metadata is not used directly with system or framework file and URL API to protect against path traversal.', 12, False, 22, 1);
        c.question_id = 57
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.2', 'Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI).', 12, False, 73, 1);
        c.question_id = 57
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.3', 'Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files (RFI); which may also lead to SSRF.', 12, False, 98, 1);
        c.question_id = 57
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.4', 'Verify that the application protects against reflective file download (RFD) by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter, the response Content-Type header should be set to text/plain, and the Content-Disposition header should have a fixed filename.', 12, False, 641, 1);
        c.question_id = 57
        c.kb_id = 160
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.5', 'Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection.', 12, False, 78, 1);
        c.question_id = 57
        c.kb_id = 225
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.3.6', 'Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs.', 12, False, 829, 2);
        c.question_id = 57
        c.kb_id = 13
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.4.1', 'Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation.', 12, False, 922, 1);
        c.question_id = 58
        c.kb_id = 227
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.4.2', 'Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload of known malicious content.', 12, False, 509, 1);
        c.question_id = 58
        c.kb_id = 226
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.5.1', 'Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak); temporary working files (e.g. .swp); compressed files (.zip, .tar.gz, etc) and other extensions commonly used by editors should be blocked unless required.', 12, False, 552, 1);
        c.question_id = 59
        c.kb_id = 288
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.5.2', 'Verify that direct requests to uploaded files will never be executed as HTML/JavaScript content.', 12, False, 434, 1);
        c.question_id = 59
        c.kb_id = 227
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.6.1', 'Verify that the web or application server is configured with a whitelist of resources or systems to which the server can send requests or load data/files from.', 12, False, 918, 1);
        c.question_id = 60
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.0', 'API and Web Service Verification Requirements', 13, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.1', 'Verify that all application components use the same encodings and parsers to avoid parsing attacks that exploit different URI or file parsing behavior that could be used in SSRF and RFI attacks.', 13, False, 116, 1);
        c.question_id = 61
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.2', 'Verify that access to administration and management functions is limited to authorized administrators.', 13, False, 419, 1);
        c.question_id = 61
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.3', 'Verify API URLs do not expose sensitive information, such as the API key, session tokens etc.', 13, False, 598, 1);
        c.question_id = 61
        c.kb_id = 91
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.1.4', 'Verify that authorization decisions are made at both the URI, enforced by programmatic or declarative security at the controller or router, and at the resource level, enforced by model-based permissions.', 13, False, 285, 2);
        c.question_id = 61
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.1.5', 'Verify that requests containing unexpected or missing content types are rejected with appropriate headers (HTTP response status 406 Unacceptable or 415 Unsupported Media Type).', 13, False, 434, 2);
        c.question_id = 61
        c.kb_id = 104
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.1', 'Verify that enabled RESTful HTTP methods are a valid choice for the user or action, such as preventing normal users using DELETE or PUT on protected API or resources.', 13, False, 650, 1);
        c.question_id = 62
        c.kb_id = 129
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.2', 'Verify that JSON schema validation is in place and verified before accepting input.', 13, False, 20, 1);
        c.question_id = 62
        c.kb_id = 286
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.3', 'Verify that RESTful web services that utilize cookies are protected from Cross-Site Request Forgery via the use of at least one or more of the following: triple or double submit cookie pattern, CSRF nonces, or ORIGIN request header checks.', 13, False, 352, 1);
        c.question_id = 62
        c.kb_id = 224
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.2.4', 'Verify that REST services have anti-automation controls to protect against excessive calls, especially if the API is unauthenticated.', 13, False, 779, 2);
        c.question_id = 62
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.2.5', 'Verify that REST services explicitly check the incoming Content-Type to be the expected one, such as application/xml or application/JSON.', 13, False, 436, 2);
        c.question_id = 62
        c.kb_id = 104
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('13.2.6', 'Verify that the message headers and payload are trustworthy and not modified in transit. Requiring strong encryption for transport (TLS only) may be sufficient in many cases as it provides both confidentiality and integrity protection. Per- message digital signatures can provide additional assurance on top of the transport protections for high-security applications but bring with them additional complexity and risks to weigh against the benefits', 345, False, 598, 2);
        c.question_id = 62
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.3.1', 'Verify that XSD schema validation takes place to ensure a properly formed XML document, followed by validation of each input field before any processing of that data takes place.', 13, False, 20, 1);
        c.question_id = 63
        c.kb_id = 175
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.3.2', 'Verify that the message payload is signed using WS-Security to ensure reliable transport between client and service.', 13, False, 345, 2);
        c.question_id = 63
        c.kb_id = 195
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.4.1', 'Verify that query whitelisting or a combination of depth limiting and amount limiting should be used to prevent GraphQL or data layer expression denial of service (DoS) as a result of expensive, nested queries. For more advanced scenarios, query cost analysis should be used.', 13, False, 770, 2);
        c.question_id = 64
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.4.2', 'Verify that GraphQL or other data layer authorization logic should be implemented at the business logic layer instead of the GraphQL layer.', 13, False, 285, 2);
        c.question_id = 64
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.0', 'Configuration Verification Requirements', 14, False, None, None);
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.1.1', 'Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts', 14, False, None, 2);
        c.question_id = 65
        c.kb_id = 284
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.1.2', 'Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found.', 14, False, 120, 2);
        c.question_id = 65
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.3', 'Verify that server configuration is hardened as per the recommendations of the application server and frameworks in use.', 14, False, 16, 2);
        c.question_id = 65
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.4', 'Verify that the application, configuration, and all dependencies can be re- deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.', 14, False, None, 2)
        c.question_id = 65
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.5', 'Verify that authorized administrators can verify the integrity of all security- ✓ relevant configurations to detect tampering.', 14, False, None, 3);
        c.question_id = 65
        c.kb_id = 237
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.1', 'Verify that all components are up to date, preferably using a dependency checker during build or compile time.', 14, False, 1026, 1);
        c.question_id = 65
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.2.2', 'Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users.', 141, False, 1002, 1);
        c.question_id = 66
        c.kb_id = 283
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.2.3', 'Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset.', 14, False, 714, 1);
        c.question_id = 66
        c.kb_id = 223
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.4', 'Verify that third party components come from pre-defined, trusted and continually maintained repositories', 14, False, 828, 2);
        c.question_id = 66
        c.kb_id = 238
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.5', 'Verify that an inventory catalog is maintained of all third party libraries in use.', 14, False, None, 2);
        c.question_id = 66
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.6', 'Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application.', 14, False, 265, 2);
        c.question_id = 66
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.1', 'Verify that web or application server and framework error messages are configured to deliver user actionable, customized responses to eliminate any unintended security disclosures.', 14, True, 209, 1);
        c.question_id = 67
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.2', 'Verify that web or application server and application framework debug modes are disabled in production to eliminate debug features, developer consoles, and unintended security disclosures.', 14, True, 497, 1);
        c.question_id = 67
        c.kb_id = 16
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.3', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', 14, False, 200, 1);
        c.question_id = 67
        c.kb_id = 130
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.1', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1).', 14, False, 173, 1);
        c.question_id = 68
        c.kb_id = 104
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.2', 'Verify that all API responses contain Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type).', 14, False, 116, 1);
        c.question_id = 68
        c.kb_id = 193
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.3', 'Verify that a content security policy (CSPv2) is in place that helps mitigate impact for XSS attacks like HTML, DOM, JSON, and JavaScript injection vulnerabilities.', 14, False, 1021, 1);
        c.question_id = 68
        c.kb_id = 178
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.4', 'Verify that all responses contain X-Content-Type-Options: nosniff.', 14, False, 116, 1);
        c.question_id = 68
        c.kb_id = 193
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.5', 'Verify that HTTP Strict Transport Security headers are included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains.', 14, False, 523, 1);
        c.question_id = 68
        c.kb_id = 192
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.6', 'Verify that a suitable "Referrer-Policy" header is included, such as "no-referrer" or "same-origin".', 14, False, 116, 1);
        c.question_id = 68
        c.kb_id = 282
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.7', 'Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a third-party site.', 14, False, 346, 1);
        c.question_id = 68
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.1', 'Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS.', 14, False, 749, 1);
        c.question_id = 69
        c.kb_id = 129
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.2', 'Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker.', 14, False, 346, 1);
        c.question_id = 69
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.3', 'Verify that the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header uses a strict white-list of trusted domains to match against and does not support the "null" origin.', 14, False, 346, 1);
        c.question_id = 69
        c.kb_id = 112
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.5.4', 'Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application.', 14, False, 306, 2);
        c.question_id = 69
        c.kb_id = 999
        db.session.add(c)
        db.session.commit()
        
        db.session.add(LabItem('Path traversal (LFI)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-1-filename-injection', 1))
        db.session.commit()
        
        db.session.add(LabItem('Cross Site Scripting','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting', 1))
        db.session.commit()
        
        db.session.add(LabItem('Cross site scripting (attribute)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting-attribute', 1))
        db.session.commit()
        
        db.session.add(LabItem('Cross site scripting (href)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting-href', 1))
        db.session.commit()
        
        db.session.add(LabItem('Cross site request forgery','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-5-csrf', 3))
        db.session.commit()
        
        db.session.add(LabItem('External entity attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-6-xxe', 2))
        db.session.commit()
        
        db.session.add(LabItem('Insecure file upload','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-13-file-upload', 1))
        db.session.commit()
        
        db.session.add(LabItem('Clickjacking','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-20-clickjacking', 1))
        db.session.commit()
        
        db.session.add(LabItem('Rate-limiting','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-29-ratelimiting', 1))
        db.session.commit()
        
        db.session.add(LabItem('HttpOnly (session hijacking)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-39-httponly-session-hijacking-xss', 3))
        db.session.commit()
        
        db.session.add(LabItem('Missing authorization','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-44-authorisation-missing', 2))
        db.session.commit()
        
        db.session.add(LabItem('Exposed Docker daemon','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-45-exposed-docker', 3))
        db.session.commit()
        
        db.session.add(LabItem('SQLI (union select)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-46-sqli-union-select', 2))
        db.session.commit()
        
        db.session.add(LabItem('Open redirect (hard)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-67-open-redirect-hard', 3))
        db.session.commit()
        
        db.session.add(LabItem('CORS exploitation','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-112-cors-exploitation', 3))
        db.session.commit()

        db.session.add(LabItem('Formulla injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-95-formula-injection', 1))
        db.session.commit()
        
        db.session.add(LabItem('Mass assingment attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-147-parameter-binding', 1))
        db.session.commit()
        
        db.session.add(LabItem('SQLI -like','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-156-sqli-like', 2))
        db.session.commit()
        
        db.session.add(LabItem('SQLI-blind','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-156-sqli-blind', 3))
        db.session.commit()
        
        db.session.add(LabItem('Local file inclusion','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-173-local-file-inclusion', 1))
        db.session.commit()
        
        db.session.add(LabItem('Remote file inclusion','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-173-remote-file-inclusion', 1))
        db.session.commit()
        
        db.session.add(LabItem('Content security policiy','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-178-content-security-policy', 1))
        db.session.commit()
        
        db.session.add(LabItem('Server side request forgery','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-262-server-side-request-forgery', 3))
        db.session.commit()
        
        db.session.add(LabItem('Tabnabbing','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-266-tabnabbing', 2))
        db.session.commit()
        
        db.session.add(LabItem('Server side template injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-267-server-side-template-injection', 3))
        db.session.commit()
        
        db.session.add(LabItem('Insecure direct object reference','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-268-insecure-direct-object-references', 2))
        db.session.commit()
        
        db.session.add(LabItem('JWT null','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-7006-jwt-null', 2))
        db.session.commit()
        
        db.session.add(LabItem('JWT weak secret','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-7006-jwt-secret', 2))
        db.session.commit()
        
        db.session.add(LabItem('Insecure deserialization (yaml)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-deserialisation-yaml', 3))
        db.session.commit()
        
        db.session.add(LabItem('Race condition','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-race-condition', 3))
        db.session.commit()
        
        db.session.add(LabItem('Regex Ddos','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-dos-regex', 1))
        db.session.commit()

        db.session.add(LabItem('Command injection 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-cmd-injection-1', 1))
        db.session.commit()

        db.session.add(LabItem('Command injection 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-cmd-injection-2', 1))
        db.session.commit()

        db.session.add(LabItem('Information disclosure 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-information-leakeage-comments', 1))
        db.session.commit()

        db.session.add(LabItem('Information disclosure 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-information-leakeage-metadata', 1))
        db.session.commit()

        db.session.add(LabItem('Blind command injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-blind-cmd-injection-1', 2))
        db.session.commit()

        db.session.add(LabItem('Right to left override attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-right-to-left-override', 1))
        db.session.commit()

        db.session.commit()
        return True

    except:
        db.session.rollback()
        raise
