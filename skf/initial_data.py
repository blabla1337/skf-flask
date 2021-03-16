import datetime
from skf.database import db
from skf.database.privileges import Privilege
from skf.database.users import User
from skf.database.groups import Group
from skf.database.questions import Question
from skf.database.checklist_category import ChecklistCategory
from skf.database.checklist_types import ChecklistType
from skf.database.checklists_kb import ChecklistKB
from skf.database.checklists_results import ChecklistResult
from skf.database.code_items import CodeItem
from skf.database.groupmembers import GroupMember
from skf.database.kb_items import KBItem
from skf.database.lab_items import LabItem
from skf.database.lab_items_code import LabItemCode
from skf.database.lab_items_code_options import LabItemCodeOptions
from skf.database.logs import Log
from skf.database.project_sprints import ProjectSprint
from skf.database.projects import Project
from skf.database.question_results import QuestionResult
from skf.database.checklist_kb_code_item import ChecklistKBCodeItem


def load_initial_data():

    try:
        p = Privilege('edit:read:manage:delete')
        db.session.add(p)
        db.session.add(Privilege('edit:read:delete'))
        db.session.add(Privilege('edit:read'))
        db.session.add(Privilege('read'))  

        user = User(username='admin', accessToken=1234, email="example@owasp.org")
        user.privilege = p
        db.session.add(user)

        group = Group('privateGroup', datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

        group.members.append(user)
        group.owner = user
        db.session.add(group)

        '''
        Checklist Categories for ASVS
        '''

        checklist = ChecklistType(name='Architecture, Design and Threat Modeling Requirements', description='Security architecture has almost become a lost art in many organizations. The days of the enterprise architect have passed in the age of DevSecOps. The application security field must catch up and adopt agile security principles while re-introducing leading security architecture principles to software practitioners. Architecture is not an implementation, but a way of thinking about a problem that has potentially many different answers, and no one single "correct" answer. All too often, security is seen as inflexible and demanding that developers fix code in a particular way, when the developers may know a much better way to solve the problem. There is no single, simple solution for architecture, and to pretend otherwise is a disservice to the software engineering field.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()
        
        checklist = ChecklistType(name='Authentication Verification Requirements', description='Authentication is the act of establishing, or confirming, someone (or something) as authentic and that claims made by a person or about a device are correct, resistant to impersonation, and prevent recovery or interception of passwords.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()
        
        checklist = ChecklistType(name='Session Management Verification Requirements', description='One of the core components of any web-based application or stateful API is the mechanism by which it controls and maintains the state for a user or device interacting with it. Session management changes a stateless protocol to stateful, which is critical for differentiating different users or devices.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Access Control Verification Requirements', description='Authorization is the concept of allowing access to resources only to those permitted to use them. Ensure that a verified application satisfies the following high level requirements:• Persons accessing resources hold valid credentials to do so.* Users are associated with a well-defined set of roles and privileges.• Role and permission metadata is protected from replay or tampering.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Validation, Sanitization and Encoding Verification Requirements', description='The most common web application security weakness is the failure to properly validate input coming from the client or the environment before directly using it without any output encoding. This weakness leads to almost all of the significant vulnerabilities in web applications, such as Cross-Site Scripting (XSS), SQL injection, interpreter injection, locale/Unicode attacks, file system attacks, and buffer overflows.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Stored Cryptography Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • All cryptographic modules fail in a secure manner and that errors are handled correctly. • A suitable random number generator is used. • Access to keys is securely managed. V6.1 Data Classification', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Error Handling and Logging Verification Requirements', description='The primary objective of error handling and logging is to provide useful information for the user, administrators, and incident response teams. The objective is not to create massive amounts of logs, but high quality logs, with more signal than discarded noise.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Data Protection Verification Requirements', description='There are three key elements to sound data protection: Confidentiality, Integrity and Availability (CIA). This standard assumes that data protection is enforced on a trusted system, such as a server, which has been hardened and has sufficient protections.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Communications Verification Requirements', description='Leading industry advice on secure TLS configuration changes frequently, often due to catastrophic breaks in existing algorithms and ciphers. Always use the most recent versions of TLS configuration review tools (such as SSLyze or other TLS scanners) to configure the preferred order and algorithm selection. Configuration should be periodically checked to ensure that secure communications configuration is always present and effective.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Malicious Code Verification Requirements', description='Finding malicious code is proof of the negative, which is impossible to completely validate. Best efforts should be undertaken to ensure that the code has no inherent malicious code or unwanted functionality.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Business Logic Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • The business logic flow is sequential, processed in order, and cannot be bypassed. • Business logic includes limits to detect and prevent automated attacks, such as continuous small funds transfers, or adding a million friends one at a time, and so on. • High value business logic flows have considered abuse cases and malicious actors, and have protections against spoofing, tampering, repudiation, information disclosure, and elevation of privilege attacks.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()
        
        checklist = ChecklistType(name='File and Resources Verification Requirements', description='Ensure that a verified application satisfies the following high level requirements: • Untrusted file data should be handled accordingly and in a secure manner. • Untrusted file data obtained from untrusted sources are stored outside the web root and with limited permissions.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='API and Web Service Verification Requirements', description='Ensure that a verified application that uses trusted service layer APIs (commonly using JSON or XML or GraphQL) has: • Adequate authentication, session management and authorization of all web services. • Input validation of all parameters that transit from a lower to higher trust level. • Effective security controls for all API types, including cloud and Serverless API Please read this chapter in combination with all other chapters at this same level; we no longer duplicate authentication or API session management concerns.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Configuration Verification Requirements', description='Ensure that a verified application has: • A secure, repeatable, automatable build environment. • Hardened third party library, dependency and configuration management such that out of date or insecure components are not included by the application. • A secure-by-default configuration, such that administrators and users have to weaken the default security posture. Configuration of the application out of the box should be safe to be on the Internet, which means a safe out of the box configuration.', visibility=1)
        checklist.checklist_category_id = 1
        db.session.add(checklist)
        db.session.commit()

        '''
        Checklist Categories for MASVS
        '''

        checklist = ChecklistType(name='Architecture, Design and Threat Modeling Requirements', description='In a perfect world, security would be considered throughout all phases of development. In reality however, security is often only a consideration at a late stage in the SDLC. Besides the technical controls, the MASVS requires processes to be in place that ensure that the security has been explicitly addressed when planning the architecture of the mobile app, and that the functional and security roles of all components are known. Since most mobile applications act as clients to remote services, it must be ensured that appropriate security standards are also applied to those services - testing the mobile app in isolation is not sufficient.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Data Storage and Privacy Requirements', description='The protection of sensitive data, such as user credentials and private information, is a key focus in mobile security. Firstly, sensitive data can be unintentionally exposed to other apps running on the same device if operating system mechanisms like IPC are used improperly. Data may also unintentionally leak to cloud storage, backups, or the keyboard cache. Additionally, mobile devices can be lost or stolen more easily compared to other types of devices, so an adversary gaining physical access is a more likely scenario. In that case, additional protections can be implemented to make retrieving the sensitive data more difficult.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Cryptography Requirements', description='Cryptography is an essential ingredient when it comes to protecting data stored on a mobile device. It is also a category where things can go horribly wrong, especially when standard conventions are not followed. The purpose of the controls in this chapter is to ensure that the verified application uses cryptography according to industry best practices.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Authentication and Session Management Requirements', description='In most cases, users logging into a remote service is an integral part of the overall mobile app architecture. Even though most of the logic happens at the endpoint, MASVS defines some basic requirements regarding how user accounts and sessions are to be managed.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Network Communication Requirements', description='The purpose of the controls listed in this section is to ensure the confidentiality and integrity of information exchanged between the mobile app and remote service endpoints. At the very least, a mobile app must set up a secure, encrypted channel for network communication using the TLS protocol with appropriate settings. Level 2 lists additional defense-in-depth measure such as SSL pinning.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Platform Interaction Requirements', description='The controls in this group ensure that the app uses platform APIs and standard components in a secure manner. Additionally, the controls cover communication between apps (IPC).', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()
        
        checklist = ChecklistType(name='Code Quality and Build Setting Requirements', description='The goal of this control is to ensure that basic security coding practices are followed in developing the app, and that "free" security features offered by the compiler are activated.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
        db.session.commit()

        checklist = ChecklistType(name='Resilience Requirements', description='This section covers defense-in-depth measures recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the apps resilience against reverse engineering and specific client-side attacks. The controls in this section should be applied as needed, based on an assessment of the risks caused by unauthorized tampering with the app and/or reverse engineering of the code. We suggest consulting the OWASP document "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (see references below) for a list of business risks as well as associated technical threats.', visibility=1)
        checklist.checklist_category_id = 2
        db.session.add(checklist)
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
        q = Question('Does your data need to be stored encrypted?', 6)
        db.session.add(q)
        db.session.commit()

        #39 -- 6.2
        q = Question('Does your application need cryptgrapic functions (they need to be on par with the latest known to be secure standards)', 6)
        db.session.add(q)
        db.session.commit()

        #40 -- 6.3
        q = Question('Does your application need secure random values or UUIDs (are they tested for sufficient entropy?)', 6)
        db.session.add(q)
        db.session.commit()

        #41 -- 6.4
        q = Question('Do your secrets need to be managed in a key-vault?', 6)
        db.session.add(q)
        db.session.commit()

        #42 -- 7.1
        q = Question('Is the application logging sensitive information? (credentials, payment details, tokens, etc)', 7)
        db.session.add(q)
        db.session.commit()

        #43 -- 7.2
        q = Question('Does the application needs to actively do logging (Do logs exist for authentication/ access control decisions?)', 7)
        db.session.add(q)
        db.session.commit()

        #44 -- 7.3
        q = Question('Do you need to implement log protection (Are logs protected for un-authorized access, injection flaws(also in viewing software), and are timestamps synced to match respective timezones)', 7)
        db.session.add(q)
        db.session.commit()

        #45 -- 7.4
        q = Question('Do you need centrilized error handling (Are errors on the application gracefully handled and show non generic error messages?)', 7)
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

        '''
        Checklist controls for ASVS
        '''

        c = ChecklistKB('1.0', 'Architecture, Design and Threat Modeling Requirements', 1, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.1', 'Verify the use of a secure software development lifecycle that addresses security in all stages of development.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html', 2)
        c.question_id = 1
        c.kb_id = 272
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.2', 'Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.', 1, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1053', 2)
        c.question_id = 1
        c.kb_id = 1053
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.3', 'Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else\s profile', 1, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1110', 2)
        c.question_id = 1
        c.kb_id = 1110
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.4', 'Verify documentation and justification of all the application\s trust boundaries, components, and significant data flows.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1059',2)
        c.question_id = 1
        c.kb_id = 1059
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.5', 'Verify definition and security analysis of the application\s high-level architecture and all connected remote services. ', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1059', 2)
        c.question_id = 1
        c.kb_id = 1059
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.6', 'Verify implementation of centralized, simple (economy of design) vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls.', 1, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/637', 2)
        c.question_id = 1
        c.kb_id = 184
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.1.7', 'Verify availability of a secure coding checklist, security requirements, guideline, or policy to all developers and testers.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/637', 2)
        c.question_id = 1
        c.kb_id = 637
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.1', 'Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers.', 1, False, 'https://cwe.mitre.org/data/definitions/250', 2)
        c.question_id = 2
        c.kb_id = 250
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.2', 'Verify that communications between application components, including APIs, middleware and data layers, are authenticated. Components should have the least necessary privileges needed.', 1, False, 'https://cwe.mitre.org/data/definitions/306', 2)
        c.question_id = 2
        c.kb_id = 306
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.3', 'Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches.', 1, False, 'https://cwe.mitre.org/data/definitions/306', 2)
        c.question_id = 2
        c.kb_id = 306
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.2.4', 'Verify that all authentication pathways and identity management APIs implement consistent authentication security control strength, such that there are no weaker alternatives per the risk of the application.', 1, False, 'https://cwe.mitre.org/data/definitions/306', 2)
        c.question_id = 2
        c.kb_id = 306
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.1', 'Verify that trusted enforcement points such as at access control gateways, servers, and serverless functions enforce access controls. Never enforce access controls on the client.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/602', 2)
        c.question_id = 3
        c.kb_id = 602
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.2', 'Verify that the chosen access control solution is flexible enough to meet the application\s needs.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/284', 2)
        c.question_id = 3
        c.kb_id = 284
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.3', 'Verify enforcement of the principle of least privilege in functions, data files, URLs, controllers, services, and other resources. This implies protection against spoofing and elevation of privilege.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/272', 2)
        c.question_id = 3
        c.kb_id = 272
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.4', 'Verify the application uses a single and well-vetted access control mechanism for accessing protected data and resources. All requests must pass through this single mechanism to avoid copy and paste or insecure alternative paths.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/284', 2)
        c.question_id = 3
        c.kb_id = 284
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.4.5', 'Verify that attribute or feature-based access control is used whereby the code checks the user\s authorization for a feature/data item rather than just their role.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/275', 2)
        c.question_id = 3
        c.kb_id = 274
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.1', 'Verify that input and output requirements clearly define how to handle and process data based on type, content, and applicable laws, regulations, and other policy compliance.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1029', 2)
        c.question_id = 4
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.2', 'Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/502', 2)
        c.question_id = 4
        c.kb_id = 502
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.3', 'Verify that input validation is enforced on a trusted service layer.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/602', 2)
        c.question_id = 4
        c.kb_id = 602
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.5.4', 'Verify that output encoding occurs close to or by the interpreter for which it is intended.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 2)
        c.question_id = 4
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.1', 'Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 5
        c.kb_id = 320
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.2', 'Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives.', 1, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 5
        c.kb_id = 320
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.3', 'Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 5
        c.kb_id = 204
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.6.4', 'Verify that symmetric keys, passwords, or API secrets generated by or shared with clients are used only in protecting low risk secrets, such as encrypting local storage, or temporary ephemeral uses such as parameter obfuscation. Sharing secrets with clients is clear-text equivalent and architecturally should be treated as such.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 5
        c.kb_id = 277
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.7.1', 'Verify that a common logging format and approach is used across the system.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1009', 2)
        c.question_id = 6
        c.kb_id = 1009
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.7.2', 'Verify that logs are securely transmitted to a preferably remote system for analysis, detection, alerting, and escalation.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html', 2)
        c.question_id = 6
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.8.1', 'Verify that all sensitive data is identified and classified into protection levels.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html', 2)
        c.question_id = 7
        c.kb_id = 278
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.8.2', 'Verify that all protection levels have an associated set of protection requirements, such as encryption requirements, integrity requirements, retention, privacy and other confidentiality requirements, and that these are applied in the architecture.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html', 2)
        c.question_id = 7
        c.kb_id = 278
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.9.1', 'Verify the application encrypts communications between components, particularly when these components are in different containers, systems, sites, or cloud providers.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/319', 2)
        c.question_id = 8
        c.kb_id = 319
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.9.2', 'Verify that application components verify the authenticity of each side in a communication link to prevent person-in-the-middle attacks. For example, application components should validate TLS certificates and chains.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/295', 2)
        c.question_id = 8
        c.kb_id = 295
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.10.1', 'Verify that a source code control system is in use, with procedures to ensure that check-ins are accompanied by issues or change tickets. The source code control system should have access control and identifiable users to allow traceability of any changes.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Virtual_Patching_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/284', 2)
        c.question_id = 9
        c.kb_id = 284
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.11.1', 'Verify the definition and documentation of all application components in terms of the business or security functions they provide.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1059', 2)
        c.question_id = 70
        c.kb_id = 1059
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.11.2', 'Verify that all high-value business logic flows, including authentication, session management and access control, do not share unsynchronized state.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/362', 2)
        c.question_id = 70
        c.kb_id = 362
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('1.11.3', 'Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.', 1, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/362', 3)
        c.question_id = 70
        c.kb_id = 362
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.12.1', 'Verify that user-uploaded files are stored outside of the web root.', 1, False, 'https://cwe.mitre.org/data/definitions/552', 2)
        c.question_id = 71
        c.kb_id = 552
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.12.2', 'Verify that user-uploaded files - if required to be displayed or downloaded from the application - are served by either octet stream downloads, or from an unrelated domain, such as a cloud file storage bucket. Implement a suitable content security policy to reduce the risk from XSS vectors or other attacks from the uploaded file.', 1, False, 'https://cwe.mitre.org/data/definitions/646', 2)
        c.question_id = 71
        c.kb_id = 646
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.1', 'Verify the segregation of components of differing trust levels through well-defined security controls, firewall rules, API gateways, reverse proxies, cloud-based security groups, or similar mechanisms.', 1, False, 'https://cwe.mitre.org/data/definitions/923', 2)
        c.question_id = 72
        c.kb_id = 923
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.2', 'Verify that if deploying binaries to untrusted devices makes use of binary signatures, trusted connections, and verified endpoints.', 1, False, 'https://cwe.mitre.org/data/definitions/494', 2)
        c.question_id = 72
        c.kb_id = 494
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.3', 'Verify that the build pipeline warns of out-of-date or insecure components and takes appropriate actions.', 1, False, 'https://cwe.mitre.org/data/definitions/1104', 2)
        c.question_id = 72
        c.kb_id = 1104
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.4', 'Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts.', 1, False, 'https://cwe.mitre.org/', 2)
        c.question_id = 72
        c.kb_id = 281
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.5', 'Verify that application deployments adequately sandbox, containerize and/or isolate at the network level to delay and deter attackers from attacking other applications, especially when they are performing sensitive or dangerous actions such as deserialization.', 1, False, 'https://cwe.mitre.org/data/definitions/265', 2)
        c.question_id = 72
        c.kb_id = 265
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('1.14.6', 'Verify the application does not use unsupported, insecure, or deprecated client-side technologies such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets.', 1, False, 'https://cwe.mitre.org/data/definitions/477', 2)
        c.question_id = 72
        c.kb_id = 477
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.0', 'Authentication Verification Requirements', 2, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.1.1', 'Verify that user set passwords are at least 12 characters in length. (C6)', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.2', 'Verify that passwords 64 characters or longer are permitted.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.3', 'Verify that passwords can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.4', 'Verify that Unicode characters are permitted in passwords. A single Unicode code point is considered a character, so 12 emoji or 64 kanji characters should be valid and permitted.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.5', 'Verify users can change their password.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/620', 1)
        c.question_id = 10
        c.kb_id = 620
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.6', 'Verify that password change functionality requires the user\s current and new password.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/620', 1)
        c.question_id = 10
        c.kb_id = 620
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.7', 'Verify that passwords submitted during account registration, login, and password change are checked against a set of breached passwords either locally (such as the top 1,000 or 10,000 most common passwords which match the system\s password policy) or using an external API. If using an API a zero knowledge proof or other mechanism should be used to ensure that the plain text password is not sent or used in verifying the breach status of the password. If the password is breached, the application must require the user to set a new non-breached password.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.8', 'Verify that a password strength meter is provided to help users set a stronger password.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.9', 'Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.10', 'Verify that there are no periodic credential rotation or password history requirements.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/263', 1)
        c.question_id = 10
        c.kb_id = 263
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.11', 'Verify that "paste" functionality, browser password helpers, and external password managers are permitted.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521',1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.1.12', 'Verify that the user can choose to either temporarily view the entire masked password, or temporarily view the last typed character of the password on platforms that do not have this as native functionality.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/521', 1)
        c.question_id = 10
        c.kb_id = 521
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.1', 'Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. Such controls include blocking the most common breached passwords, soft lockouts, rate limiting, CAPTCHA, ever increasing delays between attempts, IP address restrictions, or risk-based restrictions such as location, first login on a device, recent attempts to unlock the account, or similar. Verify that no more than 100 failed attempts per hour is possible on a single account.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/307', 1)
        c.question_id = 11
        c.kb_id = 307
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.2', 'Verify that the use of weak authenticators (such as SMS and email) is limited to secondary verification and transaction approval and not as a replacement for more secure authentication methods. Verify that stronger methods are offered before weak methods, users are aware of the risks, or that proper measures are in place to limit the risks of account compromise.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/304', 1)
        c.question_id = 11
        c.kb_id = 304
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.3', 'Verify that secure notifications are sent to users after updates to authentication details, such as credential resets, email or address changes, logging in from unknown or risky locations. The use of push notifications - rather than SMS or email - is preferred, but in the absence of push notifications, SMS or email is acceptable as long as no sensitive information is disclosed in the notification.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/620', 1)
        c.question_id = 11
        c.kb_id = 620
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.4', 'Verify impersonation resistance against phishing, such as the use of multi-factor authentication, cryptographic devices with intent (such as connected keys with a push to authenticate), or at higher AAL levels, client-side certificates.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/308', 3)
        c.question_id = 11
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.2.5', 'Verify that where a credential service provider (CSP) and the application verifying authentication are separated, mutually authenticated TLS is in place between the two endpoints.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/319', 3)
        c.question_id = 11
        c.kb_id = 319
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.6', 'Verify replay resistance through the mandated use of OTP devices, cryptographic authenticators, or lookup codes.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/308', 3)
        c.question_id = 11
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.2.7', 'Verify intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a button press on a FIDO hardware key.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/308', 3)
        c.question_id = 11
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.1', 'Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers, and expire after a short period of time. These initial secrets must not be permitted to become the long term password.', 2, False, 'https://cwe.mitre.org/data/definitions/330', 1)
        c.question_id = 12
        c.kb_id = 330
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.2', 'Verify that enrollment and use of subscriber-provided authentication devices are supported, such as a U2F or FIDO tokens.', 2, False, 'https://cwe.mitre.org/data/definitions/308', 2)
        c.question_id = 12
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.3.3', 'Verify that renewal instructions are sent with sufficient time to renew time bound authenticators.', 2, False, 'https://cwe.mitre.org/data/definitions/287', 2)
        c.question_id = 12
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.1', 'Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one- way key derivation or password hashing function. Key derivation and password hashing functions take a password, a salt, and a cost factor as inputs when generating a password hash.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/916', 2)
        c.question_id = 13
        c.kb_id = 916
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.2', 'Verify that the salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/916', 2)
        c.question_id = 13
        c.kb_id = 916
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.3', 'Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/916', 2)
        c.question_id = 13
        c.kb_id = 916
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.4.4', 'Verify that if bcrypt is used, the work factor SHOULD be as large as verification server performance will allow, typically at least 13', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/916', 2)
        c.question_id = 13
        c.kb_id = 916
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.4.5', 'Verify that an additional iteration of a key derivation function is performed, using a salt value that is secret and known only to the verifier. Generate the salt value using an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module).', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/916', 2)
        c.question_id = 13
        c.kb_id = 916
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.1', 'Verify that a system generated initial activation or recovery secret is not sent in clear text to the user.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/640', 1)
        c.question_id = 14
        c.kb_id = 640
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.2', 'Verify password hints or knowledge-based authentication (so-called "secret questions") are not present.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/640', 1)
        c.question_id = 14
        c.kb_id = 640
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.3', 'Verify password credential recovery does not reveal the current password in any way.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/640', 1)
        c.question_id = 14
        c.kb_id = 640
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.4', 'Verify shared or default accounts are not present (e.g. "root", "admin", or "sa").', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 1)
        c.question_id = 14
        c.kb_id = 276
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.5', 'Verify that if an authentication factor is changed or replaced, that the user is notified of this event.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/304', 1)
        c.question_id = 14
        c.kb_id = 304
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.5.6', 'Verify forgotten password, and other recovery paths use a secure recovery mechanism, such as TOTP or other soft token, mobile push, or another offline recovery mechanism. ', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/640', 1)
        c.question_id = 14
        c.kb_id = 640
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.5.7', 'Verify that if OTP or multi-factor authentication factors are lost, that evidence of identity proofing is performed at the same level as during enrollment.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/308', 2)
        c.question_id = 14
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.1', 'Verify that lookup secrets can be used only once.', 2, False, 'https://cwe.mitre.org/data/definitions/308', 2)
        c.question_id = 15
        c.kb_id = 290
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.2', 'Verify that lookup secrets have sufficient randomness (112 bits of entropy), or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash', 2, False, 'https://cwe.mitre.org/data/definitions/330', 2)
        c.question_id = 15
        c.kb_id = 330
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.6.3', 'Verify that lookup secrets are resistant to offline attacks, such as predictable values.', 2, False, 'https://cwe.mitre.org/data/definitions/310', 2)
        c.question_id = 15
        c.kb_id = 310
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.1', 'Verify that clear text out of band (NIST "restricted") authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/287', 1)
        c.question_id = 16
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.2', 'Verify that the out of band verifier expires out of band authentication requests, codes, or tokens after 10 minutes.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/287', 1)
        c.question_id = 16
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.3', 'Verify that the out of band verifier authentication requests, codes, or tokens are only usable once, and only for the original authentication request.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/287', 1)
        c.question_id = 16
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.7.4', 'Verify that the out of band authenticator and verifier communicates over a secure independent channel.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/523', 1)
        c.question_id = 16
        c.kb_id = 523
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.5', 'Verify that the out of band verifier retains only a hashed version of the authentication code.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/256', 2)
        c.question_id = 16
        c.kb_id = 256
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.7.6', 'Verify that the initial authentication code is generated by a secure random number generator, containing at least 20 bits of entropy (typically a six digital random number is sufficient).', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/310', 2)
        c.question_id = 16
        c.kb_id = 310
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.8.1', 'Verify that time-based OTPs have a defined lifetime before expiring.', 2, False, 'https://cwe.mitre.org/data/definitions/613', 1)
        c.question_id = 17
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('2.8.2', 'Verify that symmetric keys used to verify submitted OTPs are highly protected, such as by using a hardware security module or secure operating system based key storage.', 2, False, 'https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 17
        c.kb_id = 320
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.3', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', 2, False, 'https://cwe.mitre.org/data/definitions/326', 2)
        c.question_id = 17
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.4', 'Verify that time-based OTP can be used only once within the validity period.', 2, False, 'https://cwe.mitre.org/data/definitions/287', 2)
        c.question_id = 17
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.5', 'Verify that if a time-based multi factor OTP token is re-used during the validity period, it is logged and rejected with secure notifications being sent to the holder of the device.', 2, False, 'https://cwe.mitre.org/data/definitions/287', 2)
        c.question_id = 17
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.6', 'Verify physical single factor OTP generator can be revoked in case of theft or other loss. Ensure that revocation is immediately effective across logged in sessions, regardless of location.', 2, False, 'https://cwe.mitre.org/data/definitions/613', 2)
        c.question_id = 17 
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.8.7', 'Verify that biometric authenticators are limited to use only as 308 5.2.3 secondary factors in conjunction with either something you have and something you know.', 2, False, 'https://cwe.mitre.org/data/definitions/308', 3)
        c.question_id = 17 
        c.kb_id = 308
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.1', 'Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a TPM or HSM, or an OS service that can use this secure storage.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 18
        c.kb_id = 320
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.2', 'Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/330', 2)
        c.question_id = 18
        c.kb_id = 330
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.9.3', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', 2, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/327', 2)
        c.question_id = 18
        c.kb_id = 327
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.1', 'Verify that integration secrets do not rely on unchanging passwords, such as API keys or shared privileged accounts.', 2, False, "https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/287", 2)
        c.question_id = 19
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.2', 'Verify that if passwords are required, the credentials are not a default account', 2, False, 'https://cwe.mitre.org/data/definitions/255', 2)
        c.question_id = 19
        c.kb_id = 287
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.3', 'Verify that passwords are stored with sufficient protection to prevent offline recovery attacks, including local system access.', 2, False, 'https://cwe.mitre.org/data/definitions/522', 2)
        c.question_id = 19
        c.kb_id = 522
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('2.10.4', 'Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware trusted platform module (TPM), or a hardware security module (L3) is recommended for password storage.', 2, False, 'https://cwe.mitre.org/data/definitions/798', 2)
        c.question_id = 19
        c.kb_id = 798
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.0', 'Session Management Verification Requirements', 3, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.1.1', 'Verify the application never reveals session tokens in URL parameters or error messages.', 3, False, 'https://cwe.mitre.org/data/definitions/598', 1)
        c.question_id = 20
        c.kb_id = 598
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.1', 'Verify the application generates a new session token on user authentication.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/384', 1)
        c.question_id = 21
        c.kb_id = 384
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.2', 'Verify that session tokens possess at least 64 bits of entropy.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/311', 1)
        c.question_id = 21
        c.kb_id = 311
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.2.3', 'Verify the application only stores session tokens in the browser using secure methods such as appropriately secured cookies (see section 3.4) or HTML 5 session storage.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/539', 1)
        c.question_id = 21
        c.kb_id = 539
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.2.4', 'Verify that session token are generated using approved cryptographic algorithms', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/331', 2)
        c.question_id = 21
        c.kb_id = 331
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.1', 'Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/613', 1)
        c.question_id = 22
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.2', 'If authenticators permit users to remain logged in, verify that re-authentication occurs periodically both when actively used or after an idle period.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/613', 1)
        c.question_id = 22
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.3', 'Verify that the application terminates all other active sessions after a successful password change, and that this is effective across the application, federated login (if present) and any relying parties.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/613', 2)
        c.question_id = 22
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.3.4', 'Verify that users are able to view and log out of any or all currently active sessions and devices.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/613', 2)
        c.question_id = 22
        c.kb_id = 613
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.1', 'Verify that cookie-based session tokens have the \Secure\ attribute set.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/614', 1)
        c.question_id = 23
        c.kb_id = 614
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.2', 'Verify that cookie-based session tokens have the \HttpOnly\ attribute set.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1004', 1)
        c.question_id = 23
        c.kb_id = 1004
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.3', 'Verify that cookie-based session tokens utilize the \SameSite\ attribute to limit exposure to cross-site request forgery attacks.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 1)
        c.question_id = 23
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.4', 'Verify that cookie-based session tokens use "__Host-" prefix (see references) to provide session cookie confidentiality.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 1)
        c.question_id = 23
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('3.4.5', 'Verify that if the application is published under a domain name with other applications that set or use session cookies that might override or disclose the session cookies, set the path attribute in cookie-based session tokens using the most precise path possible.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 1)
        c.question_id = 23
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.1', 'Verify the application does not treat OAuth and refresh tokens — on their own — as the presence of the subscriber and allows users to terminate trust relationships with linked applications.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/290', 2)
        c.question_id = 24
        c.kb_id = 290
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.2', 'Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/798', 2)
        c.question_id = 24
        c.kb_id = 798
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.5.3', 'Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/345', 2)
        c.question_id = 24
        c.kb_id = 345
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

        c = ChecklistKB('3.7.1', 'Verify the application ensures a valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications.', 3, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/778', 1)
        c.question_id = 25
        c.kb_id = 778
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.0', 'Access Control Verification Requirements', 4, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.1', 'Verify that the application enforces access control rules on a trusted service layer, especially if client-side access control is present and could be bypassed.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/602', 1)
        c.question_id = 26
        c.kb_id = 602
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.2', 'Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/639', 1)
        c.question_id = 26
        c.kb_id = 639
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.3', 'Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/285', 1)
        c.question_id = 26
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.4', 'Verify that the principle of deny by default exists whereby new users/roles start with minimal or no permissions and users/roles do not receive access to new features until access is explicitly assigned. ', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/276', 1)
        c.question_id = 26
        c.kb_id = 276
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.1.5', 'Verify that access controls fail securely including when an exception occurs.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/285', 1)
        c.question_id = 26
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.2.1', 'Verify that sensitive data and APIs are protected against direct object attacks targeting creation, reading, updating and deletion of records, such as creating or updating someone else\s record, viewing everyone\s records, or deleting all records.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/639',1 )
        c.question_id = 27
        c.kb_id = 639
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.2.2', 'Verify that the application or framework enforces a strong anti-CSRF mechanism to protect authenticated functionality, and effective anti-automation or anti-CSRF protects unauthenticated functionality.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/352', 1)
        c.question_id = 27
        c.kb_id = 352
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.1', 'Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/419', 1)
        c.question_id = 28
        c.kb_id = 419
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.2', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/548', 1)
        c.question_id = 28
        c.kb_id = 548
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('4.3.3', 'Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud.', 4, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/732', 1)
        c.question_id = 28
        c.kb_id = 732
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.0', 'Validation, Sanitization and Encoding Verification Requirements', 5, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.1', 'Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, or environment variables).', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/235', 1)
        c.question_id = 29
        c.kb_id = 235
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.2', 'Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/915', 1)
        c.question_id = 29
        c.kb_id = 915
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.3', 'Verify that all input (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc) is validated using positive validation (whitelisting)', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/20', 1)
        c.question_id = 29
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.4', 'Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as checking that suburb and zip/postcode match).', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/20', 1)
        c.question_id = 29
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.1.5', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/601', 1)
        c.question_id = 29
        c.kb_id = 601
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.1', 'Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 30
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.2', 'Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/138', 1)
        c.question_id = 30
        c.kb_id = 138
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.3', 'Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/147', 1)
        c.question_id = 30
        c.kb_id = 147
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.4', 'Verify that the application avoids the use of eval() or other dynamic code execution features. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/95', 1)
        c.question_id = 30
        c.kb_id = 95
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.5', 'Verify that the application protects against template injection attacks by ensuring that any user input being included is sanitized or sandboxed.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/94', 1)
        c.question_id = 30
        c.kb_id = 94
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.6', 'Verify that the application protects against SSRF attacks, by validating or sanitizing untrusted data or HTTP file metadata, such as filenames and URL input fields, use whitelisting of protocols, domains, paths and ports.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/918', 1)
        c.question_id = 30
        c.kb_id = 918
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.7', 'Verify that the application sanitizes, disables, or sandboxes user-supplied SVG scriptable content, especially as they relate to XSS resulting from inline scripts, and foreignObject.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/159', 1)
        c.question_id = 30
        c.kb_id = 159
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.2.8', 'Verify that the application sanitizes, disables, or sandboxes user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/94', 1)
        c.question_id = 30
        c.kb_id = 94
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.1', 'Verify that output encoding is relevant for the interpreter and context required. For example, use encoders specifically for HTML values, HTML attributes, JavaScript, URL Parameters, HTTP headers, SMTP, and others as the context requires, especially from untrusted inputs (e.g. names with Unicode or apostrophes, such as bla or OHara).', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 31
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.2', 'Verify that output encoding preserves the user\s chosen character set and locale, such that any Unicode character point is valid and safely handled.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/176', 1)
        c.question_id = 31
        c.kb_id = 176
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.3', 'Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/79', 1)
        c.question_id = 31
        c.kb_id = 79
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.4', 'Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from database injection attacks.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/89', 1)
        c.question_id = 33
        c.kb_id = 89
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.5', 'Verify that where parameterized or safer mechanisms are not present, context-specific output encoding is used to protect against injection attacks, such as the use of SQL escaping to protect against SQL injection.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/89', 1)
        c.question_id = 33
        c.kb_id = 89
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.6', 'Verify that the application projects against JavaScript or JSON injection attacks, including for eval attacks, remote JavaScript includes, CSP bypasses, DOM XSS, and JavaScript expression evaluation.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/830', 1)
        c.question_id = 31
        c.kb_id = 830
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.7', 'Verify that the application protects against LDAP Injection vulnerabilities, or that specific security controls to prevent LDAP Injection have been implemented.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/943', 1)
        c.question_id = 34
        c.kb_id = 943
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.8', 'Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/78', 1)
        c.question_id = 35
        c.kb_id = 78
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.9', 'Verify that the application protects against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/829', 1)
        c.question_id = 32
        c.kb_id = 829
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.3.10', 'Verify that the application protects against XPath injection or XML injection attacks.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/643', 1)
        c.question_id = 36
        c.kb_id = 643
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

        c = ChecklistKB('5.5.1', 'Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/502', 1)
        c.question_id = 37
        c.kb_id = 502
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.2', 'Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XXE.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/611',1 )
        c.question_id = 37
        c.kb_id = 611
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.3', 'Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/502', 1)
        c.question_id = 37
        c.kb_id = 502
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('5.5.4', 'Verify that when parsing JSON in browsers or JavaScript-based backends, JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON.', 5, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/95', 1)
        c.question_id = 37
        c.kb_id = 95
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.0', 'Stored Cryptography Verification Requirements', 6, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.1.1', 'Verify that regulated private data is stored encrypted while at rest, such as personally identifiable information (PII), sensitive personal information, or data assessed likely to be subject to EUs GDPR.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/311', 2)
        c.question_id = 38
        c.kb_id = 311
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.1.2', 'Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/311', 2)
        c.question_id = 38
        c.kb_id = 311
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.1.3', 'Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/311', 2)
        c.question_id = 38
        c.kb_id = 311
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.1', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/310', 1)
        c.question_id = 39
        c.kb_id = 310
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.2', 'Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/327', 2)
        c.question_id = 39
        c.kb_id = 327
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.2.3', 'Verify that encryption initialization vector, cipher configuration, and block modes are configured securely using the latest advice.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 2)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.4', 'Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 2)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.5', 'Verify that known insecure block modes (i.e. ECB, etc.), padding modes (i.e. PKCS#1 v1.5, etc.), ciphers with small block sizes (i.e. Triple-DES, Blowfish, etc.), and weak hashing algorithms (i.e. MD5, SHA1, etc.) are not used unless required for backwards compatibility.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 2)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.6', 'Verify that nonces, initialization vectors, and other single use numbers must not be used more than once with a given encryption key. The method of generation must be appropriate for the algorithm being used.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 2)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.7', 'Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 3)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.2.8', 'Verify that all cryptographic operations are constant-time, with no short-circuit operations in comparisons, calculations, or returns, to avoid leaking information', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 3)
        c.question_id = 39
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.1', 'Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic modules approved cryptographically secure random number generator when these random values are intended to be not guessable by an attacker.', 6, False, 'https://cwe.mitre.org/data/definitions/338', 2)
        c.question_id = 40
        c.kb_id = 338
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.2', 'Verify that random GUIDs are created using the GUID v4 algorithm, and a cryptographically-secure pseudo-random number generator (CSPRNG). GUIDs created using other pseudo-random number generators may be predictable.', 6, False, 'https://cwe.mitre.org/data/definitions/338', 2)
        c.question_id = 40
        c.kb_id = 338
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.3.3', 'Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances.', 6, False, 'https://cwe.mitre.org/data/definitions/338', 3)
        c.question_id = 40
        c.kb_id = 338
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.4.1', 'Verify that a secrets management solution such as a key vault is used to securely create, store, control access to and destroy secrets.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/798', 2)
        c.question_id = 41
        c.kb_id = 798
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('6.4.2', 'Verify that key material is not exposed to the application but instead uses an isolated security module like a vault for cryptographic operations.', 6, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/320', 2)
        c.question_id = 41
        c.kb_id = 320
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.0', 'Error Handling and Logging Verification Requirements', 7, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('7.1.1', 'Verify that the application does not log credentials or payment details. Session tokens should only be stored in logs in an irreversible, hashed form.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/532', 1)
        c.question_id = 42
        c.kb_id = 532
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.2', 'Verify that the application does not log other sensitive data as defined under local privacy laws or relevant security policy.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/532', 1)
        c.question_id = 42
        c.kb_id = 532
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.3', 'Verify that the application logs security relevant events including successful and failed authentication events, access control failures, deserialization failures and input validation failures.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/778', 2)
        c.question_id = 42
        c.kb_id = 778
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.1.4', 'Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/778', 2)
        c.question_id = 42
        c.kb_id = 778
        db.session.add(c)
        db.session.commit()     

        c = ChecklistKB('7.2.1', 'Verify that all authentication decisions are logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/778', 2)
        c.question_id = 43
        c.kb_id = 778
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.2.2', 'Verify that all access control decisions can be logged and all failed decisions are logged. This should include requests with relevant metadata needed for security investigations.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/285', 2)
        c.question_id = 43
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.1', 'Verify that the application appropriately encodes user-supplied data to prevent log injection', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/117', 2)
        c.question_id = 44
        c.kb_id = 117
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.2', 'Verify that all events are protected from injection when viewed in log viewing software', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/117', 2)
        c.question_id = 44
        c.kb_id = 117
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.3', 'Verify that security logs are protected from unauthorized access and modification.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/200', 2)
        c.question_id = 44
        c.kb_id = 200
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.3.4', 'Verify that time sources are synchronized to the correct time and time zone. Strongly consider logging only in UTC if systems are global to assist with post- incident forensic analysis.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html', 2)
        c.question_id = 44
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.1', 'Verify that a generic message is shown when an unexpected or security sensitive error occurs, potentially with a unique ID which support personnel can use to investigate.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/210', 1)
        c.question_id = 45
        c.kb_id = 210
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.2', 'Verify that exception handling (or a functional equivalent) is used across the codebase to account for expected and unexpected error conditions.', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/544', 2)
        c.question_id = 45
        c.kb_id = 544
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.4.3', 'Verify that a last resort error handler is defined which will catch all unhandled exceptions', 7, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/460', 2)
        c.question_id = 45
        c.kb_id = 460
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.0', 'Error Handling and Logging Verification Requirements', 8, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.1.1', 'Verify the application protects sensitive data from being cached in server components such as load balancers and application caches.', 8, False, 'https://cwe.mitre.org/data/definitions/532', 2)
        c.question_id = 46
        c.kb_id = 532
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.2', 'Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.', 8, False, 'https://cwe.mitre.org/data/definitions/524', 2)
        c.question_id = 19
        c.kb_id = 524
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.3', 'Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values.', 8, False, 'https://cwe.mitre.org/data/definitions/233', 2)
        c.question_id = 46
        c.kb_id = 233
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.4', 'Verify the application can detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application.', 8, False, 'https://cwe.mitre.org/data/definitions/525', 2)
        c.question_id = 46
        c.kb_id = 525
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.5', 'Verify that regular backups of important data are performed and that test restoration of data is performed.', 8, False, 'https://cwe.mitre.org/data/definitions/770', 3)
        c.question_id = 46
        c.kb_id = 770
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.1.6', 'Verify that backups are stored securely to prevent data from being stolen or corrupted.', 8, False, 'https://cwe.mitre.org/data/definitions/19', 3)
        c.question_id = 46
        c.kb_id = 300
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.2.1', 'Verify the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers.', 8, False, 'https://cwe.mitre.org/data/definitions/525', 1)
        c.question_id = 25
        c.kb_id = 525
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.2.2', 'Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII.', 8, False, 'https://cwe.mitre.org/data/definitions/922', 1)
        c.question_id = 47
        c.kb_id = 922
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.2.3', 'Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated.', 8, False, 'https://cwe.mitre.org/data/definitions/922', 1)
        c.question_id = 47
        c.kb_id = 922
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.1', 'Verify that sensitive data is sent to the server in the HTTP message body or headers, and that query string parameters from any HTTP verb do not contain sensitive data.', 8, False, 'https://cwe.mitre.org/data/definitions/319', 1)
        c.question_id = 48
        c.kb_id = 319
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.2', 'Verify that users have a method to remove or export their data on demand.', 8, False, 'https://cwe.mitre.org/data/definitions/212', 1)
        c.question_id = 48
        c.kb_id = 212
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.3', 'Verify that users are provided clear language regarding collection and use of supplied personal information and that users have provided opt-in consent for the use of that data before it is used in any way.', 8, False, 'https://cwe.mitre.org/data/definitions/285', 1)
        c.question_id = 48
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('8.3.4', 'Verify that all sensitive data created and processed by the application has been identified, and ensure that a policy is in place on how to deal with sensitive data.', 8, False, 'https://cwe.mitre.org/data/definitions/200', 1)
        c.question_id = 48
        c.kb_id = 200
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.5', 'Verify accessing sensitive data is audited (without logging the sensitive data itself), if the data is collected under relevant data protection directives or where logging of access is required.', 8, False, 'https://cwe.mitre.org/data/definitions/532', 2)
        c.question_id = 48
        c.kb_id = 532
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.6', 'Verify that sensitive information contained in memory is overwritten as soon as it is no longer required to mitigate memory dumping attacks, using zeroes or random data.', 8, False, 'https://cwe.mitre.org/data/definitions/226', 2)
        c.question_id = 48
        c.kb_id = 226
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.7', 'Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity', 8, False, 'https://cwe.mitre.org/data/definitions/525', 2)
        c.question_id = 48
        c.kb_id = 525
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('8.3.8', 'Verify that sensitive personal information is subject to data retention classification, such that old or out of date data is deleted automatically, on a schedule, or as the situation requires.', 8, False, 'https://cwe.mitre.org/data/definitions/285', 2)
        c.question_id = 48
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.0', 'Communications Verification Requirements', 9, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.1', 'Verify that secured TLS is used for all client connectivity, and does not fall back to insecure or unencrypted protocols.', 9, False, 'https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/319',1 )
        c.question_id = 49
        c.kb_id = 319
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.2', 'Verify using online or up to date TLS testing tools that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred.', 9, False, 'https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 1)
        c.question_id = 49
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.1.3', 'Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are disabled, such as SSLv2, SSLv3, or TLS 1.0 and TLS 1.1. The latest version of TLS should be the preferred cipher suite.', 9, False, 'https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/326', 1)
        c.question_id = 49
        c.kb_id = 326
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.1', 'Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected.', 9, False, 'https://cwe.mitre.org/data/definitions/295', 2)
        c.question_id = 50
        c.kb_id = 295
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.2.2', 'Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols.', 9, False, 'https://cwe.mitre.org/data/definitions/319', 2)
        c.question_id = 50
        c.kb_id = 319
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('9.2.3', 'Verify that all encrypted connections to external systems that involve sensitive information or functions are authenticated.', 9, False, 'https://cwe.mitre.org/data/definitions/297', 2)
        c.question_id = 50
        c.kb_id = 297
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.4', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured.', 9, False, 'https://cwe.mitre.org/data/definitions/299', 2)
        c.question_id = 50
        c.kb_id = 299
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('9.2.5', 'Verify that backend TLS connection failures are logged', 9, False, 'https://cwe.mitre.org/data/definitions/544', 3)
        c.question_id = 50
        c.kb_id = 544
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.0', 'Malicious Code Verification Requirements', 10, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.1.1', 'Verify that a code analysis tool is in use that can detect potentially malicious code, such as time functions, unsafe file operations and network connections.', 10, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/749', 3)
        c.question_id = 51
        c.kb_id = 749
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.2.1', 'Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the users permission for it to operate before collecting any data.', 10, False, 'https://cwe.mitre.org/data/definitions/359', 2)
        c.question_id = 52
        c.kb_id = 359
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.2', 'Verify that the application does not ask for unnecessary or excessive permissions to privacy related features or sensors, such as contacts, cameras, microphones, or location.', 10, False, 'https://cwe.mitre.org/data/definitions/272', 2)
        c.question_id = 52
        c.kb_id = 272
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.3', 'Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, rootkits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered.', 10, False, 'https://cwe.mitre.org/data/definitions/507', 3)
        c.question_id = 52
        c.kb_id = 507
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.4', 'Verify that the application source code and third party libraries does not contain time bombs by searching for date and time related functions.', 10, False, 'https://cwe.mitre.org/data/definitions/511', 3)
        c.question_id = 52
        c.kb_id = 511
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.5', 'Verify that the application source code and third party libraries does not contain malicious code, such as salami attacks, logic bypasses, or logic bombs.', 10, False, 'https://cwe.mitre.org/data/definitions/511', 3)
        c.question_id = 52
        c.kb_id = 511
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.2.6', 'Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality.', 10, False, 'https://cwe.mitre.org/data/definitions/507', 3)
        c.question_id = 52
        c.kb_id = 507
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('10.3.1', 'Verify that if the application has a client or server auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update.', 10, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 1)
        c.question_id = 53
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.3.2', 'Verify that the application employs integrity protections, such as code signing or sub-resource integrity. The application must not load or execute code from untrusted sources, such as loading includes, modules, plugins, code, or libraries from untrusted sources or the Internet.', 10, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/353', 1)
        c.question_id = 53
        c.kb_id = 353
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('10.3.3', 'Verify that the application has protection from sub-domain takeovers if the application relies upon DNS entries or DNS sub-domains, such as expired domain names, out of date DNS pointers or CNAMEs, expired projects at public source code repos, or transient cloud APIs, serverless functions, or storage buckets (autogen-bucket-id.cloud.example.com) or similar. Protections can include ensuring that DNS names used by applications are regularly checked for expiry or change.', 10, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/350', 1)
        c.question_id = 53
        c.kb_id = 350
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.0', 'Business Logic Verification Requirements', 11, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.1', 'Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.', 11, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/841', 1)
        c.question_id = 54
        c.kb_id = 841
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.2', 'Verify the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.', 11, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/779', 1)
        c.question_id = 54
        c.kb_id = 779
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.3', 'Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis.', 11, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/770', 1)
        c.question_id = 54
        c.kb_id = 770
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.4', 'Verify the application has sufficient anti-automation controls to detect and protect against data exfiltration, excessive business logic requests, excessive file uploads or denial of service attacks.', 11, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/770', 1)
        c.question_id = 54
        c.kb_id = 770
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.5', 'Verify the application has business logic limits or validation to protect against likely business risks or threats, identified using threat modelling or similar methodologies.', 11, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/841', 1)
        c.question_id = 54
        c.kb_id = 841
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.6', 'Verify the application does not suffer from "time of check to time of use" (TOCTOU) issues or other race conditions for sensitive operations.', 11, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/367', 2)
        c.question_id = 54
        c.kb_id = 367
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.7', 'Verify the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt', 11, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/754', 2)
        c.question_id = 54
        c.kb_id = 754
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('11.1.8', 'Verify the application has configurable alerting when automated attacks or unusual activity is detected.', 11, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/390', 2)
        c.question_id = 54
        c.kb_id = 390
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.0', 'File and Resources Verification Requirements', 12, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.1.1', 'Verify that the application will not accept large files that could fill up storage or cause a denial of service attack.', 12, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/400', 1)
        c.question_id = 55
        c.kb_id = 400
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.1.2', 'Verify that compressed files are checked for "zip bombs" - small input files that will decompress into huge files thus exhausting file storage limits.', 12, False, 'https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/400', 2)
        c.question_id = 55
        c.kb_id = 400
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.1.3', 'Verify that a file size quota and maximum number of files per user is enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files.', 12, False, 'https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/409', 2)
        c.question_id = 55
        c.kb_id = 409
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.2.1', 'Verify that files obtained from untrusted sources are validated to be of expected type based on the files content.', 12, False, 'https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/434', 2)
        c.question_id = 56
        c.kb_id = 434
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.3.1', 'Verify that user-submitted filename metadata is not used directly with system or framework file and URL API to protect against path traversal.', 12, False, 'https://cwe.mitre.org/data/definitions/22', 1)
        c.question_id = 57
        c.kb_id = 22
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.2', 'Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI).', 12, False, 'https://cwe.mitre.org/data/definitions/73', 1)
        c.question_id = 57
        c.kb_id = 73
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.3', 'Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files (RFI) which may also lead to SSRF.', 12, False, 'https://cwe.mitre.org/data/definitions/98', 1)
        c.question_id = 57
        c.kb_id = 98
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.4', 'Verify that the application protects against reflective file download (RFD) by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter, the response Content-Type header should be set to text/plain, and the Content-Disposition header should have a fixed filename.', 12, False, 'https://cwe.mitre.org/data/definitions/641', 1)
        c.question_id = 57
        c.kb_id = 641
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.3.5', 'Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection.', 12, False, 'https://cwe.mitre.org/data/definitions/78', 1)
        c.question_id = 57
        c.kb_id = 78
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('12.3.6', 'Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs.', 12, False, 'https://cwe.mitre.org/data/definitions/829', 2)
        c.question_id = 57
        c.kb_id = 829
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.4.1', 'Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation.', 12, False, 'https://cwe.mitre.org/data/definitions/922', 1)
        c.question_id = 58
        c.kb_id = 922
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.4.2', 'Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload of known malicious content.', 12, False, 'https://cwe.mitre.org/data/definitions/509', 1)
        c.question_id = 58
        c.kb_id = 509
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.5.1', 'Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak) temporary working files (e.g. .swp) compressed files (.zip, .tar.gz, etc) and other extensions commonly used by editors should be blocked unless required.', 12, False, 'https://cwe.mitre.org/data/definitions/552', 1)
        c.question_id = 59
        c.kb_id = 552
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.5.2', 'Verify that direct requests to uploaded files will never be executed as HTML/JavaScript content.', 12, False, 'https://cwe.mitre.org/data/definitions/434', 1)
        c.question_id = 59
        c.kb_id = 434
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('12.6.1', 'Verify that the web or application server is configured with a whitelist of resources or systems to which the server can send requests or load data/files from.', 12, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/918', 1)
        c.question_id = 60
        c.kb_id = 918
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.0', 'API and Web Service Verification Requirements', 13, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.1', 'Verify that all application components use the same encodings and parsers to avoid parsing attacks that exploit different URI or file parsing behavior that could be used in SSRF and RFI attacks.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 61
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.2', 'Verify that access to administration and management functions is limited to authorized administrators.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/419', 1)
        c.question_id = 61
        c.kb_id = 419
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.1.3', 'Verify API URLs do not expose sensitive information, such as the API key, session tokens etc.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/598', 1)
        c.question_id = 61
        c.kb_id = 598
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.1.4', 'Verify that authorization decisions are made at both the URI, enforced by programmatic or declarative security at the controller or router, and at the resource level, enforced by model-based permissions.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/285', 2)
        c.question_id = 61
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.1.5', 'Verify that requests containing unexpected or missing content types are rejected with appropriate headers (HTTP response status 406 Unacceptable or 415 Unsupported Media Type).', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/434', 2)
        c.question_id = 61
        c.kb_id = 434
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.1', 'Verify that enabled RESTful HTTP methods are a valid choice for the user or action, such as preventing normal users using DELETE or PUT on protected API or resources.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/650', 1)
        c.question_id = 62
        c.kb_id = 650
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.2', 'Verify that JSON schema validation is in place and verified before accepting input.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/20', 1)
        c.question_id = 62
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.2.3', 'Verify that RESTful web services that utilize cookies are protected from Cross-Site Request Forgery via the use of at least one or more of the following: triple or double submit cookie pattern, CSRF nonces, or ORIGIN request header checks.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/352', 1)
        c.question_id = 62
        c.kb_id = 352
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.2.4', 'Verify that REST services have anti-automation controls to protect against excessive calls, especially if the API is unauthenticated.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/779', 2)
        c.question_id = 62
        c.kb_id = 779
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.2.5', 'Verify that REST services explicitly check the incoming Content-Type to be the expected one, such as application/xml or application/JSON.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/436', 2)
        c.question_id = 62
        c.kb_id = 436
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('13.2.6', 'Verify that the message headers and payload are trustworthy and not modified in transit. Requiring strong encryption for transport (TLS only) may be sufficient in many cases as it provides both confidentiality and integrity protection. Per- message digital signatures can provide additional assurance on top of the transport protections for high-security applications but bring with them additional complexity and risks to weigh against the benefits', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/598', 2)
        c.question_id = 62
        c.kb_id = 598
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.3.1', 'Verify that XSD schema validation takes place to ensure a properly formed XML document, followed by validation of each input field before any processing of that data takes place.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/20', 1)
        c.question_id = 63
        c.kb_id = 20
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('13.3.2', 'Verify that the message payload is signed using WS-Security to ensure reliable transport between client and service.', 13, False, 'https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/345', 2)
        c.question_id = 63
        c.kb_id = 345
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.4.1', 'Verify that query whitelisting or a combination of depth limiting and amount limiting should be used to prevent GraphQL or data layer expression denial of service (DoS) as a result of expensive, nested queries. For more advanced scenarios, query cost analysis should be used.', 13, False, 'https://cwe.mitre.org/data/definitions/770', 2)
        c.question_id = 64
        c.kb_id = 770
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('13.4.2', 'Verify that GraphQL or other data layer authorization logic should be implemented at the business logic layer instead of the GraphQL layer.', 13, False, 'https://cwe.mitre.org/data/definitions/285', 2)
        c.question_id = 64
        c.kb_id = 285
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.0', 'Configuration Verification Requirements', 14, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.1.1', 'Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html', 2)
        c.question_id = 65
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.1.2', 'Verify that compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/120', 2)
        c.question_id = 65
        c.kb_id = 120
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.3', 'Verify that server configuration is hardened as per the recommendations of the application server and frameworks in use.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/16', 2)
        c.question_id = 65
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.4', 'Verify that the application, configuration, and all dependencies can be re- deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html', 2)
        c.question_id = 65
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.1.5', 'Verify that authorized administrators can verify the integrity of all security-relevant configurations to detect tampering.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html', 3)
        c.question_id = 65
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.1', 'Verify that all components are up to date, preferably using a dependency checker during build or compile time.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1104', 1)
        c.question_id = 65
        c.kb_id = 1104
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.2.2', 'Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/531', 1)
        c.question_id = 66
        c.kb_id = 531
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.2.3', 'Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset.', 14, False, 'https://cwe.mitre.org/data/definitions/15', 1)
        c.question_id = 66
        c.kb_id = 15
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.4', 'Verify that third party components come from pre-defined, trusted and continually maintained repositories', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/828', 2)
        c.question_id = 66
        c.kb_id = 828
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.5', 'Verify that an inventory catalog is maintained of all third party libraries in use.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html', 2)
        c.question_id = 66
        c.kb_id = 2
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.2.6', 'Verify that the attack surface is reduced by sandboxing or encapsulating third party libraries to expose only the required behaviour into the application.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html,https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/265', 2)
        c.question_id = 66
        c.kb_id = 265
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.1', 'Verify that web or application server and framework error messages are configured to deliver user actionable, customized responses to eliminate any unintended security disclosures.', 14, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/209', 1)
        c.question_id = 67
        c.kb_id = 209
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.2', 'Verify that web or application server and application framework debug modes are disabled in production to eliminate debug features, developer consoles, and unintended security disclosures.', 14, True, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/497', 1)
        c.question_id = 67
        c.kb_id = 497
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.3.3', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/200', 1)
        c.question_id = 67
        c.kb_id = 200
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.1', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1).', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/173', 1)
        c.question_id = 68
        c.kb_id = 173
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.2', 'Verify that all API responses contain Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type).', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 68
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.3', 'Verify that a content security policy (CSPv2) is in place that helps mitigate impact for XSS attacks like HTML, DOM, JSON, and JavaScript injection vulnerabilities.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/1021', 1)
        c.question_id = 68
        c.kb_id = 1021
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.4', 'Verify that all responses contain X-Content-Type-Options: nosniff.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 68
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.5', 'Verify that HTTP Strict Transport Security headers are included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/523', 1)
        c.question_id = 68
        c.kb_id = 523
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.6', 'Verify that a suitable "Referrer-Policy" header is included, such as "no-referrer" or "same-origin".', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/116', 1)
        c.question_id = 68
        c.kb_id = 116
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.4.7', 'Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a third-party site.', 14, False, 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html,https://cwe.mitre.org/data/definitions/346', 1)
        c.question_id = 68
        c.kb_id = 346
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.1', 'Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS.', 14, False, 'https://cwe.mitre.org/data/definitions/749', 1)
        c.question_id = 69
        c.kb_id = 749
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.2', 'Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker.', 14, False, 'https://cwe.mitre.org/data/definitions/346', 1)
        c.question_id = 69
        c.kb_id = 346
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('14.5.3', 'Verify that the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header uses a strict white-list of trusted domains to match against and does not support the "null" origin.', 14, False, 'https://cwe.mitre.org/data/definitions/346', 1)
        c.question_id = 69
        c.kb_id = 346
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('14.5.4', 'Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application.', 14, False, 'https://cwe.mitre.org/data/definitions/306', 2)
        c.question_id = 69
        c.kb_id = 306
        db.session.add(c)
        db.session.commit()
        
        db.session.add(LabItem('Path traversal (LFI)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-1-filename-injection', 1, 'lfi', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Cross Site Scripting','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting', 1, 'xss', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Cross site scripting (attribute)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting-attribute', 1, 'xss-attribute', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Cross site scripting (href)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-3-cross-site-scripting-href', 1, 'xss-url', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('XSSI','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-include-files-from-untrusted-sources-js', 2, 'untrusted-sources-js', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Cross site request forgery','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-5-csrf', 3, 'csrf', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Cross site request forgery (same site)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-5-csrf-samesite', 3, 'csrf-samesite', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('External entity attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-6-xxe', 2, 'xxe', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Insecure file upload','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-13-file-upload', 1, 'file-upload', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Clickjacking','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-20-clickjacking', 1, 'x-allow-origin', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Rate-limiting','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-29-ratelimiting', 1, 'ratelimiting', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('HttpOnly (session hijacking)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-39-httponly-session-hijacking-xss', 3, 'session-hijacking-xss', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Missing authorization','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-44-authorisation-missing', 2, 'auth-missing', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Exposed Docker daemon','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-45-exposed-docker', 3, 'none', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('SQLI (union select)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-46-sqli-union-select', 2, 'sqli', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Open redirect (hard)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-67-open-redirect-hard', 3, 'url-redirection-harder', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('CORS exploitation','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-112-cors-exploitation', 3, 'cors', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Formulla injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-95-formula-injection', 1, 'formula-injection', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Mass assingment attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-147-parameter-binding', 1, 'parameter-binding', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('SQLI -like','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-156-sqli-like', 2, 'sqli-like', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('SQLI-blind','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-156-sqli-blind', 3, 'sqli-blind', 'SKF-labs', None))
        db.session.commit()
                
        db.session.add(LabItem('Remote file inclusion 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-173-remote-file-inclusion', 1, 'rfi', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Remote file inclusion 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-173-lfi-2', 1, 'lfi-2', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Remote file inclusion 3','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-173-lfi-3', 1, 'lfi-3', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Content security policiy','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-178-content-security-policy', 1, 'csp', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Server side request forgery','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-262-server-side-request-forgery', 3, 'ssrf', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Tabnabbing','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-266-tabnabbing', 2, 'tabnabbing', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Server side template injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-267-server-side-template-injection', 3, 'ssti', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Insecure direct object reference','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-268-insecure-direct-object-references', 2, 'idor', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('JWT null','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-7006-jwt-null', 2, 'jwt-null', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('JWT weak secret','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-7006-jwt-secret', 2, 'jwt-secret', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Insecure deserialization (yaml)','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-deserialisation-yaml', 3, 'des-yaml', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Insecure deserialization pickle','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-des-pickle-2', 3, 'des-pickle-2', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Race condition','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-race-condition', 3, 'racecondition', 'SKF-labs', None))
        db.session.commit()
        
        db.session.add(LabItem('Regex Ddos','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-dos-regex', 1, 'dos-regex', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Command injection 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-cmd-injection-1', 1, 'cmd', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Command injection 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-cmd-injection-2', 1, 'cmd2', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Information disclosure 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-information-leakeage-comments', 1, 'info-leakeage-comments', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Information disclosure 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-information-leakeage-metadata', 1, 'info-leakeage-metadata', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Authentication bypass 1','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-auth-bypass-1', 1, 'auth-bypass-1', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Authentication bypass 2','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-auth-bypass-2', 1, 'auth-bypass-2', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Blind command injection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-blind-cmd-injection-1', 2, 'cmd3', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Right to left override attack','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-xxx-right-to-left-override', 1, 'rtlo', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('Session puzzeling','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-250-session-puzzling', 3, 'sessionpuzzle', 'SKF-labs', None))
        db.session.commit()


        db.session.add(LabItem('Graphql DOS','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-285-graphql-dos', 3, 'graphql-dos-resource-exhaustion', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('GraphQL IDOR','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-285-graphql-idor', 3, 'graphql-idor', 'SKF-labs', None))
        db.session.commit()


        db.session.add(LabItem('GraphQL Injections','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-285-graphql-injections', 3, 'graphql-injections', 'SKF-labs', None))
        db.session.commit()


        db.session.add(LabItem('GraphQL Introspection','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-285-graphql-introspection', 3, 'graphql-info-introspection', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('GraphQL Mutations','https://owasp-skf.gitbook.io/asvs-write-ups/kbid-285-graphql-mutations', 3, 'graphql-mutation', 'SKF-labs', None))
        db.session.commit()

        db.session.add(LabItem('API-only XSS','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-persisted-xss-attack-without-using-the-frontend-application-at-all',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Access Log','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#gain-access-to-any-access-log-file-of-the-server',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Admin Registration','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#register-as-a-user-with-administrator-privileges',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Admin Section','https://pwning.owasp-juice.shop/part2/broken-access-control.html#access-the-administration-section-of-the-store',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Arbitrary File Write','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#overwrite-the-legal-information-file',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Bjoerns Favorite Pet','https://pwning.owasp-juice.shop/part2/broken-authentication.html#reset-the-password-of-bjoerns-owasp-account-via-the-forgot-password-mechanism',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Blockchain Hype','https://pwning.owasp-juice.shop/part2/security-through-obscurity.html#learn-about-the-token-sale-before-its-official-announcement',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Blocked RCE DoS','https://pwning.owasp-juice.shop/part2/insecure-deserialization.html#perform-a-remote-code-execution-that-would-keep-a-less-hardened-application-busy-forever',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('CAPTCHA Bypass','https://pwning.owasp-juice.shop/part2/broken-anti-automation.html#submit-10-or-more-customer-feedbacks-within-10-seconds',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Change Benders Password','https://pwning.owasp-juice.shop/part2/broken-authentication.html#change-benders-password-into-slurmcl4ssic-without-using-sql-injection-or-forgot-password',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Christmas Special','https://pwning.owasp-juice.shop/part2/injection.html#order-the-christmas-special-offer-of-2014',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('CSP Bypass','https://pwning.owasp-juice.shop/part2/xss.html#bypass-the-content-security-policy-and-perform-an-xss-attack-on-a-legacy-page',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Client-side XSS Protection','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-persisted-xss-attack-bypassing-a-client-side-security-mechanism',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Confidential Document','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#access-a-confidential-document',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('DOM XSS','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-dom-xss-attack',1,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Database Schema','https://pwning.owasp-juice.shop/part2/injection.html#exfiltrate-the-entire-db-schema-definition-via-sql-injection',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Deprecated Interface','https://pwning.owasp-juice.shop/part2/security-misconfiguration.html#use-a-deprecated-b2b-interface-that-was-not-properly-shut-down',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Easter Egg','https://pwning.owasp-juice.shop/part2/broken-access-control.html#find-the-hidden-easter-egg',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Email Leak','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#perform-an-unwanted-information-disclosure-by-accessing-data-cross-domain',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Ephemeral Accountant','https://pwning.owasp-juice.shop/part2/injection.html#log-in-with-the-non-existing-accountant-without-ever-registering-that-user',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Error Handling','https://pwning.owasp-juice.shop/part2/security-misconfiguration.html#provoke-an-error-that-is-neither-very-gracefully-nor-consistently-handled',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Expired Coupon','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#successfully-redeem-an-expired-campaign-coupon-code',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Extra Language','https://pwning.owasp-juice.shop/part2/broken-anti-automation.html#retrieve-the-language-file-that-never-made-it-into-production',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Five-Star Feedback','https://pwning.owasp-juice.shop/part2/broken-access-control.html#get-rid-of-all-5-star-customer-feedback',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Forged Coupon','https://pwning.owasp-juice.shop/part2/cryptographic-issues.html#forge-a-coupon-code-that-gives-you-a-discount-of-at-least-80',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Forged Feedback','https://pwning.owasp-juice.shop/part2/broken-access-control.html#post-some-feedback-in-another-users-name',3,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Forged Review','https://pwning.owasp-juice.shop/part2/broken-access-control.html#post-a-product-review-as-another-user-or-edit-any-users-existing-review',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Forged Signed JWT','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#forge-an-almost-properly-rsa-signed-jwt-token',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Forgotten Developer Backup','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#access-a-developers-forgotten-backup-file',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Forgotten Sales Backup','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#access-a-salesmans-forgotten-backup-file',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Frontend Typosquatting','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#inform-the-shop-about-a-typosquatting-imposter-that-dug-itself-deep-into-the-frontend',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('GDPR Data Erasure','https://pwning.owasp-juice.shop/part2/broken-authentication.html#log-in-with-chris-erased-user-account',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('GDPR Data Theft','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#steal-someone-elses-personal-data-without-using-injection',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('HTTP-Header XSS','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-persisted-xss-attack-through-an-http-header',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Imaginary Challenge','https://pwning.owasp-juice.shop/part2/cryptographic-issues.html#solve-challenge-2',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Leaked Access Logs','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#dumpster-dive-the-internet-for-a-leaked-password-and-log-in-to-the-original-user-account-it-belongs-to',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Leaked Unsafe Product','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#identify-an-unsafe-product-that-was-removed-from-the-shop-and-inform-the-shop-which-ingredients-are-dangerous',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Legacy Typosquatting','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#inform-the-shop-about-a-typosquatting-trick-it-has-been-a-victim-of',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Login Admin','https://pwning.owasp-juice.shop/part2/injection.html#log-in-with-the-administrators-user-account',2,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Login Amy','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#log-in-with-amys-original-user-credentials',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Login Bender','https://pwning.owasp-juice.shop/part2/injection.html#log-in-with-benders-user-account',3,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Login Bjoern','https://pwning.owasp-juice.shop/part2/broken-authentication.html#log-in-with-bjoerns-gmail-account',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Login CISO','https://pwning.owasp-juice.shop/part2/broken-authentication.html#exploit-oauth-20-to-log-in-with-the-cisos-user-account',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Login Jim','https://pwning.owasp-juice.shop/part2/injection.html#log-in-with-jims-user-account',3,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Login MC SafeSearch','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#log-in-with-mc-safesearchs-original-user-credentials',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Login Support Team','https://pwning.owasp-juice.shop/part2/security-misconfiguration.html#log-in-with-the-support-teams-original-user-credentials',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Manipulate Basket','https://pwning.owasp-juice.shop/part2/broken-access-control.html#put-an-additional-product-into-another-users-shopping-basket',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Misplaced Signature File','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#access-a-misplaced-siem-signature-file',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Multiple Likes','https://pwning.owasp-juice.shop/part2/broken-anti-automation.html#like-any-review-at-least-three-times-as-the-same-user',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Nested Easter Egg','https://pwning.owasp-juice.shop/part2/cryptographic-issues.html#apply-some-advanced-cryptanalysis-to-find-the-real-easter-egg',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('NoSQL DoS','https://pwning.owasp-juice.shop/part2/injection.html#let-the-server-sleep-for-some-time',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('NoSQL Exfiltration','https://pwning.owasp-juice.shop/part2/injection.html#all-your-orders-are-belong-to-us',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('NoSQL Manipulation','https://pwning.owasp-juice.shop/part2/injection.html#update-multiple-product-reviews-at-the-same-time',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Outdated Whitelist','https://pwning.owasp-juice.shop/part2/unvalidated-redirects.html#let-us-redirect-you-to-one-of-our-crypto-currency-addresses',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Password Strength','https://pwning.owasp-juice.shop/part2/broken-authentication.html#log-in-with-the-administrators-user-credentials-without-previously-changing-them-or-applying-sql-injection',2,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Payback Time','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#place-an-order-that-makes-you-rich',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Premium Paywall','https://pwning.owasp-juice.shop/part2/cryptographic-issues.html#unlock-premium-challenge-to-access-exclusive-content',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Privacy Policy','https://pwning.owasp-juice.shop/part2/miscellaneous.html#read-our-privacy-policy',1,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Privacy Policy Inspection','https://pwning.owasp-juice.shop/part2/security-through-obscurity.html#prove-that-you-actually-read-our-privacy-policy',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Product Tampering','https://pwning.owasp-juice.shop/part2/broken-access-control.html#change-the-href-of-the-link-within-the-o-saft-product-description',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Reflected XSS','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-reflected-xss-attack',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Repetitive Registration','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#follow-the-dry-principle-while-registering-a-user',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Reset Benders Password','https://pwning.owasp-juice.shop/part2/broken-authentication.html#reset-benders-password-via-the-forgot-password-mechanism',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Reset Bjoerns Password','https://pwning.owasp-juice.shop/part2/broken-authentication.html#reset-the-password-of-bjoerns-internal-account-via-the-forgot-password-mechanism',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Reset Jims Password','https://pwning.owasp-juice.shop/part2/broken-authentication.html#reset-jims-password-via-the-forgot-password-mechanism',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Reset Mortys Password','https://pwning.owasp-juice.shop/part2/broken-anti-automation.html#reset-mortys-password-via-the-forgot-password-mechanism',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Retrieve Blueprint','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#deprive-the-shop-of-earnings-by-downloading-the-blueprint-for-one-of-its-products',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('SSRF','https://pwning.owasp-juice.shop/part2/broken-access-control.html#request-a-hidden-resource-on-server-through-server',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('SSTi','https://pwning.owasp-juice.shop/part2/injection.html#infect-the-server-with-juicy-malware-by-abusing-arbitrary-command-execution',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Score Board','https://pwning.owasp-juice.shop/part2/score-board.html#find-the-carefully-hidden-score-board-page',1,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Security Policy','https://pwning.owasp-juice.shop/part2/miscellaneous.html#behave-like-any-white-hat-should-before-getting-into-the-action',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Server-side XSS Protection','https://pwning.owasp-juice.shop/part2/xss.html#perform-a-persisted-xss-attack-bypassing-a-server-side-security-mechanism',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Steganography','https://pwning.owasp-juice.shop/part2/security-through-obscurity.html#rat-out-a-notorious-character-hiding-in-plain-sight-in-the-shop',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Successful RCE DoS','https://pwning.owasp-juice.shop/part2/insecure-deserialization.html#perform-a-remote-code-execution-that-occupies-the-server-for-a-while-without-using-infinite-loops',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Supply Chain Attack','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#inform-the-development-team-about-a-danger-to-some-of-their-credentials',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Two Factor Authentication','https://pwning.owasp-juice.shop/part2/broken-authentication.html#solve-the-2fa-challenge-for-user-wurstbrot',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Unsigned JWT','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#forge-an-essentially-unsigned-jwt-token',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Upload Size','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#upload-a-file-larger-than-100-kb',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Upload Type','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#upload-a-file-that-has-no-pdf-or-zip-extension',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('User Credentials','https://pwning.owasp-juice.shop/part2/injection.html#retrieve-a-list-of-all-user-credentials-via-sql-injection',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Video XSS','https://pwning.owasp-juice.shop/part2/xss.html#embed-an-xss-payload-into-our-promo-video',6,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('View Basket','https://pwning.owasp-juice.shop/part2/broken-access-control.html#view-another-users-shopping-basket',2,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Vulnerable Library','https://pwning.owasp-juice.shop/part2/vulnerable-components.html#inform-the-shop-about-a-vulnerable-library-it-is-using',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Weird Crypto','https://pwning.owasp-juice.shop/part2/cryptographic-issues.html#inform-the-shop-about-an-algorithm-or-library-it-should-definitely-not-use-the-way-it-does',2,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Whitelist Bypass','https://pwning.owasp-juice.shop/part2/unvalidated-redirects.html#enforce-a-redirect-to-a-page-you-are-not-supposed-to-redirect-to',4,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('XXE Data Access','https://pwning.owasp-juice.shop/part2/xxe.html#retrieve-the-content-of-cwindowssystemini-or-etcpasswd-from-the-server',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('XXE DoS','https://pwning.owasp-juice.shop/part2/xxe.html#give-the-server-something-to-chew-on-for-quite-a-while',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Zero Stars','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#give-a-devastating-zero-star-feedback-to-the-store',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Missing Encoding','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#retrieve-the-photo-of-bjoerns-cat-in-melee-combat-mode',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Cross-Site Imaging','https://pwning.owasp-juice.shop/part2/injection.html#stick-cute-cross-domain-kittens-all-over-our-delivery-boxes',5,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Exposed Metrics','https://pwning.owasp-juice.shop/part2/sensitive-data-exposure.html#find-the-endpoint-that-serves-usage-data-to-be-scraped-by-a-popular-monitoring-system',1,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Deluxe Fraud','https://pwning.owasp-juice.shop/part2/improper-input-validation.html#obtain-a-deluxe-membership-without-paying-for-it',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('CSRF','https://pwning.owasp-juice.shop/part2/broken-access-control.html#change-the-name-of-a-user-by-performing-cross-site-request-forgery-from-another-origin',3,'juice-shop','juice-shop',None))
        db.session.commit()

        db.session.add(LabItem('Bonus Payload','https://pwning.owasp-juice.shop/part2/xss.html#use-the-bonus-payload-in-the-dom-xss-challenge',1,'juice-shop','juice-shop',True))
        db.session.commit()

        db.session.add(LabItem('Juice Shop CTF','https://owasp.org/www-project-juice-shop/',3,'juice-shop-ctf','juice-shop',None))
        db.session.commit()

        '''
        Checklist controls for MASVS
        '''

        c = ChecklistKB('1.0', 'Architecture, Design and Threat Modeling Requirements', 15, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
            
        c = ChecklistKB('2.0', 'Data Storage and Privacy Requirements', 16, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('3.0', 'Cryptography Requirements', 17, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
            
        c = ChecklistKB('4.0', 'Authentication and Session Management Requirements', 18, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('5.0', 'Network Communication Requirements', 19, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
        
        c = ChecklistKB('6.0', 'Platform Interaction Requirements', 20, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        c = ChecklistKB('7.0', 'Code Quality and Build Setting Requirements', 21, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()
            
        c = ChecklistKB('8.0', 'Resilience Requirements', 22, False, None, None)
        c.question_id = None
        c.kb_id = 1
        db.session.add(c)
        db.session.commit()

        '''
        Checklist Categories for MASVS
        '''


        c = ChecklistKB('1.1', 'All app components are identified and known to be needed.', 15, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-for-insecure-configuration-of-instant-apps-mstg-arch-1,-mstg-arch-7', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.2', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', 15, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#verifying-that-appropriate-authentication-is-in-place-mstg-arch-2-and-mstg-auth-1,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04h-Testing-Code-Quality.md#injection-flaws-mstg-arch-2-and-mstg-platform-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.3', 'A high-level architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', 15, False, '', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.4', 'Data considered sensitive in the context of the mobile app is clearly identified.', 15, False, '', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.5', 'All app components are defined in terms of the business functions and/or security functions they provide.', 15, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.6', 'A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures.', 15, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.7', 'All security controls have a centralized implementation.', 15, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-for-insecure-configuration-of-instant-apps-mstg-arch-1,-mstg-arch-7', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.8', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 800-57.', 15, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.9', 'A mechanism for enforcing updates of the mobile app exists.', 15, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-enforced-updating-mstg-arch-9,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-enforced-updating-mstg-arch-9', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.10', 'Security is addressed within all parts of the software development lifecycle.', 15, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.11', 'A responsible disclosure policy is in place and effectively applied.', 15, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('1.12', 'The app should comply with privacy laws and regulations.', 15, False, '', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.1', 'System credential storage facilities need to be used to store sensitive data, such as PII, user credentials or cryptographic keys.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-local-storage-for-sensitive-data-mstg-storage-1-and-mstg-storage-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#testing-local-data-storage-mstg-storage-1-and-mstg-storage-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.2', 'No sensitive data should be stored outside of the app container or system credential storage facilities.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-local-storage-for-sensitive-data-mstg-storage-1-and-mstg-storage-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#testing-local-data-storage-mstg-storage-1-and-mstg-storage-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.3', 'No sensitive data is written to application logs.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-logs-for-sensitive-data-mstg-storage-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#checking-logs-for-sensitive-data-mstg-storage-3', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.4', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#determining-whether-sensitive-data-is-sent-to-third-parties-mstg-storage-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#determining-whether-sensitive-data-is-sent-to-third-parties-mstg-storage-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.5', 'The keyboard cache is disabled on text inputs that process sensitive data.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#determining-whether-the-keyboard-cache-is-disabled-for-text-input-fields-mstg-storage-5,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#finding-sensitive-data-in-the-keyboard-cache-mstg-storage-5', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.6', 'No sensitive data is exposed via IPC mechanisms.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#determining-whether-sensitive-stored-data-has-been-exposed-via-ipc-mechanisms-mstg-storage-6,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#determining-whether-sensitive-data-is-exposed-via-ipc-mechanisms-mstg-storage-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.7', 'No sensitive data, such as passwords or pins, is exposed through the user interface.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#checking-for-sensitive-data-disclosure-through-the-user-interface-mstg-storage-7,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#checking-for-sensitive-data-disclosed-through-the-user-interface-mstg-storage-7', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.8', 'No sensitive data is included in backups generated by the mobile operating system.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-backups-for-sensitive-data-mstg-storage-8,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#testing-backups-for-sensitive-data-mstg-storage-8', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.9', 'The app removes sensitive data from views when moved to the background.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#finding-sensitive-information-in-auto-generated-screenshots-mstg-storage-9,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#testing-auto-generated-screenshots-for-sensitive-information-mstg-storage-9', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.10', 'The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#checking-memory-for-sensitive-data-mstg-storage-10,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#testing-memory-for-sensitive-data-mstg-storage-10', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.11', 'The app enforces a minimum device-access-security policy, such as requiring the user to set a device passcode.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-the-device-access-security-policy-mstg-storage-11,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md#testing-local-authentication-mstg-auth-8-and-mstg-storage-11', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.12', 'The app educates the user about the types of personally identifiable information processed, as well as security best practices the user should follow in using the app.', 16, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04i-Testing-user-interaction.md#testing-user-education-mstg-storage-12', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.13', 'No sensitive data should be stored locally on the mobile device. Instead, data should be retrieved from a remote endpoint when needed and only be kept in memory.', 16, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.14', 'If sensitive data is still required to be stored locally, it should be encrypted using a key derived from hardware backed storage which requires authentication.', 16, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('2.15', 'The app’s local storage should be wiped after an excessive number of failed authentication attempts.', 16, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md#testing-key-management-mstg-crypto-1-and-mstg-crypto-5,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04g-Testing-Cryptography.md#common-configuration-issues-mstg-crypto-1,-mstg-crypto-2-and-mstg-crypto-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-symmetric-cryptography-mstg-crypto-1', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.2', 'The app uses proven implementations of cryptographic primitives.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md#verifying-the-configuration-of-cryptographic-standard-algorithms-mstg-crypto-2-and-mstg-crypto-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04g-Testing-Cryptography.md#common-configuration-issues-mstg-crypto-1,-mstg-crypto-2-and-mstg-crypto-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-the-configuration-of-cryptographic-standard-algorithms-mstg-crypto-2,-mstg-crypto-3-and-mstg-crypto-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.3', 'The app uses cryptographic primitives that are appropriate for the particular use-case, configured with parameters that adhere to industry best practices.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md#verifying-the-configuration-of-cryptographic-standard-algorithms-mstg-crypto-2-and-mstg-crypto-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04g-Testing-Cryptography.md#common-configuration-issues-mstg-crypto-1,-mstg-crypto-2-and-mstg-crypto-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-the-configuration-of-cryptographic-standard-algorithms-mstg-crypto-2,-mstg-crypto-3-and-mstg-crypto-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered deprecated for security purposes.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04g-Testing-Cryptography.md#identifying-insecure-and/or-deprecated-cryptographic-algorithms-mstg-crypto-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-the-configuration-of-cryptographic-standard-algorithms-mstg-crypto-2,-mstg-crypto-3-and-mstg-crypto-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.5', 'The app doesn\'t re-use the same cryptographic key for multiple purposes.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md#testing-key-management-mstg-crypto-1-and-mstg-crypto-5,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-the-purposes-of-keys-mstg-crypto-5', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('3.6', 'All random values are generated using a sufficiently secure random number generator.', 17, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md#testing-random-number-generation-mstg-crypto-6,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md#testing-random-number-generation-mstg-crypto-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.1', 'If the app provides users access to a remote service, some form of authentication, such as username/password authentication, is performed at the remote endpoint.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#verifying-that-appropriate-authentication-is-in-place-mstg-arch-2-and-mstg-auth-1,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-oauth-2.0-flows-mstg-auth-1-and-mstg-auth-3', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.2', 'If stateful session management is used, the remote endpoint uses randomly generated session identifiers to authenticate client requests without sending the user\'s credentials.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-stateful-session-management-mstg-auth-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.3', 'If stateless token-based authentication is used, the server provides a token that has been signed using a secure algorithm.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-stateless-(token-based)-authentication-mstg-auth-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-oauth-2.0-flows-mstg-auth-1-and-mstg-auth-3', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.4', 'The remote endpoint terminates the existing session when the user logs out.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-user-logout-mstg-auth-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.5', 'A password policy exists and is enforced at the remote endpoint.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-best-practices-for-passwords-mstg-auth-5-and-mstg-auth-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.6', 'The remote endpoint implements a mechanism to protect against the submission of credentials an excessive number of times.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-best-practices-for-passwords-mstg-auth-5-and-mstg-auth-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.7', 'Sessions are invalidated at the remote endpoint after a predefined period of inactivity and access tokens expire.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-session-timeout-mstg-auth-7', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.8', 'Biometric authentication, if any, is not event-bound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md#testing-local-authentication-mstg-auth-8-and-mstg-storage-11', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.9', 'A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-two-factor-authentication-and-step-up-authentication-mstg-auth-9-and-mstg-auth-10', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.10', 'Sensitive transactions require step-up authentication.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-two-factor-authentication-and-step-up-authentication-mstg-auth-9-and-mstg-auth-10', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.11', 'The app informs the user of all sensitive activities with their account. Users are able to view a list of devices, view contextual information (IP address, location, etc.), and to block specific devices.', 18, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md#testing-login-activity-and-device-blocking-mstg-auth-11', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('4.12', 'Authorization models should be defined and enforced at the remote endpoint.', 18, False, '', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md#verifying-data-encryption-on-the-network-mstg-network-1-and-mstg-network-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md#app-transport-security-mstg-network-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md#verifying-data-encryption-on-the-network-mstg-network-1-and-mstg-network-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a trusted CA are accepted.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-endpoint-identify-verification-mstg-network-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-3-and-mstg-network-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.4', 'The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-the-network-security-configuration-settings-mstg-network-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-3-and-mstg-network-4', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.5', 'The app doesn\'t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrollments and account recovery.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md#making-sure-that-critical-operations-use-secure-communication-channels-mstg-network-5', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('5.6', 'The app only depends on up-to-date connectivity and security libraries.', 19, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-the-security-provider-mstg-network-6', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.1', 'The app only requests the minimum set of permissions necessary.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-app-permissions-mstg-platform-1,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-app-permissions-mstg-platform-1', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.2', 'All inputs from external sources and the user are validated and if necessary sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04h-Testing-Code-Quality.md#injection-flaws-mstg-arch-2-and-mstg-platform-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04h-Testing-Code-Quality.md#cross-site-scripting-flaws-mstg-platform-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-local-storage-for-input-validation-mstg-platform-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-for-injection-flaws-mstg-platform-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-for-fragment-injection-mstg-platform-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-custom-url-schemes-mstg-platform-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-custom-url-schemes-mstg-platform-3', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-for-sensitive-functionality-exposure-through-ipc-mstg-platform-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-for-sensitive-functionality-exposure-through-ipc-mstg-platform-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.5', 'JavaScript is disabled in WebViews unless explicitly required.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-ios-webviews-mstg-platform-5,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-javascript-execution-in-webviews-mstg-platform-5', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and app-id, are disabled.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-webview-protocol-handlers-mstg-platform-6,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-webview-protocol-handlers-mstg-platform-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.7', 'If native methods of the app are exposed to a WebView, verify that the WebView only renders JavaScript contained within the app package.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#determining-whether-native-methods-are-exposed-through-webviews-mstg-platform-7,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#determining-whether-java-objects-are-exposed-through-webviews-mstg-platform-7', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.8', 'Object deserialization, if any, is implemented using safe serialization APIs.', 20, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-object-persistence-mstg-platform-8,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-object-persistence-mstg-platform-8', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.9', 'The app protects itself against screen overlay attacks. (Android only)', 20, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.10', 'A WebView\'s cache, storage, and loaded resources (JavaScript, etc.) should be cleared before the WebView is destroyed.', 20, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('6.11', 'Verify that the app prevents usage of custom third-party keyboards whenever sensitive data is entered.', 20, False, '', 2)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.1', 'The app is signed and provisioned with a valid certificate, of which the private key is properly protected.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#making-sure-that-the-app-is-properly-signed-mstg-code-1,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#making-sure-that-the-app-is-properly-signed-mstg-code-1', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. non-debuggable).', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#testing-whether-the-app-is-debuggable-mstg-code-2,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#determining-whether-the-app-is-debuggable-mstg-code-2', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.3', 'Debugging symbols have been removed from native binaries.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#testing-for-debugging-symbols-mstg-code-3,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#finding-debugging-symbols-mstg-code-3', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.4', 'Debugging code and developer assistance code (e.g. test code, backdoors, hidden settings) have been removed. The app does not log verbose errors or debugging messages.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#testing-for-debugging-code-and-verbose-error-logging-mstg-code-4,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#finding-debugging-code-and-verbose-error-logging-mstg-code-4', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.5', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#checking-for-weaknesses-in-third-party-libraries-mstg-code-5,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#checking-for-weaknesses-in-third-party-libraries-mstg-code-5', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.6', 'The app catches and handles possible exceptions.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#testing-exception-handling-mstg-code-6-and-mstg-code-7,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#testing-exception-handling-mstg-code-6', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.7', 'Error handling logic in security controls denies access by default.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#testing-exception-handling-mstg-code-6-and-mstg-code-7', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.8', 'In unmanaged code, memory is allocated, freed and used securely.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#memory-corruption-bugs-mstg-code-8,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04h-Testing-Code-Quality.md#memory-corruption-bugs-mstg-code-8,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#memory-corruption-bugs-mstg-code-8', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('7.9', 'Free security features offered by the toolchain, such as byte-code minification, stack protection, PIE support and automatic reference counting, are activated.', 21, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md#make-sure-that-free-security-features-are-activated-mstg-code-9,https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md#make-sure-that-free-security-features-are-activated-mstg-code-9', 1)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.1', 'The app detects, and responds to, the presence of a rooted or jailbroken device either by alerting the user or terminating the app.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#jailbreak-detection-mstg-resilience-1', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.2', 'The app prevents debugging and/or detects, and responds to, a debugger being attached. All available debugging protocols must be covered.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#testing-anti-debugging-detection-mstg-resilience-2', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.3', 'The app detects, and responds to, tampering with executable files and critical data within its own sandbox.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#file-integrity-checks-mstg-resilience-3-and-mstg-resilience-11', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.4', 'The app detects, and responds to, the presence of widely used reverse engineering tools and frameworks on the device.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#testing-reverse-engineering-tools-detection-mstg-resilience-4', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.5', 'The app detects, and responds to, being run in an emulator.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#testing-emulator-detection-mstg-resilience-5', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.6', 'The app detects, and responds to, tampering the code and data in its own memory space.', 22, False, '', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.7', 'The app implements multiple mechanisms in each defense category (8.1 to 8.6). Note that resiliency scales with the amount, diversity of the originality of the mechanisms used.', 22, False, '', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.8', 'The detection mechanisms trigger responses of different types, including delayed and stealthy responses.', 22, False, '', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.9', 'Obfuscation is applied to programmatic defenses, which in turn impede de-obfuscation via dynamic analysis.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#testing-obfuscation-mstg-resilience-9', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.10', 'The app implements a \'device binding\' functionality using a device fingerprint derived from multiple properties unique to the device.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#device-binding-mstg-resilience-10', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.11', 'All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data.', 22, False, 'https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#file-integrity-checks-mstg-resilience-3-and-mstg-resilience-11', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.12', 'If the goal of obfuscation is to protect sensitive computations, an obfuscation scheme is used that is both appropriate for the particular task and robust against manual and automated de-obfuscation methods, considering currently published research. The effectiveness of the obfuscation scheme must be verified through manual testing. Note that hardware-based isolation features are preferred over obfuscation whenever possible.', 22, False, '', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        c = ChecklistKB('8.13', 'As a defense in depth, next to having solid hardening of the communicating parties, application level payload encryption can be applied to further impede eavesdropping.', 22, False, '', 3)
        c.kb_id = 2000
        db.session.add(c)
        db.session.commit()


        '''
        DESIGN PATTERNS
        '''

        #Project 1 ASVS LvL 1
        p = Project('Design Patterns ASVS LvL 1', '4.0', 'Application Security Verification Standard', '2021-10-05 13:37')
        db.session.add(p)
        db.session.commit()

        # Add sprints for the ASVS LvL 1 checklist category
        p = ProjectSprint('Authentication Verification Requirements','Authentication Verification Requirements')
        p.sprint_id = '1'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Session Management Verification Requirements','Session Management Verification Requirements')
        p.sprint_id = '2'        
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Access Control Verification Requirements','Access Control Verification Requirements')
        p.sprint_id = '3'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Validation, Sanitization and Encoding Verification Requirements','Validation, Sanitization and Encoding Verification Requirements')
        p.sprint_id = '4'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Stored Cryptography Verification Requirements','Stored Cryptography Verification Requirements')
        p.sprint_id = '5'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Error Handling and Logging Verification Requirements','Error Handling and Logging Verification Requirements')
        p.sprint_id = '6'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Data Protection Verification Requirements','Data Protection Verification Requirements')
        p.sprint_id = '7'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Communications Verification Requirements','Communications Verification Requirements')
        p.sprint_id = '8'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Malicious Code Verification Requirements','Malicious Code Verification Requirements')
        p.sprint_id = '9'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Business Logic Verification Requirements','Business Logic Verification Requirements')
        p.sprint_id = '10'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('File and Resources Verification Requirements','File and Resources Verification Requirements')
        p.sprint_id = '11'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('API and Web Service Verification Requirements','API and Web Service Verification Requirements')
        p.sprint_id = '12'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Configuration Verification Requirements','Configuration Verification Requirements')
        p.sprint_id = '13'
        p.group_id = 1
        p.project_id = 1
        db.session.add(p)
        db.session.commit()

        #Checklist Results
        c = ChecklistResult('0','0',False)
        c.checklist_id = '45'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '46'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '47'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '48'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '49'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '50'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '51'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '52'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '53'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '54'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '263'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '55'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '56'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '57'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '307'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '58'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '59'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '64'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '72'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '73'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '74'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '75'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '276'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '76'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '77'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '82'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '83'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '84'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '85'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '523'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '88'
        c.project_id = '1'
        c.sprint_id = '1'
        c.kb_id = '613'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '103'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '598'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '104'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '384'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '105'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '311'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '106'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '539'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '108'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '109'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '112'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '614'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '113'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '1004'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '114'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '115'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '116'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '120'
        c.project_id = '1'
        c.sprint_id = '2'
        c.kb_id = '778'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '122'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '602'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '123'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '124'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '125'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '276'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '126'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '127'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '128'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '352'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '129'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '419'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '130'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '548'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '131'
        c.project_id = '1'
        c.sprint_id = '3'
        c.kb_id = '732'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '133'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '235'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '134'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '915'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '135'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '136'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '137'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '601'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '138'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '139'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '138'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '140'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '147'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '141'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '142'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '143'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '918'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '144'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '159'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '145'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '146'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '147'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '176'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '148'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '79'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '151'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '830'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '154'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '829'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '149'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '150'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '152'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '943'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '153'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '78'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '155'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '643'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '156'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '157'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '611'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '158'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '159'
        c.project_id = '1'
        c.sprint_id = '4'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '164'
        c.project_id = '1'
        c.sprint_id = '5'
        c.kb_id = '310'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '178'
        c.project_id = '1'
        c.sprint_id = '6'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '179'
        c.project_id = '1'
        c.sprint_id = '6'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '188'
        c.project_id = '1'
        c.sprint_id = '6'
        c.kb_id = '210'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '199'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '200'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '201'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '319'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '202'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '212'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '203'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '285'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '204'
        c.project_id = '1'
        c.sprint_id = '7'
        c.kb_id = '200'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '210'
        c.project_id = '1'
        c.sprint_id = '8'
        c.kb_id = '319'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '211'
        c.project_id = '1'
        c.sprint_id = '8'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '212'
        c.project_id = '1'
        c.sprint_id = '8'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '226'
        c.project_id = '1'
        c.sprint_id = '9'
        c.kb_id = '2'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '227'
        c.project_id = '1'
        c.sprint_id = '9'
        c.kb_id = '353'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '228'
        c.project_id = '1'
        c.sprint_id = '9'
        c.kb_id = '350'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '230'
        c.project_id = '1'
        c.sprint_id = '10'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '231'
        c.project_id = '1'
        c.sprint_id = '10'
        c.kb_id = '779'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '232'
        c.project_id = '1'
        c.sprint_id = '10'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '233'
        c.project_id = '1'
        c.sprint_id = '10'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '234'
        c.project_id = '1'
        c.sprint_id = '10'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '239'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '400'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '243'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '22'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '244'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '73'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '245'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '98'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '246'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '641'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '247'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '78'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '249'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '922'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '250'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '509'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '251'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '552'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '252'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '434'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '253'
        c.project_id = '1'
        c.sprint_id = '11'
        c.kb_id = '918'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '255'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '116'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '256'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '419'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '257'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '598'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '260'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '650'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '261'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '262'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '352'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '266'
        c.project_id = '1'
        c.sprint_id = '12'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '276'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '1104'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '277'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '531'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '278'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '15'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '284'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '200'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '285'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '173'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '286'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '287'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '1021'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '288'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '289'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '523'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '290'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '291'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '292'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '749'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '293'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '294'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '282'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '209'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '283'
        c.project_id = '1'
        c.sprint_id = '13'
        c.kb_id = '497'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()

        #Project 2 ASVS LvL 2
        p = Project('Design Patterns ASVS LvL 2', '4.0', 'Application Security Verification Standard', '2021-10-05 13:37')
        db.session.add(p)
        db.session.commit()

        # Add sprints for the ASVS LvL 1 checklist category
        p = ProjectSprint('Architecture, Design and Threat Modeling Requirements','Architecture, Design and Threat Modeling Requirements')
        p.sprint_id = '14'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Authentication Verification Requirements','Authentication Verification Requirements')
        p.sprint_id = '15'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Session Management Verification Requirements','Session Management Verification Requirements')
        p.sprint_id = '16'        
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Access Control Verification Requirements','Access Control Verification Requirements')
        p.sprint_id = '17'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Validation, Sanitization and Encoding Verification Requirements','Validation, Sanitization and Encoding Verification Requirements')
        p.sprint_id = '18'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Stored Cryptography Verification Requirements','Stored Cryptography Verification Requirements')
        p.sprint_id = '19'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Error Handling and Logging Verification Requirements','Error Handling and Logging Verification Requirements')
        p.sprint_id = '20'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Data Protection Verification Requirements','Data Protection Verification Requirements')
        p.sprint_id = '21'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Communications Verification Requirements','Communications Verification Requirements')
        p.sprint_id = '22'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Malicious Code Verification Requirements','Malicious Code Verification Requirements')
        p.sprint_id = '23'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Business Logic Verification Requirements','Business Logic Verification Requirements')
        p.sprint_id = '24'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('File and Resources Verification Requirements','File and Resources Verification Requirements')
        p.sprint_id = '25'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('API and Web Service Verification Requirements','API and Web Service Verification Requirements')
        p.sprint_id = '26'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Configuration Verification Requirements','Configuration Verification Requirements')
        p.sprint_id = '27'
        p.group_id = 1
        p.project_id = 2
        db.session.add(p)
        db.session.commit()

        #Checklist results
        c = ChecklistResult('0','0',False)
        c.checklist_id = '2'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '272'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '5'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '6'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '8'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '637'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '9'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '250'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '10'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '11'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '12'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '13'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '602'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '14'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '15'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '272'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '16'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '17'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '274'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '18'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '20'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '19'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '502'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '20'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '602'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '21'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '116'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '22'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '320'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '24'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '204'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '25'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '277'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '26'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1009'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '27'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '2'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '28'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '278'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '29'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '278'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '30'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '319'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '31'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '295'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '32'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '33'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '34'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '362'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '36'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '552'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '37'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '646'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '38'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '923'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '39'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '494'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '40'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1104'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '41'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '281'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '42'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '265'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '43'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '477'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '3'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1053'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '4'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '1110'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '7'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '184'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '23'
        c.project_id = '2'
        c.sprint_id = '14'
        c.kb_id = '320'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '45'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '46'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '47'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '48'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '49'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '50'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '51'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '52'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '53'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '54'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '263'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '55'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '56'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '57'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '307'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '58'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '59'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '64'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '65'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '66'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '67'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '68'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '69'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '70'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '71'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '72'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '73'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '74'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '75'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '276'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '76'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '77'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '78'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '79'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '290'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '80'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '81'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '310'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '82'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '83'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '84'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '85'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '523'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '86'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '256'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '87'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '310'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '88'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '613'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '89'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '320'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '90'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '326'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '91'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '92'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '93'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '613'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '95'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '320'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '96'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '97'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '327'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '98'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '99'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '100'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '522'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '101'
        c.project_id = '2'
        c.sprint_id = '15'
        c.kb_id = '798'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '103'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '598'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '104'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '384'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '105'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '311'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '106'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '539'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '107'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '331'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '108'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '109'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '110'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '111'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '112'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '614'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '113'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '1004'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '114'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '115'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '116'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '117'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '290'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '118'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '798'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '119'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '345'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '120'
        c.project_id = '2'
        c.sprint_id = '16'
        c.kb_id = '778'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '122'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '602'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '123'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '124'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '125'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '276'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '126'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '127'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '128'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '352'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '129'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '419'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '130'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '548'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '131'
        c.project_id = '2'
        c.sprint_id = '17'
        c.kb_id = '732'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '133'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '235'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '134'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '915'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '135'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '136'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '137'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '601'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '138'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '139'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '138'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '140'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '147'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '141'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '142'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '143'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '918'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '144'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '159'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '145'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '146'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '147'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '176'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '148'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '79'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '151'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '830'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '154'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '829'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '149'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '150'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '152'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '943'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '153'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '78'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '155'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '643'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '156'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '157'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '611'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '158'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '159'
        c.project_id = '2'
        c.sprint_id = '18'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '161'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '162'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '163'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '164'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '310'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '165'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '327'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '166'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '167'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '168'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '169'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '172'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '338'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '173'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '338'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '175'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '798'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '176'
        c.project_id = '2'
        c.sprint_id = '19'
        c.kb_id = '320'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '178'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '179'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '180'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '181'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '182'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '183'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '285'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '184'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '117'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '185'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '117'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '186'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '200'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '187'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '2'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '188'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '210'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '189'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '544'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '190'
        c.project_id = '2'
        c.sprint_id = '20'
        c.kb_id = '460'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '192'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '532'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '194'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '233'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '195'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '525'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '199'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '200'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '201'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '319'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '202'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '212'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '203'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '285'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '204'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '200'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '205'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '532'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '206'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '226'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '207'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '525'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '208'
        c.project_id = '2'
        c.sprint_id = '21'
        c.kb_id = '285'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '210'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '319'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '211'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '212'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '213'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '295'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '214'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '319'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '215'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '297'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '216'
        c.project_id = '2'
        c.sprint_id = '22'
        c.kb_id = '299'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '220'
        c.project_id = '2'
        c.sprint_id = '23'
        c.kb_id = '359'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '221'
        c.project_id = '2'
        c.sprint_id = '23'
        c.kb_id = '272'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '226'
        c.project_id = '2'
        c.sprint_id = '23'
        c.kb_id = '2'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '227'
        c.project_id = '2'
        c.sprint_id = '23'
        c.kb_id = '353'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '228'
        c.project_id = '2'
        c.sprint_id = '23'
        c.kb_id = '350'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '230'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '231'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '779'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '232'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '233'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '237'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '390'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '234'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '235'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '367'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '236'
        c.project_id = '2'
        c.sprint_id = '24'
        c.kb_id = '754'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '239'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '400'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '240'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '400'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '241'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '409'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '242'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '434'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '243'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '22'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '244'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '73'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '245'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '98'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '246'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '641'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '247'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '78'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '248'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '829'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '249'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '922'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '250'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '509'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '251'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '552'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '252'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '434'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '253'
        c.project_id = '2'
        c.sprint_id = '25'
        c.kb_id = '918'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '255'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '116'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '256'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '419'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '257'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '598'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '258'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '285'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '259'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '434'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '260'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '650'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '261'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '262'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '352'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '263'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '779'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '264'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '436'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '265'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '598'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '266'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '267'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '345'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '268'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '770'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '269'
        c.project_id = '2'
        c.sprint_id = '26'
        c.kb_id = '285'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '271'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '272'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '120'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '273'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '274'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '276'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '1104'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '277'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '531'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '278'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '15'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '279'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '828'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '280'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '281'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '265'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '284'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '200'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '285'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '173'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '286'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '287'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '1021'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '288'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '289'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '523'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '290'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '291'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '292'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '749'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '293'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '294'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '295'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '306'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '282'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '209'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '283'
        c.project_id = '2'
        c.sprint_id = '27'
        c.kb_id = '497'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()

        #Project 3 ASVS LvL 3
        p = Project('Design Patterns ASVS LvL 3', '4.0', 'Application Security Verification Standard', '2021-10-05 13:37')
        db.session.add(p)
        db.session.commit()

        # Add sprints for the ASVS LvL 3 checklist category
        p = ProjectSprint('Architecture, Design and Threat Modeling Requirements','Architecture, Design and Threat Modeling Requirements')
        p.sprint_id = '28'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Authentication Verification Requirements','Authentication Verification Requirements')
        p.sprint_id = '29'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Session Management Verification Requirements','Session Management Verification Requirements')
        p.sprint_id = '30'        
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Access Control Verification Requirements','Access Control Verification Requirements')
        p.sprint_id = '31'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Validation, Sanitization and Encoding Verification Requirements','Validation, Sanitization and Encoding Verification Requirements')
        p.sprint_id = '32'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Stored Cryptography Verification Requirements','Stored Cryptography Verification Requirements')
        p.sprint_id = '33'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Error Handling and Logging Verification Requirements','Error Handling and Logging Verification Requirements')
        p.sprint_id = '34'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Data Protection Verification Requirements','Data Protection Verification Requirements')
        p.sprint_id = '35'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Communications Verification Requirements','Communications Verification Requirements')
        p.sprint_id = '36'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Malicious Code Verification Requirements','Malicious Code Verification Requirements')
        p.sprint_id = '37'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Business Logic Verification Requirements','Business Logic Verification Requirements')
        p.sprint_id = '38'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('File and Resources Verification Requirements','File and Resources Verification Requirements')
        p.sprint_id = '39'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('API and Web Service Verification Requirements','API and Web Service Verification Requirements')
        p.sprint_id = '40'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        p = ProjectSprint('Configuration Verification Requirements','Configuration Verification Requirements')
        p.sprint_id = '41'
        p.group_id = 1
        p.project_id = 3
        db.session.add(p)
        db.session.commit()

        #Checklist results
        c = ChecklistResult('0','0',False)
        c.checklist_id = '2'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '272'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '5'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '6'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '8'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '637'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '9'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '250'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '10'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '11'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '12'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '306'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '13'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '602'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '14'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '15'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '272'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '16'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '17'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '274'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '18'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '20'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '19'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '502'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '20'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '602'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '21'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '116'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '22'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '320'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '24'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '204'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '25'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '277'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '26'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1009'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '27'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '2'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '28'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '278'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '29'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '278'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '30'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '319'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '31'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '295'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '32'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '284'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '33'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1059'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '34'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '362'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '35'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '362'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '36'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '552'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '37'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '646'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '38'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '923'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '39'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '494'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '40'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1104'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '41'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '281'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '42'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '265'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '43'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '477'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '3'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1053'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '4'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '1110'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '7'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '184'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '23'
        c.project_id = '3'
        c.sprint_id = '28'
        c.kb_id = '320'
        c.checklist_type_id = '1'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '45'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '46'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '47'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '48'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '49'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '50'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '51'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '52'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '53'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '54'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '263'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '55'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '56'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '521'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '57'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '307'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '58'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '59'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '620'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '60'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '61'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '319'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '62'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '63'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '64'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '65'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '66'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '67'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '68'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '69'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '70'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '71'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '916'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '72'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '73'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '74'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '75'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '276'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '76'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '304'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '77'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '640'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '78'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '79'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '290'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '80'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '81'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '310'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '82'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '83'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '84'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '85'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '523'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '86'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '256'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '87'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '310'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '88'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '613'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '89'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '320'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '90'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '326'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '91'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '92'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '93'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '613'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '94'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '308'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '95'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '320'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '96'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '330'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '97'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '327'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '98'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '99'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '287'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '100'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '522'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '101'
        c.project_id = '3'
        c.sprint_id = '29'
        c.kb_id = '798'
        c.checklist_type_id = '2'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '103'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '598'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '104'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '384'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '105'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '311'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '106'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '539'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '107'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '331'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '108'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '109'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '110'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '111'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '613'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '112'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '614'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '113'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '1004'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '114'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '115'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '116'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '2'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '117'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '290'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '118'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '798'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '119'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '345'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '120'
        c.project_id = '3'
        c.sprint_id = '30'
        c.kb_id = '778'
        c.checklist_type_id = '3'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '122'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '602'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '123'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '124'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '125'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '276'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '126'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '285'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '127'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '639'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '128'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '352'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '129'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '419'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '130'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '548'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '131'
        c.project_id = '3'
        c.sprint_id = '31'
        c.kb_id = '732'
        c.checklist_type_id = '4'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '133'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '235'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '134'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '915'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '135'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '136'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '20'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '137'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '601'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '138'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '139'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '138'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '140'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '147'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '141'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '142'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '143'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '918'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '144'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '159'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '145'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '94'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '146'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '116'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '147'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '176'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '148'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '79'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '151'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '830'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '154'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '829'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '149'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '150'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '89'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '152'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '943'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '153'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '78'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '155'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '643'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '156'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '157'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '611'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '158'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '502'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '159'
        c.project_id = '3'
        c.sprint_id = '32'
        c.kb_id = '95'
        c.checklist_type_id = '5'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '161'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '162'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '163'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '311'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '164'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '310'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '165'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '327'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '166'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '167'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '168'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '169'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '170'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '171'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '326'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '172'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '338'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '173'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '338'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '174'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '338'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '175'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '798'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '176'
        c.project_id = '3'
        c.sprint_id = '33'
        c.kb_id = '320'
        c.checklist_type_id = '6'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '178'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '179'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '532'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '180'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '181'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '182'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '778'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '183'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '285'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '184'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '117'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '185'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '117'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '186'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '200'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '187'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '2'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '188'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '210'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '189'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '544'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '190'
        c.project_id = '3'
        c.sprint_id = '34'
        c.kb_id = '460'
        c.checklist_type_id = '7'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '192'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '532'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '194'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '233'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '195'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '525'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '196'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '770'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '197'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '300'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '199'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '200'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '922'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '201'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '319'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '202'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '212'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '203'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '285'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '204'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '200'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '205'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '532'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '206'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '226'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '207'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '525'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '208'
        c.project_id = '3'
        c.sprint_id = '35'
        c.kb_id = '285'
        c.checklist_type_id = '8'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '210'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '319'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '211'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '212'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '326'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '213'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '295'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '214'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '319'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '215'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '297'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '216'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '299'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '217'
        c.project_id = '3'
        c.sprint_id = '36'
        c.kb_id = '544'
        c.checklist_type_id = '9'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '219'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '749'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '220'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '359'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '221'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '272'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '222'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '507'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '223'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '511'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '224'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '511'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '225'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '507'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '226'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '2'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '227'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '353'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '228'
        c.project_id = '3'
        c.sprint_id = '37'
        c.kb_id = '350'
        c.checklist_type_id = '10'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '230'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '231'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '779'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '232'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '233'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '770'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '237'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '390'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '234'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '841'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '235'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '367'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '236'
        c.project_id = '3'
        c.sprint_id = '38'
        c.kb_id = '754'
        c.checklist_type_id = '11'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '239'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '400'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '240'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '400'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '241'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '409'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '242'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '434'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '243'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '22'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '244'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '73'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '245'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '98'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '246'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '641'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '247'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '78'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '248'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '829'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '249'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '922'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '250'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '509'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '251'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '552'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '252'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '434'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '253'
        c.project_id = '3'
        c.sprint_id = '39'
        c.kb_id = '918'
        c.checklist_type_id = '12'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '255'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '116'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '256'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '419'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '257'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '598'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '258'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '285'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '259'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '434'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '260'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '650'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '261'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '262'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '352'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '263'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '779'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '264'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '436'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '265'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '598'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '266'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '20'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '267'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '345'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '268'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '770'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '269'
        c.project_id = '3'
        c.sprint_id = '40'
        c.kb_id = '285'
        c.checklist_type_id = '13'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '271'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '272'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '120'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '273'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '274'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '275'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '276'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '1104'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '277'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '531'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '278'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '15'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '279'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '828'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '280'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '2'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '281'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '265'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '284'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '200'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '285'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '173'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '286'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '287'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '1021'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '288'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '289'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '523'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '290'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '116'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '291'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '292'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '749'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '293'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '294'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '346'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '295'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '306'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '282'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '209'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()


        c = ChecklistResult('0','0',False)
        c.checklist_id = '283'
        c.project_id = '3'
        c.sprint_id = '41'
        c.kb_id = '497'
        c.checklist_type_id = '14'
        db.session.add(c)
        db.session.commit()






        '''
        ASVS 1 to testing controls
        '''

        kb_code_cor = ChecklistKBCodeItem(45,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(45,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(45,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(46,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(46,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(46,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(47,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(47,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(47,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(48,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(48,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(48,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(49,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(49,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(49,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(50,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(50,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(51,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(52,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(52,289)   
        db.session.add(kb_code_cor)
        db.session.commit()
        
        kb_code_cor = ChecklistKBCodeItem(53,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(53,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(53,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(55,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(55,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(56,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(56,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(57,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(59,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(59,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(64,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(64,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(64,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(72,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(72,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(72,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(74,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(74,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(74,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(76,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(76,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(76,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(77,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(77,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(77,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(82,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(82,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(83,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(83,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(83,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(83,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(83,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(84,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(84,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(84,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(84,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(84,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(88,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(88,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(88,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(103,291)   
        db.session.add(kb_code_cor)
        db.session.commit()
        
        kb_code_cor = ChecklistKBCodeItem(104,286)   
        db.session.add(kb_code_cor)
        db.session.commit()
        
        kb_code_cor = ChecklistKBCodeItem(104,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(104,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(106,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(106,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(106,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(106,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(107,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(107,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(107,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(108,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(108,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(109,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(109,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(109,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(112,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(112,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(112,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(112,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(113,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(113,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(113,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(113,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(114,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(114,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(114,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(114,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(115,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(115,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(115,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(115,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(116,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(116,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(116,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(116,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(124,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(124,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(124,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(124,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(124,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(125,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(125,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(125,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(126,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(128,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(128,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(128,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(130,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(129,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(133,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(134,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(134,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(134,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(135,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(135,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(135,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(136,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(136,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(136,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(137,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(137,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(137,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(138,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(139,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(139,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(139,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(141,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(141,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(141,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(143,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(143,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(143,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(143,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(144,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(145,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(146,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(146,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(146,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(146,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(147,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(147,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(147,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(147,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(148,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(148,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(148,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(148,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(149,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(149,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(149,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(149,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(150,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(150,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(150,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(150,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(151,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(151,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(151,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(151,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(152,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(152,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(152,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(152,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(153,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(153,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(153,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(153,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(154,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(154,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(154,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(154,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(164,294)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(178,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(178,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(178,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(179,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(179,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(179,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(188,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(188,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(188,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(198,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(198,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(198,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(198,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(199,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(201,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(201,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(201,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(202,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(202,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(202,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(203,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(203,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(203,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(203,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(203,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(210,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(211,294)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(211,294)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(227,291)   
        db.session.add(kb_code_cor)
        db.session.commit()       

        kb_code_cor = ChecklistKBCodeItem(230,292)   
        db.session.add(kb_code_cor)
        db.session.commit()  

        kb_code_cor = ChecklistKBCodeItem(230,289)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(231,292)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(231,289)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(232,292)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(232,289)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(233,292)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(233,289)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(233,291)   
        db.session.add(kb_code_cor)
        db.session.commit()   

        kb_code_cor = ChecklistKBCodeItem(239,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(239,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(239,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(243,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(243,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(243,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(243,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(244,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(244,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(244,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(244,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(245,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(245,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(245,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(245,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(246,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(246,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(246,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(246,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(247,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(247,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(247,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(247,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(249,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(249,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(249,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(249,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(250,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(250,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(250,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(251,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(251,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(251,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(251,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(252,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(252,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(253,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(253,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(253,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(255,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(255,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(255,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(255,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(257,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(260,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(260,289)   
        db.session.add(kb_code_cor)
        db.session.commit()
        
        kb_code_cor = ChecklistKBCodeItem(261,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(261,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(262,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(262,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(262,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(262,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(266,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(266,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(266,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(266,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(276,290)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(276,293)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(282,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(282,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(283,292)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(283,289)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(284,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(285,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(286,291)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(287,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(287,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(287,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(287,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(288,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(288,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(288,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(288,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(289,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(289,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(289,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(289,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(290,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(290,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(290,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(290,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(291,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(291,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(291,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(291,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(292,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(292,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(292,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(292,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(293,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(293,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(293,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(293,288)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(294,286)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(294,295)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(294,287)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(294,288)   
        db.session.add(kb_code_cor)
        db.session.commit()


        '''
        ASVS 1 to FLASK examples
        '''

        
        kb_code_cor = ChecklistKBCodeItem(45,130)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(46,130)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(47,130)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(51,130)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(53,130)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(99,143)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(64,142)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(67,143)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(68,143)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(70,143)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(71,143)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(87,142)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(108,139)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(108,163)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(112,148)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(116,133)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(128,138)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(131,131)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(135,140)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(137,140)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(137,150)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(142,129)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,151)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(155,168)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(149,149)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(153,147)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(154,144)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(157,156)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(198,152)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(230,146)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(239,169)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(243,144)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(244,169)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(246,135)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(249,169)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(262,138)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(283,158)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(285,136)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(291,157)   
        db.session.add(kb_code_cor)
        db.session.commit()

        kb_code_cor = ChecklistKBCodeItem(295,154)   
        db.session.add(kb_code_cor)
        db.session.commit()

        '''
        Code review labs solutions
        '''

        lab_code_sol = LabItemCodeOptions("Denial Of Service")   
        db.session.add(lab_code_sol)
        db.session.commit()

        lab_code_sol = LabItemCodeOptions("Exec Code")   
        db.session.add(lab_code_sol)
        db.session.commit()     

        lab_code_sol = LabItemCodeOptions("Overflow")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Execute Code")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Obtain Information")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Memory corruption")   
        db.session.add(lab_code_sol)
        db.session.commit()   
        
        lab_code_sol = LabItemCodeOptions("Gain privileges")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Obtain Information")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Bypass a restriction")   
        db.session.add(lab_code_sol)
        db.session.commit()   

        lab_code_sol = LabItemCodeOptions("Directory traversal")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Filename injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Http response splitting")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Cross Site Request Forgery")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Sql Injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("File inclusion")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Cross Site Scripting")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Server side template injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Client side template injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("XML injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Xpath injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Ldap injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Race condition")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("CRLF injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Header injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Regular expression injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Expression language injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCodeOptions("Deserialization injection")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        '''
        Code review labs
        '''

        lab_code_sol = LabItemCode("<?php system($input); ?>", 2, "php")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCode("<?php $query  = 'SELECT id, name FROM products ORDER BY name LIMIT 20 OFFSET $offset;'; ?>", 14, "php")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCode("System.Diagnostics.Process.Start('CMD.exe',strCommand);", 2, "asp")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        lab_code_sol = LabItemCode("os.system($input)", 2, "python")   
        db.session.add(lab_code_sol)
        db.session.commit()  

        print('Initialized the initial data.')
        return True
    except:
        db.session.rollback()
        raise