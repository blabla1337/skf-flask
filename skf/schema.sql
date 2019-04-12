--
-- Table structure for table `users`
--
drop table if exists `users`;
CREATE TABLE `users` (
`userID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilegeID` int(11) NOT NULL,
`userName` varchar(255) NOT NULL UNIQUE,
`email` varchar(255) NOT NULL UNIQUE,
`password` varchar(255) NOT NULL,
`accessToken` int(11) NOT NULL UNIQUE,
`activated` varchar(255),
`access` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "False", "False", "example@owasp.org");


--
-- Table structure for table `groups`
--
drop table if exists `groups`;
CREATE TABLE `groups` (
`groupID` INTEGER PRIMARY KEY AUTOINCREMENT,
`ownerID` int(11) NOT NULL,
`groupName` varchar(250) NOT NULL,
`timestamp` timestamp
);

INSERT OR REPLACE INTO `groups` (`groupID`, `ownerID`, `groupName`) VALUES (1, 1, "privateGroup");

--
-- Table structure for table `groupmembers`
--
drop table if exists `groupmembers`;
CREATE TABLE `groupmembers` (
`memberID` INTEGER PRIMARY KEY AUTOINCREMENT,
`userID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`ownerID` int(11) NOT NULL,
`timestamp` timestamp
);

INSERT OR REPLACE INTO `groupMembers` (`memberID`, `userID`, `groupID`, `ownerID`) VALUES (1, 1, 1, 1);


--
-- Table structure for table `privileges`
--
drop table if exists `privileges`;
CREATE TABLE `privileges` (
`privilegeID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilege` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (1, "edit:read:manage:delete");
INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (2, "edit:read:delete");
INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (3, "edit:read");
INSERT OR REPLACE INTO `privileges` (`privilegeID`, `privilege`) VALUES (4, "read");

--
-- Table structure for table `kb_items`
--

drop table if exists `kb_items`;
CREATE TABLE `kb_items` (
`kbID` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL
);


--
-- Table structure for table `code_items`
--
drop table if exists `code_items`;
CREATE TABLE `code_items` (
`codeID` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL,
`code_lang` varchar(250) NOT NULL
);


--
-- Table structure for table `projects`
--
drop table if exists `projects`;
CREATE TABLE `projects` (
`projectID` INTEGER PRIMARY KEY AUTOINCREMENT,
`userID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`projectName` varchar(250) NOT NULL,
`projectVersion` varchar(250) NOT NULL,
`projectDesc` text NOT NULL,
`ownerID` int(11) NOT NULL,
`timestamp` timestamp NOT NULL,
`checklist_type` int(11) NOT NULL
);


--
-- Table structure for table `project_sprints`
--
drop table if exists `project_sprints`;
CREATE TABLE `project_sprints` (
`sprintID` INTEGER PRIMARY KEY AUTOINCREMENT,
`projectID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`sprintName` varchar(250) NOT NULL,
`sprintDesc` varchar(250) NOT NULL
);


--
-- Table structure for table `logs`
--
drop table if exists `logs`;
CREATE TABLE `logs` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`date` varchar(255) NOT NULL,
`time` varchar(255) NOT NULL,
`threat` varchar(255) NOT NULL,
`ip` varchar(255) NOT NULL,
`userID` varchar(255) NOT NULL,
`status` varchar(255) NOT NULL,
`message` varchar(255) NOT NULL
);


--
-- Table structure for table `checklist_types`
--
drop table if exists `checklist_types`;
CREATE TABLE `checklist_types` (
`checklist_type` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_description` varchar(255) NOT NULL,
`checklist_name` varchar(255) NOT NULL
);


--
-- Default checklist types
--
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS SKF", "A checklist derrived from ASVS");


--
-- Table structure for table `questions_sprint`
--
drop table if exists `questions_sprint`;
CREATE TABLE `questions_sprint` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);

--
--ASVS SKF
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement changes that affect and change CI/CD?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement changes that affect authentication/authorization?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement changes that affect session management?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement changes that affect access control systems?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint make use/implement an ORM framework? (object relational model)");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that handle user supplied input? (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc)");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that forward or redirect your users trough the application?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize wysiwyg editors?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that allow users to send emails?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize templating engines or single page apps such as (Angular, React)");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that allow for SVG scriptable content to be uploaded/posted?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that reflect user supplied input on the side of the client?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize raw SQL queries?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize LDAP?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize OS commands?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that get/grabs files from the file system?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that parse or digests XML?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/change functions with native code (C, C++)");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that deserializes objects (JSON, XML and YAML)");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that process sensitive data?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint imlement functions that require secure random values");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that impact logging?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes TLS configuration?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that allow users to upload/download files?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that utilize GraphQL");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement functions that store sensitive information?");


--
-- Table structure for table `questions_pre`
--
drop table if exists `questions_pre`;
CREATE TABLE `questions_pre` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);

--
--ASVS SKF
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Is there a mature SDLC process in place and is this process validated using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are authentication Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Session Management Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are access Control Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Input and Output Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Cryptographic Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Errors, Logging and Auditing Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Data Protection and Privacy Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are secure Communications Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Business Logic Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Secure Files Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are API Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Configuration Architectural Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are General Authenticator Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Authenticatior lifecycle Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are crediential Recovery Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Memorized Secret Authenticator Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Credential Storage Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Look-up Secret Verifier Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Single Factor out of band Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Single/Multi Factor OTP requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Cryptographic Software and Devices defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Service Authentication Requirements defined and validated against ASVS");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Does the application use Cookie-based Session Management, Session Logout and Timeout?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Does the application use Token-based Session Management?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Is authentication in the form of Re-authentication from a Federation or Assertion");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are you writing relying party(RP) or credential service provider(CSP) code?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements defined that include guidelines for input validation?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements defined that include guidelines for output encoding and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements defined that include guidelines for unmanaged code (system languages, C, C++) and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place for defining critical data that should be stored encrypted and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Is there a hardened secret management solution in place for storing application/infrastructure secrets and is this secret manager validated against ASVS ?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place with regard to Logging, Log Processing, Log Protection, and are these validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements for Error Handling in place, and are these validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place with regard to high level data protection, and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place for hardening TLS connections, and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements for code integrity controls in place, and are there requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place for a four eyes principle proces to validate the application does not contain malicous code, and are these controls validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there controls in place to validate the integrity of a  Deployed Application, and are these controls validated against ASVS?(sub domain takeover)");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place to validate Business Logic, and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are there requirements in place for API and web-service development, and are these requirements validated against ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Validate that a source control system is in use");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`,  `question`) VALUES (1, "Are Algorithms and key lengths still safe and sufficient to protect data and validated against ASVS?");


--
-- Table structure for table `question_sprint_results`
--
drop table if exists `question_sprint_results`;
CREATE TABLE `question_sprint_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`projectID` int(11) NOT NULL,
`sprintID` int(11) NOT NULL,
`question_sprint_ID` int(11) NOT NULL,
`result` boolean
);
 

--
-- Table structure for table `question_pre_results`
--
drop table if exists `question_pre_results`;
CREATE TABLE `question_pre_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`projectID` int(11) NOT NULL,
`question_pre_ID` int(11) NOT NULL,
`result` boolean
);

--
-- Table structure for table `checklists_results`
--
drop table if exists `checklists_results`;
CREATE TABLE `checklists_results` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255) NOT NULL,
`projectID` int(11) NOT NULL,
`sprintID` int(11) NOT NULL,
`status` int(11) NOT NULL,
`preItem` int(11) NOT NULL,
`kbID` int(11)
);

--
-- Table structure for table `comments`
--
drop table if exists `comments`;
CREATE TABLE `comments` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`sprintID` int(11) NOT NULL,
`checklistID` varchar(255) NOT NULL,
`userID` int(11) NOT NULL, 
`status` int(11) NOT NULL, 	
`comment` varchar(255),
`date` varchar(255) NOT NULL
);

--
-- Table structure for table `chatbot_log`
--
drop table if exists `chatbot_log`;
CREATE TABLE `chatbot_log` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`question` varchar(255)
); 

--
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;

CREATE TABLE IF NOT EXISTS checklists_kb (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `checklistID` varchar(255),
    `content` varchar(255),
    `cwe` int(11),
    `question_pre_ID` int(11),
    `question_sprint_ID` int(11),
    `include_first` varchar(5),
    `include_always` varchar(5),
    `kbID` int(11)
);

INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES ('1','Architecture, Design and Threat Modeling Requirements',0,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.1.1','Verify the use of a secure software development lifecycle that addresses security in all stages of development.',NULL,1,1,'False','False',272);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('1.1.2','Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.',1053,NULL,NULL,'False','True',164);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.1.3','Verify that all user stories and features contain functional security constraints, such as "As a user, I should be able to view and edit my profile. I should not be able to view or edit anyone else''s profile"',1110,1,1,'False','True',273);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.1.6','Verify implementation of centralized, simple (economy of design); vetted, secure, and reusable security controls to avoid duplicate, missing, ineffective, or insecure controls.',637,1,1,'False','True',184);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('1.2.1','Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers.',250,3,NULL,'False','False',126);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.2.3','Verify that the application uses a single vetted authentication mechanism that is known to be secure, can be extended to include strong authentication, and has sufficient logging and monitoring to detect account abuse or breaches.',306,3,NULL,'False','False',259);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.2.4','Verify that all authentication pathways and identity management APIs implement consistent authentication security control strength, such that there are no weaker alternatives per the risk of the application.',306,3,NULL,'False','False',85);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.4.1','Verify that trusted enforcement points such as at access control gateways, servers, and serverless functions enforce access controls. Never enforce access controls on the client.',602,4,NULL,'False','False',240);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.4.3','Verify enforcement of the principle of least privilege in functions, data files, URLs, controllers, services, and other resources. This implies protection against spoofing and elevation of privilege.',272,4,NULL,'v','False',126);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('1.4.5','Verify that attribute or feature-based access control is used whereby the code checks the user''s authorization for a feature/data item rather than just their role.',275,4,NULL,'False','False',274);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('1.6.1','Verify that there is an explicit policy for management of cryptographic keys and that a cryptographic key lifecycle follows a key management standard such as NIST SP 800-57.',320,6,NULL,'True','False',275);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.6.2','Verify that consumers of cryptographic services protect key material and other secrets by using key vaults or API based alternatives.',320,6,NULL,'False','True',276);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.6.3','Verify that all keys and passwords are replaceable and are part of a well-defined process to re-encrypt sensitive data.',320,6,NULL,'False','False',204);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.6.4','Verify that symmetric keys, passwords, or API secrets generated by or shared with clients are used only in protecting low risk secrets, such as encrypting local storage, or temporary ephemeral uses such as parameter obfuscation. Sharing secrets with clients is clear-text equivalent and architecturally should be treated as such.',320,6,NULL,'False','False',277);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.8.1','Verify that all sensitive data is identified and classified into protection levels.',NULL,8,NULL,'False','False',278);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.8.2','Verify that all protection levels have an associated set of protection requirements, such as encryption requirements, integrity requirements, retention, privacy and other confidentiality requirements, and that these are applied in the architecture.',NULL,8,NULL,'False','False',278);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.10','Malicious Software Architectural Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.10.1','Verify that a source code control system is in use, with procedures to ensure that check-ins are accompanied by issues or change tickets. The source code control system should have access control and identifiable users to allow traceability of any changes.',284,50,NULL,'False',NULL,279);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.12.1','Verify that user-uploaded files are stored outside of the web root.',552,11,NULL,'False','False',227);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('1.14.3','Verify that the build pipeline warns of out-of-date or insecure components and takes appropriate actions.',1104,13,NULL,'True','False',280);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('1.14.4','Verify that the build pipeline contains a build step to automatically build and verify the secure deployment of the application, particularly if the application infrastructure is software defined, such as cloud environment build scripts.',NULL,13,NULL,'True','False',281);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2','Authentication Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.1.1','Verify that user set passwords are at least 12 characters in length. (C6)',521,17,NULL,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.1.2','Verify that passwords 64 characters or longer are permitted. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',521,17,2,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.1.3','Verify that passwords can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',521,17,2,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.1.4','Verify that Unicode characters are permitted in passwords. A single Unicode code point is considered a character, so 12 emoji or 64 kanji characters should be valid and permitted.',521,17,2,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.1.5','Verify users can change their password.',620,17,2,'False','False',1343);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.1.6','Verify that password change functionality requires the user''s current and new password.',620,17,2,'False','False',32);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES ('2.1.7','Verify that passwords submitted during account registration, login, and password change are checked against a set of breached passwords either locally (such as the top 1,000 or 10,000 most common passwords which match the system''s password policy) or using an external API. If using an API a zero knowledge proof or other mechanism should be used to ensure that the plain text password is not sent or used in verifying the breach status of the password. If the password is breached, the application must require the user to set a new non-breached password. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',521,17,2,'False','False',1345);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.1.8','Verify that a password strength meter is provided to help users set a stronger password.',521,17,2,'False','False',1344);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.1.9','Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',521,17,2,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.1.10','Verify that there are no periodic credential rotation or password history requirements.',263,17,2,'False','False',295);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.1.11','Verify that "paste" functionality, browser password helpers, and external password managers are permitted.',521,17,2,'False','False',59);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.2.1','Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. Such controls include blocking the most common breached passwords, soft lockouts, rate limiting, CAPTCHA, ever increasing delays between attempts, IP address restrictions, or risk-based restrictions such as location, first login on a device, recent attempts to unlock the account, or similar. Verify that no more than 100 failed attempts per hour is possible on a single account.',307,15,2,'False','False',29);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.2.2','Verify that the use of weak authenticators (such as SMS and email) is limited to secondary verification and transaction approval and not as a replacement for more secure authentication methods. Verify that stronger methods are offered before weak methods, users are aware of the risks, or that proper measures are in place to limit the risks of account compromise.',304,14,2,'False','False',115);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.2.3','Verify that secure notifications are sent to users after updates to authentication details, such as credential resets, email or address changes, logging in from unknown or risky locations. The use of push notifications - rather than SMS or email - is preferred, but in the absence of push notifications, SMS or email is acceptable as long as no sensitive information is disclosed in the notification.',620,14,2,'False','False',296);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.2.4','Verify impersonation resistance against phishing, such as the use of multi-factor authentication, cryptographic devices with intent (such as connected keys with a push to authenticate); or at higher AAL levels, client-side certificates.',308,14,2,'False','False',2231);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.2.6','Verify replay resistance through the mandated use of OTP devices, cryptographic authenticators, or lookup codes.',308,14,2,'False','False',290);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.3.1','Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers, and expire after a short period of time. These initial secrets must not be permitted to become the long term password.',330,15,2,'False','False',214);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.4.1','Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one-way key derivation or password hashing function. Key derivation and password hashing functions take a password, a salt, and a cost factor as inputs when generating a password hash. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',916,18,2,'False','False',51);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.5.1','Verify that a system generated initial activation or recovery secret is not sent in clear text to the user. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',640,16,2,'False','False',243);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.5.2','Verify password hints or knowledge-based authentication (so-called "secret questions") are not present.',640,16,2,'False','False',87);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.5.3','Verify password credential recovery does not reveal the current password in any way. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',640,16,2,'False','False',243);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.5.5','Verify that if an authentication factor is changed or replaced, that the user is notified of this event.',304,16,2,'False','False',296);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.5.6','Verify forgotten password, and other recovery paths use a secure recovery mechanism, such as TOTP or other soft token, mobile push, or another offline recovery mechanism. ',640,16,2,'False','False',115);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.6.1','Verify that lookup secrets can be used only once.',308,19,2,'False','False',290);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.6.2','Verify that lookup secrets have sufficient randomness (112 bits of entropy); or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash.',330,19,2,'False','False',304);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.8.1','Verify that time-based OTPs have a defined lifetime before expiring.',613,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.8.2','Verify that symmetric keys used to verify submitted OTPs are highly protected, such as by using a hardware security module or secure operating system based key storage.',320,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.8.3','Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.',326,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.8.4','Verify that time-based OTP can be used only once within the validity period.',287,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.8.5','Verify that if a time-based multi factor OTP token is re-used during the validity period, it is logged and rejected with secure notifications being sent to the holder of the device.',287,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.8.6','Verify physical single factor OTP generator can be revoked in case of theft or other loss. Ensure that revocation is immediately effective across logged in sessions, regardless of location.',613,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('2.8.7','Verify that biometric authenticators are limited to use only as secondary factors in conjunction with either something you have and something you know.',308,21,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.9.1','Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a TPM or HSM, or an OS service that can use this secure storage.',320,23,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.9.2','Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device.',330,23,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('2.9.3','Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.',327,23,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('2.10.1','Verify that integration secrets do not rely on unchanging passwords, such as API keys or shared privileged accounts.',287,24,2,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3','Session Management Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.1.1','Verify the application never reveals session tokens in URL parameters or error messages.',598,3,3,'False','False',91);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('3.2.1','Verify the application generates a new session token on user authentication. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',384,3,3,'False','False',58);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.3.1','Verify that logout and expiration invalidate the session token, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',613,3,3,'False','False',57);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.3.3','Verify that the application terminates all other active sessions after a successful password change, and that this is effective across the application, federated login (if present); and any relying parties.',613,3,3,'False','False',254);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.3.4','Verify that users are able to view and log out of any or all currently active sessions and devices.',613,3,3,'False','False',188);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.4.1','Verify that cookie-based session tokens have the ''Secure'' attribute set. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',614,27,3,'False','False',38);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('3.4.2','Verify that cookie-based session tokens have the ''HttpOnly'' attribute set. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',1004,27,3,'False','False',39);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('3.4.3','Verify that cookie-based session tokens utilize the ''SameSite'' attribute to limit exposure to cross-site request forgery attacks. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',16,27,3,'False','False',291);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('3.4.4','Verify that cookie-based session tokens use "__Host-" prefix (see references) to provide session cookie confidentiality.',16,27,3,'False','False',292);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('3.4.5','Verify that if the application is published under a domain name with other applications that set or use session cookies that might override or disclose the session cookies, set the path attribute in cookie-based session tokens using the most precise path possible. ([C6](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',16,27,3,'False','False',158);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('3.5.3','Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks.',345,28,3,'False','False',297);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('3.7.1','Verify the application ensures a valid login session or requires re-authentication or secondary verification before allowing any sensitive transactions or account modifications.',778,14,3,'False','False',233);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('4','Access Control Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('4.1.5','Verify that access controls fail securely including when an exception occurs. ([C10](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',285,4,4,'False','False',114);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('4.2.1','Verify that sensitive data and APIs are protected against direct object attacks targeting creation, reading, updating and deletion of records, such as creating or updating someone else''s record, viewing everyone''s records, or deleting all records.',639,4,4,'False','False',268);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('4.2.2','Verify that the application or framework enforces a strong anti-CSRF mechanism to protect authenticated functionality, and effective anti-automation or anti-CSRF protects unauthenticated functionality.',352,4,4,'False','False',5);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('4.3.1','Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use.',419,4,4,'False','False',231);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('4.3.2','Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.',548,4,4,'False','False',61);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('4.3.3','Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud.',732,4,4,'False','False',111);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5','Validation, Sanitization and Encoding Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.1.1','Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, or environment variables).',235,34,NULL,'False','False',71);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.1.2','Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar. ([C5](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',915,34,5,'False','False',147);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.1.3','Verify that all input (HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc) is validated using positive validation (whitelisting)',20,34,6,'False','False',167);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.1.4','Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as checking that suburb and zip/postcode match). ([C5](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',20,34,6,'False','False',234);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.1.5','Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.',601,34,7,'False','False',67);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.2.1','Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature. ([C5](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',116,NULL,8,'False','False',180);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.2.2','Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length.',138,NULL,6,'False','False',269);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('5.2.3','Verify that the application sanitizes user input before passing to mail systems to protect against SMTP or IMAP injection.',147,NULL,9,'False','False',270);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.2.4','Verify that the application avoids the use of eval() or other dynamic code execution features. Where there is no alternative, any user input being included must be sanitized or sandboxed before being executed.',95,NULL,6,'False','False',4);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.2.5','Verify that the application protects against template injection attacks by ensuring that any user input being included is sanitized or sandboxed.',94,NULL,9,'False','False',267);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.2.6','Verify that the application protects against SSRF attacks, by validating or sanitizing untrusted data or HTTP file metadata, such as filenames and URL input fields, use whitelisting of protocols, domains, paths and ports.',918,NULL,6,'False','False',262);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('5.2.7','Verify that the application sanitizes, disables, or sandboxes user-supplied SVG scriptable content, especially as they relate to XSS resulting from inline scripts, and foreignObject.',159,NULL,10,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.2.8','Verify that the application sanitizes, disables, or sandboxes user-supplied scriptable or expression template language content, such as Markdown, CSS or XSL stylesheets, BBCode, or similar.',94,NULL,6,'False','False',289);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.3.1','Verify that output encoding is relevant for the interpreter and context required. For example, use encoders specifically for HTML values, HTML attributes, JavaScript, URL Parameters, HTTP headers, SMTP, and others as the context requires, especially from untrusted inputs (e.g. names with Unicode or apostrophes, such as ねこ or O''Hara).',116,35,11,'False','False',269);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.3.3','Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS.',79,35,11,'False','False',3);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.3.4','Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or are otherwise protected from database injection attacks. ([C3](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',89,35,12,'False','False',46);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.3.5','Verify that where parameterized or safer mechanisms are not present, context-specific output encoding is used to protect against injection attacks, such as the use of SQL escaping to protect against SQL injection.',89,35,12,'False','False',269);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.3.6','Verify that the application projects against JavaScript or JSON injection attacks, including for eval attacks, remote JavaScript includes, CSP bypasses, DOM XSS, and JavaScript expression evaluation.',830,35,11,'False','False',181);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.3.7','Verify that the application protects against LDAP Injection vulnerabilities, or that specific security controls to prevent LDAP Injection have been implemented. ([C4](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',943,35,13,'False','False',11);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('5.3.8','Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding. ([C4](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',78,35,14,'False','False',4);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('5.3.9','Verify that the application protects against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks.',829,35,15,'False','False',1);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('5.3.10','Verify that the application protects against XPath injection or XML injection attacks. ([C4](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',643,35,16,'False','False',183);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.5.1','Verify that serialized objects use integrity checks or are encrypted to prevent hostile object creation or data tampering.',502,NULL,18,'False','False',271);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.5.2','Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XXE.',611,NULL,18,'False','False',6);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('5.5.3','Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).',502,NULL,18,'False','False',271);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('5.5.4','Verify that when parsing JSON in browsers or JavaScript-based backends, JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON.',95,NULL,18,'False','False',181);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   (6.0,'Stored Cryptography Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.1.1','Verify that regulated private data is stored encrypted while at rest, such as personally identifiable information (PII); sensitive personal information, or data assessed likely to be subject to EU''s GDPR.',311,37,19,'False','False',207);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.1.2','Verify that regulated health data is stored encrypted while at rest, such as medical records, medical device details, or de-anonymized research records.',311,37,19,'False','False',207);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.1.3','Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records.',311,37,19,'False','False',207);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('6.2.1','Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.',310,37,19,'False','False',149);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('6.2.2','Verify that industry proven or government approved cryptographic algorithms, modes, and libraries are used, instead of custom coded cryptography. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',327,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.2.3','Verify that encryption initialization vector, cipher configuration, and block modes are configured securely using the latest advice.',326,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('6.2.4','Verify that random number, encryption or hashing algorithms, key lengths, rounds, ciphers or modes, can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',326,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.2.5','Verify that known insecure block modes (i.e. ECB, etc.); padding modes (i.e. PKCS#1 v1.5, etc.); ciphers with small block sizes (i.e. Triple-DES, Blowfish, etc.); and weak hashing algorithms (i.e. MD5, SHA1, etc.) are not used unless required for backwards compatibility.',326,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('6.2.6','Verify that nonces, initialization vectors, and other single use numbers must not be used more than once with a given encryption key. The method of generation must be appropriate for the algorithm being used.',326,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('6.2.7','Verify that encrypted data is authenticated via signatures, authenticated cipher modes, or HMAC to ensure that ciphertext is not altered by an unauthorized party.',326,51,19,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('6.3.1','Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module''s approved cryptographically secure random number generator when these random values are intended to be not guessable by an attacker.',338,NULL,20,'False','False',118);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.3.2','Verify that random GUIDs are created using the GUID v4 algorithm, and a cryptographically-secure pseudo-random number generator (CSPRNG). GUIDs created using other pseudo-random number generators may be predictable.',338,NULL,20,'False','False',298);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('6.3.3','Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances.',338,NULL,20,'False','False',205);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7','Error Handling and Logging Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.1.1','Verify that the application does not log credentials or payment details. Session tokens should only be stored in logs in an irreversible, hashed form. ([C9, C10](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',532,39,21,'False','False',78);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.1.2','Verify that the application does not log other sensitive data as defined under local privacy laws or relevant security policy. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',532,39,21,'False','False',78);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.1.3','Verify that the application logs security relevant events including successful and failed authentication events, access control failures, deserialization failures and input validation failures.',778,39,21,'False','False',83);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.1.4','Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',778,39,21,'False','False',99);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.2.1','Verify that all authentication decisions are logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.',778,39,21,'False','False',232);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('7.2.2','Verify that all access control decisions can be logged and all failed decisions are logged. This should include requests with relevant metadata needed for security investigations.',285,39,21,'False','False',232);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('7.3.1','Verify that the application appropriately encodes user-supplied data to prevent log injection. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',117,39,21,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('7.3.2','Verify that all events are protected from injection when viewed in log viewing software. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',117,39,21,'False','False',100);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('7.3.3','Verify that security logs are protected from unauthorized access and modification. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',200,39,21,'False','False',257);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('7.3.4','Verify that time sources are synchronized to the correct time and time zone. Strongly consider logging only in UTC if systems are global to assist with post-incident forensic analysis. ([C9](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',NULL,39,21,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('7.4.1','Verify that a generic message is shown when an unexpected or security sensitive error occurs, potentially with a unique ID which support personnel can use to investigate.  ([C10](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',210,NULL,NULL,'True','False',15);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('7.4.2','Verify that exception handling (or a functional equivalent) is used across the codebase to account for expected and unexpected error conditions. ([C10](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',544,NULL,NULL,'True','False',299);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('7.4.3','Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. ([C10](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',460,NULL,NULL,'True','False',299);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8','Data Protection Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.1.1','Verify the application protects sensitive data from being cached in server components such as load balancers and application caches.',524,43,25,'False','False',19);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.1.2','Verify that all cached or temporary copies of sensitive data stored on the server are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.',524,43,25,'False','False',145);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.1.4','Verify the application can detect and alert on abnormal numbers of requests, such as by IP, user, total per hour or day, or whatever makes sense for the application.',770,43,25,'False','False',125);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.1.5','Verify that regular backups of important data are performed and that test restoration of data is performed.',19,43,25,'False','False',300);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('8.1.6','Verify that backups are stored securely to prevent data from being stolen or corrupted.',19,43,25,'False','False',300);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES     ('8.2.1','Verify the application sets sufficient anti-caching headers so that sensitive data is not cached in modern browsers.',525,43,25,'False','False',19);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.2.2','Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII.',922,43,25,'False','False',190);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.2.3','Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated.',922,43,25,'False','False',190);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.3.1','Verify that sensitive data is sent to the server in the HTTP message body or headers, and that query string parameters from any HTTP verb do not contain sensitive data.',319,43,25,'False','False',72);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.3.2','Verify that users have a method to remove or export their data on demand.',212,43,25,'False','False',999);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.3.4','Verify that all sensitive data created and processed by the application has been identified, and ensure that a policy is in place on how to deal with sensitive data. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',200,43,25,'False','False',276);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.3.5','Verify accessing sensitive data is audited (without logging the sensitive data itself); if the data is collected under relevant data protection directives or where logging of access is required.',532,43,25,'False','False',235);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('8.3.6','Verify that sensitive information contained in memory is overwritten as soon as it is no longer required to mitigate memory dumping attacks, using zeroes or random data.',226,43,25,'False','False',135);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('8.3.7','Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provide both confidentiality and integrity. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',327,43,25,'False','False',276);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('8.3.8','Verify that sensitive personal information is subject to data retention classification, such that old or out of date data is deleted automatically, on a schedule, or as the situation requires.',285,43,25,'False','False',276);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('9','Communications Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('9.1.1','Verify that secured TLS is used for all client connectivity, and does not fall back to insecure or unencrypted protocols. ([C8](https://www.owasp.org/index.php/OWASP_Proactive_Controls#tab=Formal_Numbering))',319,44,22,'False','False',244);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('9.1.2','Verify using online or up to date TLS testing tools that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred.',326,44,22,'False','False',247);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('9.1.3','Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are disabled, such as SSLv2, SSLv3, or TLS 1 and TLS 1.1. The latest version of TLS should be the preferred cipher suite.',326,44,22,'False','False',247);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('9.2.1','Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected.',295,44,22,'False','False',101);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('9.2.2','Verify that encrypted communications such as TLS is used for all inbound and outbound connections, including for management ports, monitoring, authentication, API, or web service calls, database, cloud, serverless, mainframe, external, and partner connections. The server must not fall back to insecure or unencrypted protocols.',319,44,22,'False','False',302);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('9.2.4','Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured.',299,44,22,'False','False',139);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('9.2.5','Verify that backend TLS connection failures are logged.',544,44,22,'False','False',103);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('10','Malicious Code Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('10.1.1','Verify that a code analysis tool is in use that can detect potentially malicious code, such as time functions, unsafe file operations and network connections.',749,NULL,NULL,'True','False',301);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('10.3.2','Verify that the application employs integrity protections, such as code signing or sub-resource integrity. The application must not load or execute code from untrusted sources, such as loading includes, modules, plugins, code, or libraries from untrusted sources or the Internet.',353,47,1,'False','False',303);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('10.3.3','Verify that the application has protection from sub-domain takeovers if the application relies upon DNS entries or DNS sub-domains, such as expired domain names, out of date DNS pointers or CNAMEs, expired projects at public source code repos, or transient cloud APIs, serverless functions, or storage buckets (autogen-bucket-id.cloud.example.com) or similar. Protections can include ensuring that DNS names used by applications are regularly checked for expiry or change.',350,47,1,'False','False',294);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('11','Business Logic Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('11.1.1','Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.',841,NULL,NULL,'False','True',110);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('11.1.6','Verify the application does not suffer from "time of check to time of use" (TOCTOU) issues or other race conditions for sensitive operations.',367,NULL,NULL,'False','True',293);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('12','File and Resources Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.1.1','Verify that the application will not accept large files that could fill up storage or cause a denial of service attack.',400,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.1.2','Verify that compressed files are checked for "zip bombs" - small input files that will decompress into huge files thus exhausting file storage limits.',409,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('12.1.3','Verify that a file size quota and maximum number of files per user is enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files.',770,NULL,23,'False','False',116);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.2.1','Verify that files obtained from untrusted sources are validated to be of expected type based on the file''s content.',434,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.3.1','Verify that user-submitted filename metadata is not used directly with system or framework file and URL API to protect against path traversal.',22,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('12.3.2','Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI).',73,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.3.3','Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure or execution of remote files (RFI); which may also lead to SSRF.',98,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.3.4','Verify that the application protects against reflective file download (RFD) by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter, the response Content-Type header should be set to text/plain, and the Content-Disposition header should have a fixed filename.',641,NULL,23,'False','False',160);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.3.5','Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection.',78,NULL,23,'False','False',225);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.3.6','Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs.',829,NULL,23,'False','False',13);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.4.1','Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation.',922,NULL,23,'False','False',227);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.4.2','Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent upload of known malicious content.',509,NULL,23,'False','False',226);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.5.1','Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, backup files (e.g. .bak); temporary working files (e.g. .swp); compressed files (.zip, .tar.gz, etc) and other extensions commonly used by editors should be blocked unless required.',552,NULL,23,'False','False',288);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('12.5.2','Verify that direct requests to uploaded files will never be executed as HTML/JavaScript content.',434,NULL,23,'False','False',227);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13','API and Web Service Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13.1.3','Verify API URLs do not expose sensitive information, such as the API key, session tokens etc.',598,49,NULL,'False','False',91);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13.1.5','Verify that requests containing unexpected or missing content types are rejected with appropriate headers (HTTP response status 406 Unacceptable or 415 Unsupported Media Type).',434,49,NULL,'False','False',104);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES    ('13.2.1','Verify that enabled RESTful HTTP methods are a valid choice for the user or action, such as preventing normal users using DELETE or PUT on protected API or resources.',650,49,NULL,'False','False',129);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13.2.2','Verify that JSON schema validation is in place and verified before accepting input.',20,49,NULL,'False','False',286);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('13.2.3','Verify that RESTful web services that utilize cookies are protected from Cross-Site Request Forgery via the use of at least one or more of the following: triple or double submit cookie pattern (see [references](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)_Prevention_Cheat_Sheet)); CSRF nonces, or ORIGIN request header checks.',352,49,NULL,'False','False',224);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('13.2.5','Verify that REST services explicitly check the incoming Content-Type to be the expected one, such as application/xml or application/JSON.',436,49,NULL,'False','False',104);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('13.3.1','Verify that XSD schema validation takes place to ensure a properly formed XML document, followed by validation of each input field before any processing of that data takes place.',20,49,NULL,'False','False',175);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('13.3.2','Verify that the message payload is signed using WS-Security to ensure reliable transport between client and service.',345,49,NULL,'False','False',195);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13.4.1','Verify that query whitelisting or a combination of depth limiting and amount limiting should be used to prevent GraphQL or data layer expression denial of service (DoS) as a result of expensive, nested queries. For more advanced scenarios, query cost analysis should be used.',770,49,NULL,'False','False',285);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('13.4.2','Verify that GraphQL or other data layer authorization logic should be implemented at the business logic layer instead of the GraphQL layer.',285,49,NULL,'False','False',285);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14','Configuration Verification Requirements',NULL,NULL,NULL,'False','False',0);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14.1.1','Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation, automated configuration management, and automated deployment scripts.',NULL,1,1,'False','False',284);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14.1.5','Verify that authorized administrators can verify the integrity of all security-relevant configurations to detect tampering.',NULL,1,1,'False','False',237);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('14.2.2','Verify that all unneeded features, documentation, samples, configurations are removed, such as sample applications, platform documentation, and default or example users.',1002,1,1,'False','False',283);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14.2.3','Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset.',714,1,1,'False','False',223);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14.2.4','Verify that third party components come from pre-defined, trusted and continually maintained repositories.',829,1,1,'False','False',238);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('14.3.2','Verify that web or application server and application framework debug modes are disabled in production to eliminate debug features, developer consoles, and unintended security disclosures.',497,NULL,NULL,'False','True',16);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES  ('14.3.3','Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.',200,NULL,NULL,'True','False',130);
INSERT OR REPLACE INTO checklists_kb (checklistID, content, cwe, question_pre_ID, question_sprint_ID, include_first, include_always, kbID) VALUES   ('14.4.1','Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1).',173,NULL,NULL,'True','False',104);
