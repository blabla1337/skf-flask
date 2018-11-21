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
/*
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
*/

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
-- Table structure for table `questions_sprint`
--
drop table if exists `questions_sprint`;
CREATE TABLE `questions_sprint` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);

--
--ASVS lvl 1
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that send parameters and data any request methods other then POST and GET?");
--
--ASVS lvl 2
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (2, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (2, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
--
--ASVS lvl 3
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (3, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (3, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
--
--MASVS lvl 1
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--MASVS lvl 2
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--MASVS lvl 3
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--PCIDSS
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (7, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (7, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--CUSTOM
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (8, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (8, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");

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
--ASVS lvl 1
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (1, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (1, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--ASVS lvl 2
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (2, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (2, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--ASVS lvl 3
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a central Single Sign On service and validated this service using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a central Identity Management System service and validated this service using ASVS?");
--
--MASVS lvl 1
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (4, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (4, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--MASVS lvl 2
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (5, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (5, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--MASVS lvl 3
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a central Single Sign On service and validated this service using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a central Identity Management System service and validated this service using ASVS?");
--
--PCIDSS
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (7, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (7, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--CUSTOM
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (8, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (8, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");


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
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv1", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv2", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv3", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS Lv1", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS Lv2", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS Lv", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "PCIDSS", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "Custom", "TBD");


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
-- Table structure for table `checklists_post`
--
drop table if exists `checklists_post`;
CREATE TABLE `checklists_post` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255) NOT NULL,
`projectID` int(11) NOT NULL,
`sprintID` int(11) NOT NULL,
`status` int(11) NOT NULL,
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
CREATE TABLE `checklists_kb` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`content` varchar(255),
`question_sprint_ID` int(11),
`question_pre_ID` int(11),
`kbID` int(11),
`include_always` varchar(5),
`include_first` varchar(5),
`checklist_type` int(11)
); 

---
--- ASVS lvl 1 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.12', 'Verify that session ids stored in cookies have their path set to an appropriately restrictive value for the application, and authentication session tokens additionally set the "HttpOnly" and "secure" attributes', '92'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.24', 'Verify that if shared knowledge based questions (also known as "secret questions") are required, the questions do not violate privacy laws and are sufficiently strong to protect accounts from malicious recovery.', '87'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.2', 'Verify that the mobile app does not store sensitive data onto potentially unencrypted shared resources on the device (e.g. SD card or shared folders).', '212'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.1', 'Verify all pages and resources by default require authentication except those specifically intended to be public (Principle of complete mediation).', '45'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.2', 'Verify that access to administration and management functions within the Web Service Application is limited to web service administrators.', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '7.7', 'Verify that cryptographic algorithms used by the application have been validated against FIPS 1402 or an equivalent standard.', '119'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '8.1', 'Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information', '15'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.0', 'HTTP security configuration verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '1.0', 'Architecture, design and threat modelling', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.11', 'Verify that the app validates input to exported activities, intents, or content providers.', '221'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '7.2', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding.', '149'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.8', 'Verify the application code does not execute uploaded data obtained from untrusted sources.', '13'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.5', 'Verify that untrusted data is not used within crossdomain resource sharing (CORS) to protect against arbitrary remote content.', '112'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.0', 'Session Management Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.16', 'Verify that the application limits the number of active concurrent sessions.', '188'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '8.10', 'Verify that an audit log or similar allows for nonrepudiation of key transactions.', '107'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.16', 'Verify that the TLS settings are in line with current leading practice, particularly as common configurations, ciphers, and algorithms become insecure.', '247'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '9.0', 'Data protection verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '9.1', 'Verify that all forms containing sensitive information have disabled client side caching, including autocomplete features.', '140'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.3', 'Verify that TLS is used for all connections (including both external and backend connections) that are authenticated or that involve sensitive data or functions, and does not fall back to insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm.', '244'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.5', 'Verify that input validation routines are enforced on the server side.', '108'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.1', 'Verify that the runtime environment is not susceptible to buffer overflows, or that security controls prevent buffer overflows.', '146'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.0', 'Authentication Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.1', 'Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid.', '101'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.6', 'Verify all authentication controls fail securely to ensure attackers cannot log in.', '114'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.9', 'Do not use Flash, ActiveX, Silverlight, NACL, clientside Java or other client side technologies not supported natively via W3C browser standards.', '194'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.8', 'Verify all account identity authentication functions (such as update profile, forgot password, disabled / lost token, help desk or IVR) that might regain access to the account are at least as resistant to attack as the primary authentication mechanism.', '85'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '15.0', 'Business logic verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.5', 'Verify that all pages that require authentication have easy and visible access to logout functionality.', '90'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.7', 'Verify that the REST service is protected from CrossSite Request Forgery via the use of at least one or more of the following: ORIGIN checks, double submit cookie pattern, CSRF nonces, and referrer checks.', '224'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.22', 'Verify that forgotten password and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. Use of a random value in an email or SMS should be a last resort and is known weak.', '115'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.15', 'Ensure that all string variables placed into HTML or other web client code is either properly contextually encoded manually, or utilize templates that automatically encode contextually to ensure the application is not susceptible to reflected, stored and DOM CrossSite Scripting (XSS) attacks.', '3'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '8.0', 'Error handling and logging verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '1.1', 'Verify that all application components are identified and are known to be needed', '161'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.33', 'Browser autocomplete, and integration with password managers are permitted unless prohibited by risk based policy.', '209'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.0', 'Access Control Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.3', 'Verify that sessions timeout after a specified period of inactivity.', '60'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.5', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', '130'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.16', 'Verify that the application correctly enforces contextsensitive authorisation so as to not allow unauthorised manipulation by means of parameter tampering.', '241'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '13.0', 'Malicious controls verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.22', 'Make sure untrusted HTML from WYSIWYG editors or similar are properly sanitized with an HTML sanitizer and handle it appropriately according to the input validation task and encoding task.', '180'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.10', 'Verify that all SQL queries, HQL, OSQL, NOSQL and stored procedures, calling of stored procedures are protected by the use of prepared statements or query parameterization, and thus not susceptible to SQL injection', '46'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.7', 'Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent password managers, long passphrases or highly complex passwords being entered.', '59'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.4', 'Verify all authentication controls are enforced on the server side.', '43'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.1', 'Verify that ID values stored on the device and retrievable by other applications, such as the UDID or IMEI number are not used as authentication tokens.', '211'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.11', 'Verify that session ids are sufficiently long, random and unique across the correct active session base.', '55'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.0', 'Files and resources verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.18', 'Verify the user is prompted with the option to terminate all other active sessions after a successful change password process.', '254'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.17', 'Verify that the forgotten password function and other recovery paths do not reveal the current password and that the new password is not sent in clear text to the user.', '243'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.7', 'Verify that all successful authentication and reauthentication generates a new session and session id.', '58'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.6', 'Verify that the session id is never disclosed in URLs, error messages, or logs. This includes verifying that the application does not support URL rewriting of session cookies.', '91'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.0', 'Mobile verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.16', 'Verify that credentials are transported using a suitable encrypted link and that all pages/functions that require a user to enter credentials are done so using an encrypted link.', '122'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '8.13', 'Time sources should be synchronized to ensure logs have the correct time.', '210'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.1', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', '67'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '7.0', 'Cryptography at rest verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '19.1', 'All components should be up to date with proper security configuration(s) and version(s). This should include removal of unneeded configurations and folders such as sample applications, platform documentation, and default or example users.', '14'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.7', 'Verify that the application sensitive code is laid out unpredictably in memory (For example ASLR).', '217'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.4', 'Verify that all input is limited to an appropriate size limit.', '176'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '9.9', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '190'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.3', 'Verify that server side input validation failures result in request rejection and are logged.', '95'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.9', 'Verify that the same access control rules implied by the presentation layer are enforced on the server side.', '240'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.5', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', '61'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.1', 'Verify that the application accepts only a defined set of required HTTP request methods, such as GET and POST are accepted, and unused methods (e.g. TRACE, PUT, and DELETE) are explicitly blocked.', '129'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.32', 'Verify that administrative interfaces are not accessible to untrusted parties', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.13', 'Verify that the application is not susceptible to Remote File Inclusion (RFI) or Local File Inclusion (LFI) when content is used that is a path to a file.', '173'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.4', 'Verify that secret keys, API tokens, or passwords are dynamically generated in mobile applications.', '214'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.2', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF8, ISO 88591).', '104'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '19.0', 'Configuration', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.4', 'Verify that untrusted data is not used within inclusion, class loader, or reflection capabilities to prevent remote/local file inclusion vulnerabilities.', '250'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.9', 'Verify that the app does not export sensitive activities, intents, or content providers for other mobile apps on the same device to exploit.', '219'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.8', 'Verify that the XXSSProtection: 1; mode=block header is in place.', '21'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.12', 'Verify that the application is not susceptible to OS Command Injection, or that security controls prevent OS Command Injection.', '4'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '9.3', 'Verify that all sensitive data is sent to the server in the HTTP message body or headers (i.e., URL parameters are never used to send sensitive data).', '72'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.6', 'Verify the use of sessionbased authentication and authorization. Please refer to sections 2, 3 and 4 for further guidance. Avoid the use of static "API keys" and similar.', '152'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.0', 'Malicious input handling verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.14', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OSCP) Stapling, is enabled and configured.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.1', 'Verify that there is no custom session manager, or that the custom session manager is resistant against all common session management attacks.', '132'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.0', 'Communications security verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.0', 'Web services verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '17.3', 'Verify that sensitive data is not stored unprotected on the device, even in system protected areas such as key chains.', '213'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.3', 'Verify that files obtained from untrusted sources are validated to be of expected type and scanned by antivirus scanners to prevent upload of known malicious content.', '226'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.19', 'Verify there are no default passwords in use for the application framework or any components used by the application (such as "admin/password").', '63'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.4', 'Verify that access to sensitive records is protected, such that only authorized objects or data is accessible to each user (for example, protect against users tampering with a parameter to see or alter another user''s account).', '44'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.13', 'Ensure forward secrecy ciphers are in use to mitigate passive attackers recording traffic.', '170'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.6', 'Verify that all API responses contain XContentTypeOptions: nosniff and ContentDisposition: attachment; filename="api.json" (or other appropriate filename for the content type).', '193'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '16.2', 'Verify that untrusted file data submitted to the application is not used directly with file I/O commands,particularly to protect against path traversal, local file include, file mime type, and OS command injection vulnerabilities.', '225'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.1', 'Verify that the same encoding style is used between the client and the server.', '33'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.11', 'Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as StrictTransportSecurity: maxage=15724800; includeSubdomains', '192'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '10.15', 'Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy, including root and intermediary certificates of your selected certifying authority.', '198'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.18', 'Verify that information enumeration is not possible via login, password reset, or forgot account functionality.', '70'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '11.7', 'Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities.', '178'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.20', 'Verify that antiautomation is in place to prevent breached credential testing, brute forcing, and account lockout attacks.', '29'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.2', 'Verify that forms containing credentials are not filled in by the application. Prefilling by the application implies that credentials are stored in plaintext or a reversible format, which is explicitly prohibited.', '113'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.17', 'Verify that an active session list is displayed in the account profile or similar of each user. The user should be able to terminate any active session.', '253'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.8', 'Verify that access controls fail securely.', '242'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '3.2', 'Verify that sessions are invalidated when the user logs out.', '57'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.13', 'Verify that the application or framework uses strong random antiCSRF tokens or has another transaction protection mechanism.', '5'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.3', 'Verify that XML or JSON schema is in place and verified before accepting input.', '175'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.27', 'Verify that measures are in place to block the use of commonly chosen passwords and weak passphrases.', '222'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.14', 'Verify that the application is not susceptible to common XML attacks, such as XPath query tampering, XML External Entity attacks, and XML injection attacks.', '183'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '2.9', 'Verify that the changing password functionality includes the old password, the new password, and a password confirmation.', '86'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '9.4', 'Verify that the application sets appropriate anticaching headers as per the risk of the application, such as the following:
    Expires: Tue, 03 Jul 2001 06:00:00 GMT 
    LastModified: {now} GMT
    CacheControl: nostore, nocache, mustrevalidate, maxage=0 CacheControl: postcheck=0, precheck=0
    Pragma: nocache', '19'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '4.1', 'Verify that the principle of least privilege exists  users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', '126'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '18.5', 'Verify that SOAP based web services are compliant with Web ServicesInteroperability (WSI) Basic Profile at minimum. This essentially means TLS encryption.', '197'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '5.11', 'Verify that the application is not susceptible to LDAP Injection, or that security controls prevent LDAP Injection.', '11'); 
---
--- ASVS lvl 2 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.12', 'Verify that session ids stored in cookies have their path set to an appropriately restrictive value for the application, and authentication session tokens additionally set the "HttpOnly" and "secure" attributes', '92'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.24', 'Verify that if shared knowledge based questions (also known as "secret questions") are required, the questions do not violate privacy laws and are sufficiently strong to protect accounts from malicious recovery.', '87'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.2', 'Verify that the mobile app does not store sensitive data onto potentially unencrypted shared resources on the device (e.g. SD card or shared folders).', '212'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.1', 'Verify all pages and resources by default require authentication except those specifically intended to be public (Principle of complete mediation).', '45'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.2', 'Verify that access to administration and management functions within the Web Service Application is limited to web service administrators.', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.23', 'For autoescaping template technology, if UI escaping is disabled, ensure that HTML sanitization is enabled instead.', '189'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.7', 'Verify that cryptographic algorithms used by the application have been validated against FIPS 1402 or an equivalent standard.', '119'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.1', 'Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information', '15'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.3', 'Verify security logging controls provide the ability to log success and particularly failure events that are identified as securityrelevant.', '83'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.0', 'HTTP security configuration verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.14', 'Verify the system can protect against aggregate or continuous access of secured functions, resources, or data. For example, consider the use of a resource governor to limit the number of edits per hour or to prevent the entire database from being scraped by an individual user.', '116'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '15.1', 'Verify the application will only process business logic flows in sequential step order, with all steps being processed in realistic human time, and not process out of order, skipped steps, process steps from another user, or too quickly submitted transactions.', '110'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.5', 'Verify that the application build and deployment processes are performed in a secure fashion.', '199'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.5', 'Verify that on the server, all cached or temporary copies of sensitive data stored are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.', '145'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.0', 'Architecture, design and threat modelling', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.11', 'Verify that the app validates input to exported activities, intents, or content providers.', '221'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.2', 'Communications between components, such as between the application server and the database server, should be encrypted, particularly when the components are in different containers or on different systems.', '102'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.4', 'Verify that sessions timeout after an administrativelyconfigurable maximum time period regardless of activity (an absolute timeout).', '89'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.2', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding.', '149'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.6', 'Verify that files obtained from untrusted sources are stored outside the webroot, with limited permissions, preferably with strong validation.', '227'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.8', 'Verify the application code does not execute uploaded data obtained from untrusted sources.', '13'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.5', 'Verify that untrusted data is not used within crossdomain resource sharing (CORS) to protect against arbitrary remote content.', '112'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.0', 'Session Management Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.16', 'Verify that the application limits the number of active concurrent sessions.', '188'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.4', 'Verify application deployments are adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications.', '106'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.10', 'Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required.', '235'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.10', 'Verify that an audit log or similar allows for nonrepudiation of key transactions.', '107'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.2', 'Verify that error handling logic in security controls denies access by default.', '251'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.16', 'Verify that the TLS settings are in line with current leading practice, particularly as common configurations, ciphers, and algorithms become insecure.', '247'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.14', 'Verify that all keys and passwords are replaceable, and are generated or replaced at installation time.', '204'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.16', 'If the application framework allows automatic mass parameter assignment (also called automatic variable binding) from the inbound request to a model, verify that security sensitive fields such as "accountBalance", "role" or "password" are protected from malicious automatic binding.', '147'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.0', 'Data protection verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.1', 'Verify that all forms containing sensitive information have disabled client side caching, including autocomplete features.', '140'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.3', 'Verify that TLS is used for all connections (including both external and backend connections) that are authenticated or that involve sensitive data or functions, and does not fall back to insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm.', '244'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.13', 'Verify that sensitive passwords or key material maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '203'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.9', 'Verify that the message payload is signed to ensure reliable transport between client and service, using JSON Web Signing or WSSecurity for SOAP requests.', '195'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.5', 'Verify that input validation routines are enforced on the server side.', '108'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.25', 'Verify that the system can be configured to disallow the use of a configurable number of previous passwords.', '88'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.1', 'Verify that the runtime environment is not susceptible to buffer overflows, or that security controls prevent buffer overflows.', '146'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.21', 'Verify that unstructured data is sanitized to enforce generic safety measures such as allowed characters and length, and characters potentially harmful in given context should be escaped (e.g. natural names with Unicode or apostrophes, such as &x306D;&x3053; or O''Hara)', '202'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.5', 'Verify that the mobile app prevents leaking of sensitive information (for example, screenshots are saved of the current application as the application is backgrounded or writing sensitive information in console).', '215'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.0', 'Authentication Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.1', 'Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid.', '101'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.7', 'Verify that the web or application server is configured by default to deny access to remote resources or systems outside the web or application server.', '138'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.6', 'Verify all authentication controls fail securely to ensure attackers cannot log in.', '114'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.5', 'Verify that all events that include untrusted data will not execute as code in the intended log viewing software.', '100'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.9', 'Do not use Flash, ActiveX, Silverlight, NACL, clientside Java or other client side technologies not supported natively via W3C browser standards.', '194'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.8', 'Verify all account identity authentication functions (such as update profile, forgot password, disabled / lost token, help desk or IVR) that might regain access to the account are at least as resistant to attack as the primary authentication mechanism.', '85'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.3', 'Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application.', '131'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.6', 'Verify that the application is requesting minimal permissions for required functionality and resources.', '216'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.11', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '135'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.18', 'Verify that client side validation is used as a second line of defense, in addition to server side validation.', '166'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '15.0', 'Business logic verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.5', 'Verify that all pages that require authentication have easy and visible access to logout functionality.', '90'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.7', 'Verify that the REST service is protected from CrossSite Request Forgery via the use of at least one or more of the following: ORIGIN checks, double submit cookie pattern, CSRF nonces, and referrer checks.', '224'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.22', 'Verify that forgotten password and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. Use of a random value in an email or SMS should be a last resort and is known weak.', '115'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.8', 'Verify the REST service explicitly check the incoming ContentType to be the expected one, such as application/xml or application/json.', '160'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.15', 'Ensure that all string variables placed into HTML or other web client code is either properly contextually encoded manually, or utilize templates that automatically encode contextually to ensure the application is not susceptible to reflected, stored and DOM CrossSite Scripting (XSS) attacks.', '3'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.0', 'Error handling and logging verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.3', 'Communications between components, such as between the application server and the database server should be authenticated using an account with the least necessary privileges.', '246'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.1', 'Verify that all application components are identified and are known to be needed', '161'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.33', 'Browser autocomplete, and integration with password managers are permitted unless prohibited by risk based policy.', '209'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.0', 'Access Control Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.3', 'Verify that sessions timeout after a specified period of inactivity.', '60'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.5', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', '130'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.16', 'Verify that the application correctly enforces contextsensitive authorisation so as to not allow unauthorised manipulation by means of parameter tampering.', '241'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.24', 'Verify that data transferred from one DOM context to another, uses safe JavaScript methods, such as using .innerText and .val.', '179'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '13.0', 'Malicious controls verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.10', 'Verify that only session ids generated by the application framework are recognized as active by the application.', '56'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.22', 'Make sure untrusted HTML from WYSIWYG editors or similar are properly sanitized with an HTML sanitizer and handle it appropriately according to the input validation task and encoding task.', '180'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.17', 'Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, environment, etc.)', '71'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.26', 'Verify that risk based reauthentication, two factor or transaction signing is in place for high value transactions.', '233'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.10', 'Verify that all SQL queries, HQL, OSQL, NOSQL and stored procedures, calling of stored procedures are protected by the use of prepared statements or query parameterization, and thus not susceptible to SQL injection', '46'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.7', 'Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent password managers, long passphrases or highly complex passwords being entered.', '59'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.4', 'Verify all authentication controls are enforced on the server side.', '43'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.9', 'Verify the application has a clear separation between the data layer, controller layer and the display layer, such that security decisions can be enforced on trusted systems.', '185'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.20', 'Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as validating suburbs and zip or post codes match).', '234'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.1', 'Verify that ID values stored on the device and retrievable by other applications, such as the UDID or IMEI number are not used as authentication tokens.', '211'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.2', 'Verify that al components, such as libraries, modules, and external systems, that are not part of the application but that the application relies on to opperate are identified.', '162'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.15', 'Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce antifraud controls as per the risk of application and past fraud.', '111'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.11', 'Verify that session ids are sufficiently long, random and unique across the correct active session base.', '55'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.0', 'Files and resources verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.18', 'Verify the user is prompted with the option to terminate all other active sessions after a successful change password process.', '254'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.17', 'Verify that the forgotten password function and other recovery paths do not reveal the current password and that the new password is not sent in clear text to the user.', '243'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.10', 'Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code.', '74'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.7', 'Verify that all successful authentication and reauthentication generates a new session and session id.', '58'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.6', 'Verify that the session id is never disclosed in URLs, error messages, or logs. This includes verifying that the application does not support URL rewriting of session cookies.', '91'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.0', 'Mobile verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.8', 'Verify that components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups.', '206'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.16', 'Verify that credentials are transported using a suitable encrypted link and that all pages/functions that require a user to enter credentials are done so using an encrypted link.', '122'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.13', 'Time sources should be synchronized to ensure logs have the correct time.', '210'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.1', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', '67'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.0', 'Cryptography at rest verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.1', 'All components should be up to date with proper security configuration(s) and version(s). This should include removal of unneeded configurations and folders such as sample applications, platform documentation, and default or example users.', '14'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.12', 'Verify that all access control decisions can be logged and all failed decisions are logged.', '232'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.7', 'Verify that the application sensitive code is laid out unpredictably in memory (For example ASLR).', '217'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.4', 'Verify that all input is limited to an appropriate size limit.', '176'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.9', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '190'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.3', 'Verify that server side input validation failures result in request rejection and are logged.', '95'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.9', 'Verify that the same access control rules implied by the presentation layer are enforced on the server side.', '240'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.10', 'Verify that alternative and less secure access paths do not exist.', '80'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.5', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', '61'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.1', 'Verify that the application accepts only a defined set of required HTTP request methods, such as GET and POST are accepted, and unused methods (e.g. TRACE, PUT, and DELETE) are explicitly blocked.', '129'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.32', 'Verify that administrative interfaces are not accessible to untrusted parties', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.3', 'Verify that a highlevel architecture for the application has been defined.', '163'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.12', 'Personally Identifiable Information should be stored encrypted at rest and ensure that communication goes via protected channels.', '207'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.13', 'Verify that the application is not susceptible to Remote File Inclusion (RFI) or Local File Inclusion (LFI) when content is used that is a path to a file.', '173'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.9', 'Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced.', '121'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.4', 'Verify that secret keys, API tokens, or passwords are dynamically generated in mobile applications.', '214'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.2', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF8, ISO 88591).', '104'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '19.0', 'Configuration', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.6', 'Verify that security logs are protected from unauthorized access and modification.', '257'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.4', 'Verify that untrusted data is not used within inclusion, class loader, or reflection capabilities to prevent remote/local file inclusion vulnerabilities.', '250'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.9', 'Verify that the app does not export sensitive activities, intents, or content providers for other mobile apps on the same device to exploit.', '219'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.8', 'Verify that the XXSSProtection: 1; mode=block header is in place.', '21'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.12', 'Verify that the application is not susceptible to OS Command Injection, or that security controls prevent OS Command Injection.', '4'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.3', 'Verify that all sensitive data is sent to the server in the HTTP message body or headers (i.e., URL parameters are never used to send sensitive data).', '72'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.6', 'Verify the use of sessionbased authentication and authorization. Please refer to sections 2, 3 and 4 for further guidance. Avoid the use of static "API keys" and similar.', '152'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.25', 'Verify when parsing JSON in browsers, that JSON.parse is used to parse JSON on the client. Do not use eval() to parse JSON on the client.', '181'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.0', 'Malicious input handling verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.14', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OSCP) Stapling, is enabled and configured.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.7', 'Verify that the application does not log sensitive data as defined under local privacy laws or regulations, organizational sensitive data as defined by a risk assessment, or sensitive authentication data that could assist an attacker, including user''s session identifiers, passwords, hashes, or API tokens.', '78'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.10', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '220'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.10', 'Verify that TLS certificate public key pinning (HPKP) is implemented with production and backup public keys. For more information, please see the references below.', '168'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.1', 'Verify that there is no custom session manager, or that the custom session manager is resistant against all common session management attacks.', '132'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.0', 'Communications security verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.0', 'Web services verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '17.3', 'Verify that sensitive data is not stored unprotected on the device, even in system protected areas such as key chains.', '213'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.23', 'Verify that account lockout is divided into soft and hard lock status, and these are not mutually exclusive. If an account is temporarily soft locked out due to a brute force attack, this should not reset the hard lock status.', '182'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.7', 'Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values.', '142'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.3', 'Verify that files obtained from untrusted sources are validated to be of expected type and scanned by antivirus scanners to prevent upload of known malicious content.', '226'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.19', 'Verify there are no default passwords in use for the application framework or any components used by the application (such as "admin/password").', '63'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '15.2', 'Verify the application has business limits and correctly enforces on a per user basis, with configurable alerting and automated reactions to automated or unusual attack.', '125'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.4', 'Verify that a suitable XFRAMEOPTIONS header is in use for sites where content should not be viewed in a 3rdparty XFrame.', '20'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.4', 'Verify that access to sensitive records is protected, such that only authorized objects or data is accessible to each user (for example, protect against users tampering with a parameter to see or alter another user''s account).', '44'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.13', 'Ensure forward secrecy ciphers are in use to mitigate passive attackers recording traffic.', '170'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.6', 'Verify that all API responses contain XContentTypeOptions: nosniff and ContentDisposition: attachment; filename="api.json" (or other appropriate filename for the content type).', '193'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.11', 'Verify that all application components, libraries, modules, frameworks, platform, and operating systems are free from known vulnerabilities.', '208'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.26', 'Verify that authenticated data is cleared from client storage, such as the browser DOM, after the session is terminated.', '249'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '16.2', 'Verify that untrusted file data submitted to the application is not used directly with file I/O commands,particularly to protect against path traversal, local file include, file mime type, and OS command injection vulnerabilities.', '225'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.1', 'Verify that the same encoding style is used between the client and the server.', '33'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.11', 'Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as StrictTransportSecurity: maxage=15724800; includeSubdomains', '192'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.15', 'Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy, including root and intermediary certificates of your selected certifying authority.', '198'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.18', 'Verify that information enumeration is not possible via login, password reset, or forgot account functionality.', '70'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.10', 'Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized.', '258'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '7.6', 'Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module''s approved random number generator when these random values are intended to be not guessable by an attacker.', '118'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '11.7', 'Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities.', '178'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.20', 'Verify that antiautomation is in place to prevent breached credential testing, brute forcing, and account lockout attacks.', '29'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.2', 'Verify that forms containing credentials are not filled in by the application. Prefilling by the application implies that credentials are stored in plaintext or a reversible format, which is explicitly prohibited.', '113'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.17', 'Verify that an active session list is displayed in the account profile or similar of each user. The user should be able to terminate any active session.', '253'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.8', 'Verify that access controls fail securely.', '242'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '8.4', 'Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens.', '99'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.21', 'Verify that all authentication credentials for accessing services external to the application are encrypted and stored in a protected location.', '65'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.19', 'Verify that all input data is validated, not only HTML form fields but all sources of input such as REST calls, query parameters, HTTP headers, cookies, batch files, RSS feeds, etc; using positive validation (whitelisting), then lesser forms of validation such as greylisting (eliminating known bad strings), or rejecting bad inputs (blacklisting).', '167'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.12', 'Verify that all authentication decisions can be logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.', '76'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '10.6', 'Verify that all connections to external systems that involve sensitive information or functions are authenticated.', '84'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '3.2', 'Verify that sessions are invalidated when the user logs out.', '57'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.31', 'Verify that if an application allows users to authenticate, they can authenticate using twofactor authentication or other strong authentication, or any similar scheme that provides protection against username + password disclosure.', '231'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.13', 'Verify that the application or framework uses strong random antiCSRF tokens or has another transaction protection mechanism.', '5'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.3', 'Verify that XML or JSON schema is in place and verified before accepting input.', '175'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.27', 'Verify that measures are in place to block the use of commonly chosen passwords and weak passphrases.', '222'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.7', 'Verify all security controls (including libraries that call external security services) have a centralized implementation.', '184'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.14', 'Verify that the application is not susceptible to common XML attacks, such as XPath query tampering, XML External Entity attacks, and XML injection attacks.', '183'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.9', 'Verify that the changing password functionality includes the old password, the new password, and a password confirmation.', '86'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '9.4', 'Verify that the application sets appropriate anticaching headers as per the risk of the application, such as the following:
    Expires: Tue, 03 Jul 2001 06:00:00 GMT 
    LastModified: {now} GMT
    CacheControl: nostore, nocache, mustrevalidate, maxage=0 CacheControl: postcheck=0, precheck=0
    Pragma: nocache', '19'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '4.1', 'Verify that the principle of least privilege exists  users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', '126'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '18.5', 'Verify that SOAP based web services are compliant with Web ServicesInteroperability (WSI) Basic Profile at minimum. This essentially means TLS encryption.', '197'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '2.13', 'Verify that account passwords are one way hashed with a salt, and there is sufficient work factor to defeat brute force and password hash recovery attacks.', '51'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '5.11', 'Verify that the application is not susceptible to LDAP Injection, or that security controls prevent LDAP Injection.', '11');
---
--- ASVS lvl 3 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.12', 'Verify that session ids stored in cookies have their path set to an appropriately restrictive value for the application, and authentication session tokens additionally set the "HttpOnly" and "secure" attributes', '92'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.24', 'Verify that if shared knowledge based questions (also known as "secret questions") are required, the questions do not violate privacy laws and are sufficiently strong to protect accounts from malicious recovery.', '87'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.2', 'Verify that the mobile app does not store sensitive data onto potentially unencrypted shared resources on the device (e.g. SD card or shared folders).', '212'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1', 'Verify all pages and resources by default require authentication except those specifically intended to be public (Principle of complete mediation).', '45'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.2', 'Verify that access to administration and management functions within the Web Service Application is limited to web service administrators.', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.23', 'For autoescaping template technology, if UI escaping is disabled, ensure that HTML sanitization is enabled instead.', '189'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.7', 'Verify that cryptographic algorithms used by the application have been validated against FIPS 1402 or an equivalent standard.', '119'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.1', 'Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information', '15'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.3', 'Verify security logging controls provide the ability to log success and particularly failure events that are identified as securityrelevant.', '83'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.8', 'Verify that there are antidebugging techniques present that are sufficient enough to deter or delay likely attackers from injecting debuggers into the mobile app (For example GDB).', '218'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.0', 'HTTP security configuration verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.14', 'Verify the system can protect against aggregate or continuous access of secured functions, resources, or data. For example, consider the use of a resource governor to limit the number of edits per hour or to prevent the entire database from being scraped by an individual user.', '116'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.1', 'Verify the application will only process business logic flows in sequential step order, with all steps being processed in realistic human time, and not process out of order, skipped steps, process steps from another user, or too quickly submitted transactions.', '110'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.5', 'Verify that the application build and deployment processes are performed in a secure fashion.', '199'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.5', 'Verify that on the server, all cached or temporary copies of sensitive data stored are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.', '145'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.6', 'Verify that a threat model for the target application has been produced and covers off risks associated with Spoofing, Tampering, Repudiation, Information Disclosure, and Elevation of privilege (STRIDE).', '172'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.0', 'Architecture, design and threat modelling', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.11', 'Verify that the app validates input to exported activities, intents, or content providers.', '221'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.2', 'Communications between components, such as between the application server and the database server, should be encrypted, particularly when the components are in different containers or on different systems.', '102'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4', 'Verify that sessions timeout after an administrativelyconfigurable maximum time period regardless of activity (an absolute timeout).', '89'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.2', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable oracle padding.', '149'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.6', 'Verify that files obtained from untrusted sources are stored outside the webroot, with limited permissions, preferably with strong validation.', '227'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.8', 'Verify the application code does not execute uploaded data obtained from untrusted sources.', '13'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.5', 'Verify that untrusted data is not used within crossdomain resource sharing (CORS) to protect against arbitrary remote content.', '112'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.0', 'Session Management Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.16', 'Verify that the application limits the number of active concurrent sessions.', '188'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.4', 'Verify application deployments are adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications.', '106'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.10', 'Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required.', '235'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.10', 'Verify that an audit log or similar allows for nonrepudiation of key transactions.', '107'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.2', 'Verify that error handling logic in security controls denies access by default.', '251'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.28', 'Verify that all authentication challenges, whether successful or failed, should respond in the same average response time.', '165'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.11', 'Verify that security logs have some form of integrity checking or controls to prevent unauthorized modification.', '256'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.11', 'Verify that all consumers of cryptographic services do not have direct access to key material. Isolate cryptographic processes, including master secrets and consider the use of a virtualized or physical hardware key vault (HSM).', '196'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.2', 'Verify that the application source code, and as many third party libraries as possible, does not contain back doors, Easter eggs, and logic flaws in authentication, access control, input validation, and the business logic of high value transactions.', '105'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.16', 'Verify that the TLS settings are in line with current leading practice, particularly as common configurations, ciphers, and algorithms become insecure.', '247'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.14', 'Verify that all keys and passwords are replaceable, and are generated or replaced at installation time.', '204'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.16', 'If the application framework allows automatic mass parameter assignment (also called automatic variable binding) from the inbound request to a model, verify that security sensitive fields such as "accountBalance", "role" or "password" are protected from malicious automatic binding.', '147'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.0', 'Data protection verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.1', 'Verify that all forms containing sensitive information have disabled client side caching, including autocomplete features.', '140'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.3', 'Verify that TLS is used for all connections (including both external and backend connections) that are authenticated or that involve sensitive data or functions, and does not fall back to insecure or unencrypted protocols. Ensure the strongest alternative is the preferred algorithm.', '244'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.13', 'Verify that sensitive passwords or key material maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '203'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.2', 'Verify that the list of sensitive data processed by the application is identified, and that there is an explicit policy for how access to this data must be controlled, encrypted and enforced under relevant data protection directives.', '261'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.9', 'Verify that the message payload is signed to ensure reliable transport between client and service, using JSON Web Signing or WSSecurity for SOAP requests.', '195'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.5', 'Verify that input validation routines are enforced on the server side.', '108'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.25', 'Verify that the system can be configured to disallow the use of a configurable number of previous passwords.', '88'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1', 'Verify that the runtime environment is not susceptible to buffer overflows, or that security controls prevent buffer overflows.', '146'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.21', 'Verify that unstructured data is sanitized to enforce generic safety measures such as allowed characters and length, and characters potentially harmful in given context should be escaped (e.g. natural names with Unicode or apostrophes, such as &x306D;&x3053; or O''Hara)', '202'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.5', 'Verify that the mobile app prevents leaking of sensitive information (for example, screenshots are saved of the current application as the application is backgrounded or writing sensitive information in console).', '215'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.0', 'Authentication Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.1', 'Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid.', '101'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.8', 'Verify that there is a single standard TLS implementation that is used by the application that is configured to operate in an approved mode of operation.', '127'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.7', 'Verify that the web or application server is configured by default to deny access to remote resources or systems outside the web or application server.', '138'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6', 'Verify all authentication controls fail securely to ensure attackers cannot log in.', '114'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.5', 'Verify that all events that include untrusted data will not execute as code in the intended log viewing software.', '100'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.9', 'Do not use Flash, ActiveX, Silverlight, NACL, clientside Java or other client side technologies not supported natively via W3C browser standards.', '194'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8', 'Verify all account identity authentication functions (such as update profile, forgot password, disabled / lost token, help desk or IVR) that might regain access to the account are at least as resistant to attack as the primary authentication mechanism.', '85'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.3', 'Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application.', '131'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.6', 'Verify that the application is requesting minimal permissions for required functionality and resources.', '216'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.11', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '135'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.9', 'Verify that log fields from trusted and untrusted sources are distinguishable in log entries.', '134'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.5', 'Verify that certificate paths are built and verified for all client certificates using configured trust anchors and revocation information.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.18', 'Verify that client side validation is used as a second line of defense, in addition to server side validation.', '166'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.11', 'Verify that there is a centralized mechanism (including libraries that call external authorization services) for protecting access to each type of protected resource.', '259'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.0', 'Business logic verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.5', 'Verify that all pages that require authentication have easy and visible access to logout functionality.', '90'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.7', 'Verify that the REST service is protected from CrossSite Request Forgery via the use of at least one or more of the following: ORIGIN checks, double submit cookie pattern, CSRF nonces, and referrer checks.', '224'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.22', 'Verify that forgotten password and other recovery paths use a TOTP or other soft token, mobile push, or other offline recovery mechanism. Use of a random value in an email or SMS should be a last resort and is known weak.', '115'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.8', 'Verify the REST service explicitly check the incoming ContentType to be the expected one, such as application/xml or application/json.', '160'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.8', 'Verify that cryptographic modules operate in their approved mode according to their published security policies.', '141'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.15', 'Ensure that all string variables placed into HTML or other web client code is either properly contextually encoded manually, or utilize templates that automatically encode contextually to ensure the application is not susceptible to reflected, stored and DOM CrossSite Scripting (XSS) attacks.', '3'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.0', 'Error handling and logging verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.3', 'Communications between components, such as between the application server and the database server should be authenticated using an account with the least necessary privileges.', '246'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.1', 'Verify that all application components are identified and are known to be needed', '161'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.33', 'Browser autocomplete, and integration with password managers are permitted unless prohibited by risk based policy.', '209'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.0', 'Access Control Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.6', 'Verify that a single input validation control is used by the application for each type of data that is accepted.', '96'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3', 'Verify that sessions timeout after a specified period of inactivity.', '60'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.5', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', '130'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.16', 'Verify that the application correctly enforces contextsensitive authorisation so as to not allow unauthorised manipulation by means of parameter tampering.', '241'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.24', 'Verify that data transferred from one DOM context to another, uses safe JavaScript methods, such as using .innerText and .val.', '179'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.0', 'Malicious controls verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.10', 'Verify that only session ids generated by the application framework are recognized as active by the application.', '56'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.22', 'Make sure untrusted HTML from WYSIWYG editors or similar are properly sanitized with an HTML sanitizer and handle it appropriately according to the input validation task and encoding task.', '180'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.17', 'Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, environment, etc.)', '71'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.26', 'Verify that risk based reauthentication, two factor or transaction signing is in place for high value transactions.', '233'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.10', 'Verify that all SQL queries, HQL, OSQL, NOSQL and stored procedures, calling of stored procedures are protected by the use of prepared statements or query parameterization, and thus not susceptible to SQL injection', '46'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.29', 'Verify that secrets, API keys, and passwords are not included in the source code, or online source code repositories.', '251'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.12', 'Verify that the logs are stored on a different partition than the application is running with proper log rotation.', '191'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7', 'Verify password entry fields allow, or encourage, the use of passphrases, and do not prevent password managers, long passphrases or highly complex passwords being entered.', '59'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4', 'Verify all authentication controls are enforced on the server side.', '43'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.9', 'Verify the application has a clear separation between the data layer, controller layer and the display layer, such that security decisions can be enforced on trusted systems.', '185'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.20', 'Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as validating suburbs and zip or post codes match).', '234'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.1', 'Verify that ID values stored on the device and retrievable by other applications, such as the UDID or IMEI number are not used as authentication tokens.', '211'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.2', 'Verify that al components, such as libraries, modules, and external systems, that are not part of the application but that the application relies on to opperate are identified.', '162'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.15', 'Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce antifraud controls as per the risk of application and past fraud.', '111'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.11', 'Verify that session ids are sufficiently long, random and unique across the correct active session base.', '55'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.0', 'Files and resources verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.18', 'Verify the user is prompted with the option to terminate all other active sessions after a successful change password process.', '254'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.17', 'Verify that the forgotten password function and other recovery paths do not reveal the current password and that the new password is not sent in clear text to the user.', '243'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.10', 'Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code.', '74'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.7', 'Verify that all successful authentication and reauthentication generates a new session and session id.', '58'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.6', 'Verify that the session id is never disclosed in URLs, error messages, or logs. This includes verifying that the application does not support URL rewriting of session cookies.', '91'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.0', 'Mobile verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.8', 'Verify that components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups.', '206'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.16', 'Verify that credentials are transported using a suitable encrypted link and that all pages/functions that require a user to enter credentials are done so using an encrypted link.', '122'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.13', 'Time sources should be synchronized to ensure logs have the correct time.', '210'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.1', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', '67'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.0', 'Cryptography at rest verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.1', 'All components should be up to date with proper security configuration(s) and version(s). This should include removal of unneeded configurations and folders such as sample applications, platform documentation, and default or example users.', '14'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.8', 'Verify the application has the ability to detect and alert on abnormal numbers of requests for data harvesting for an example screen scraping.', '125'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.12', 'Verify that all access control decisions can be logged and all failed decisions are logged.', '232'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.7', 'Verify that the application sensitive code is laid out unpredictably in memory (For example ASLR).', '217'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.4', 'Verify that all input is limited to an appropriate size limit.', '176'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.9', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '190'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.4', 'Verify that all application components are defined in terms of the business functions and/or security functions they provide.', '258'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3', 'Verify that server side input validation failures result in request rejection and are logged.', '95'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.9', 'Verify that the same access control rules implied by the presentation layer are enforced on the server side.', '240'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.5', 'Verify that all components that are not part of the application but that the application relies on to operate are defined in terms of the functions, and/or security functions, they provide.', '260'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.10', 'Verify that alternative and less secure access paths do not exist.', '80'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.5', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', '61'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.1', 'Verify that the application accepts only a defined set of required HTTP request methods, such as GET and POST are accepted, and unused methods (e.g. TRACE, PUT, and DELETE) are explicitly blocked.', '129'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.32', 'Verify that administrative interfaces are not accessible to untrusted parties', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.3', 'Verify that a highlevel architecture for the application has been defined.', '163'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.12', 'Personally Identifiable Information should be stored encrypted at rest and ensure that communication goes via protected channels.', '207'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.13', 'Verify that the application is not susceptible to Remote File Inclusion (RFI) or Local File Inclusion (LFI) when content is used that is a path to a file.', '173'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.9', 'Verify that there is an explicit policy for how cryptographic keys are managed (e.g., generated, distributed, revoked, and expired). Verify that this key lifecycle is properly enforced.', '121'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.4', 'Verify that secret keys, API tokens, or passwords are dynamically generated in mobile applications.', '214'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.6', 'Verify that there is a method to remove each type of sensitive data from the application at the end of the required retention policy.', '135'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.2', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF8, ISO 88591).', '104'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.15', 'Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances.', '205'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.0', 'Configuration', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.6', 'Verify that security logs are protected from unauthorized access and modification.', '257'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.4', 'Verify that untrusted data is not used within inclusion, class loader, or reflection capabilities to prevent remote/local file inclusion vulnerabilities.', '250'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.9', 'Verify that the app does not export sensitive activities, intents, or content providers for other mobile apps on the same device to exploit.', '219'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.8', 'Verify that the XXSSProtection: 1; mode=block header is in place.', '21'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.6', 'Verify that authorised administrators have the capability to verify the integrity of all securityrelevant configurations to ensure that they have not been tampered with.', '237'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.12', 'Verify that the application is not susceptible to OS Command Injection, or that security controls prevent OS Command Injection.', '4'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.3', 'Verify that all sensitive data is sent to the server in the HTTP message body or headers (i.e., URL parameters are never used to send sensitive data).', '72'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.6', 'Verify the use of sessionbased authentication and authorization. Please refer to sections 2, 3 and 4 for further guidance. Avoid the use of static "API keys" and similar.', '152'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.25', 'Verify when parsing JSON in browsers, that JSON.parse is used to parse JSON on the client. Do not use eval() to parse JSON on the client.', '181'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.0', 'Malicious input handling verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.14', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OSCP) Stapling, is enabled and configured.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.7', 'Verify that the application does not log sensitive data as defined under local privacy laws or regulations, organizational sensitive data as defined by a risk assessment, or sensitive authentication data that could assist an attacker, including user''s session identifiers, passwords, hashes, or API tokens.', '78'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.10', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it no longer required, to mitigate memory dumping attacks.', '220'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.10', 'Verify that TLS certificate public key pinning (HPKP) is implemented with production and backup public keys. For more information, please see the references below.', '168'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.1', 'Verify that there is no custom session manager, or that the custom session manager is resistant against all common session management attacks.', '132'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.0', 'Communications security verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.0', 'Web services verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '17.3', 'Verify that sensitive data is not stored unprotected on the device, even in system protected areas such as key chains.', '213'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.23', 'Verify that account lockout is divided into soft and hard lock status, and these are not mutually exclusive. If an account is temporarily soft locked out due to a brute force attack, this should not reset the hard lock status.', '182'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.7', 'Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values.', '142'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.3', 'Verify that files obtained from untrusted sources are validated to be of expected type and scanned by antivirus scanners to prevent upload of known malicious content.', '226'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.19', 'Verify there are no default passwords in use for the application framework or any components used by the application (such as "admin/password").', '63'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.7', 'Verify that all application components are signed.', '200'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.2', 'Verify the application has business limits and correctly enforces on a per user basis, with configurable alerting and automated reactions to automated or unusual attack.', '125'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.4', 'Verify that a suitable XFRAMEOPTIONS header is in use for sites where content should not be viewed in a 3rdparty XFrame.', '20'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.4', 'Verify that access to sensitive records is protected, such that only authorized objects or data is accessible to each user (for example, protect against users tampering with a parameter to see or alter another user''s account).', '44'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.13', 'Ensure forward secrecy ciphers are in use to mitigate passive attackers recording traffic.', '170'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.6', 'Verify that all API responses contain XContentTypeOptions: nosniff and ContentDisposition: attachment; filename="api.json" (or other appropriate filename for the content type).', '193'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.11', 'Verify that all application components, libraries, modules, frameworks, platform, and operating systems are free from known vulnerabilities.', '208'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.26', 'Verify that authenticated data is cleared from client storage, such as the browser DOM, after the session is terminated.', '249'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.2', 'Verify that untrusted file data submitted to the application is not used directly with file I/O commands,particularly to protect against path traversal, local file include, file mime type, and OS command injection vulnerabilities.', '225'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.1', 'Verify that the same encoding style is used between the client and the server.', '33'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.1', 'Verify all malicious activity is adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications.', '239'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.9', 'Ensure that build processes for system level languages have all security flags enabled, such as ASLR, DEP, and security checks.', '201'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.11', 'Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as StrictTransportSecurity: maxage=15724800; includeSubdomains', '192'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.15', 'Verify that only strong algorithms, ciphers, and protocols are used, through all the certificate hierarchy, including root and intermediary certificates of your selected certifying authority.', '198'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.12', 'Verify that production website URL has been submitted to preloaded list of Strict Transport Security domains maintained by web browser vendors.', '255'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.18', 'Verify that information enumeration is not possible via login, password reset, or forgot account functionality.', '70'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.10', 'Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized.', '258'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.6', 'Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module''s approved random number generator when these random values are intended to be not guessable by an attacker.', '118'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.7', 'Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities.', '178'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.4', 'Verify that backend TLS connection failures are logged.', '103'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.10', 'Verify that all application assets are hosted by the application, such as JavaScript libraries, CSS stylesheets and web fonts are hosted by the application rather than rely on a CDN or external provider.', '223'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.20', 'Verify that antiautomation is in place to prevent breached credential testing, brute forcing, and account lockout attacks.', '29'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.2', 'Verify that forms containing credentials are not filled in by the application. Prefilling by the application implies that credentials are stored in plaintext or a reversible format, which is explicitly prohibited.', '113'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.17', 'Verify that an active session list is displayed in the account profile or similar of each user. The user should be able to terminate any active session.', '253'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.8', 'Verify that access controls fail securely.', '242'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.4', 'Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens.', '99'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.21', 'Verify that all authentication credentials for accessing services external to the application are encrypted and stored in a protected location.', '65'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.19', 'Verify that all input data is validated, not only HTML form fields but all sources of input such as REST calls, query parameters, HTTP headers, cookies, batch files, RSS feeds, etc; using positive validation (whitelisting), then lesser forms of validation such as greylisting (eliminating known bad strings), or rejecting bad inputs (blacklisting).', '167'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.12', 'Verify that all authentication decisions can be logged, without storing sensitive session identifiers or passwords. This should include requests with relevant metadata needed for security investigations.', '76'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.6', 'Verify that all connections to external systems that involve sensitive information or functions are authenticated.', '84'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2', 'Verify that sessions are invalidated when the user logs out.', '57'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.31', 'Verify that if an application allows users to authenticate, they can authenticate using twofactor authentication or other strong authentication, or any similar scheme that provides protection against username + password disclosure.', '231'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.13', 'Verify that the application or framework uses strong random antiCSRF tokens or has another transaction protection mechanism.', '5'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.3', 'Verify that XML or JSON schema is in place and verified before accepting input.', '175'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.27', 'Verify that measures are in place to block the use of commonly chosen passwords and weak passphrases.', '222'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.7', 'Verify all security controls (including libraries that call external security services) have a centralized implementation.', '184'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.14', 'Verify that the application is not susceptible to common XML attacks, such as XPath query tampering, XML External Entity attacks, and XML injection attacks.', '183'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9', 'Verify that the changing password functionality includes the old password, the new password, and a password confirmation.', '86'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.4', 'Verify that the application sets appropriate anticaching headers as per the risk of the application, such as the following:
    Expires: Tue, 03 Jul 2001 06:00:00 GMT 
    LastModified: {now} GMT
    CacheControl: nostore, nocache, mustrevalidate, maxage=0 CacheControl: postcheck=0, precheck=0
    Pragma: nocache', '19'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.1', 'Verify that the principle of least privilege exists  users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', '126'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.8', 'Verify that third party components come from trusted repositories.', '238'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.5', 'Verify that SOAP based web services are compliant with Web ServicesInteroperability (WSI) Basic Profile at minimum. This essentially means TLS encryption.', '197'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.8', 'Verify that all nonprintable symbols and field separators are properly encoded in log entries, to prevent log injection.', '236'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.13', 'Verify that account passwords are one way hashed with a salt, and there is sufficient work factor to defeat brute force and password hash recovery attacks.', '51'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.11', 'Verify that the application is not susceptible to LDAP Injection, or that security controls prevent LDAP Injection.', '11'); 
---
--- MASVS lvl 1 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.1', 'All app components are identified and known to be needed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- MASVS lvl 2 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.6', 'Biometric authentication, if any, is not eventbound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.10', 'The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.9', 'Stepup authentication is required to enable actions that deal with sensitive data or transactions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.4', 'The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.8', 'A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.7', 'Sessions are terminated at the remote endpoint after a predefined period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.12', 'The app educates the user about the types of personally identifiable information processed, as well as security best practices the user should follow in using the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.10', 'All components that are not part of the application but that the application relies on to operate, are clearly identified and the security implications of using those components are known.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.7', 'A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.1', 'All app components are identified and known to be needed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.13', 'Security is addressed within all parts of the software development lifecycle.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.8', 'No sensitive data is included in backups generated by the mobile operating system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.9', 'All security controls have a centralized implementation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.11', 'The app enforces a minimum deviceaccesssecurity policy, such as requiring the user to set a device passcode.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.5', 'The app doesn''t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrolments and account recovery.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.10', 'The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.8', 'All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.9', 'The app removes sensitive data from views when backgrounded.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.12', 'Remote endpoints verify that connecting clients use an uptodate version of the mobile app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.11', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 80057.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- MASVS lvl 3 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.11', 'The app uses multiple functionally independent methods of emulator detection that, in context of the overall protection scheme, force adversaries to invest significant manual effort to run the app in an emulator (supersedes requirement 8.7).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.6', 'Biometric authentication, if any, is not eventbound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.7', 'The app implements multiple different responses to tampering, debugging and emulation, including stealthy responses that don''t simply terminate the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.1', 'The app implements two or more functionally independent methods of root detection and responds to the presence of a rooted device either by alerting the user or terminating the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.4', 'The app detects the presence of widely used reverse engineering tools, such as code injection tools, hooking frameworks and debugging servers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.10', 'The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.5', 'The app detects, and response to, being run in an emulator using any method.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.9', 'Stepup authentication is required to enable actions that deal with sensitive data or transactions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.4', 'The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.10', 'The app implements a ''device binding'' functionality using a device fingerprint derived from multiple properties unique to the device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.9', 'Obfuscating transformations and functional defenses are interdependent and wellintegrated throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.8', 'A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.6', 'The app detects, and responds to, modifications of process memory, such as relocation table patches and injected code.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.3', 'The app detects, and responds to, tampering with executable files and critical data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.13', 'If the architecture requires sensitive computations be performed on the clientside, these computations are isolated from the operating system by using a hardwarebased SE / TEE. Alternatively, the information is protected using obfuscation. Considering current published research, the obfuscation type and parameters are sufficient to cause significant manual effort for reverse engineers seeking to comprehend the sensitive portions of the code and/or data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.2', 'The app implements multiple functionally independent debugging defenses that, in context of the overall protection scheme, force adversaries to invest considerable manual effort to enable debugging. All available debugging protocols must be covered (e.g. JDWP and native).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.8', 'All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.7', 'Sessions are terminated at the remote endpoint after a predefined period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.12', 'If the architecture requires sensitive information be stored on the device, the app only runs on operating system versions and devices that offer hardwarebacked key storage. Alternatively, the information is protected using obfuscation. Considering current published research, the obfuscation type and parameters are sufficient to cause significant manual effort for reverse engineers seeking to comprehend or extract the sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.12', 'The app educates the user about the types of personally identifiable information processed, as well as security best practices the user should follow in using the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.10', 'All components that are not part of the application but that the application relies on to operate, are clearly identified and the security implications of using those components are known.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.7', 'A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.1', 'All app components are identified and known to be needed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.13', 'Security is addressed within all parts of the software development lifecycle.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.8', 'No sensitive data is included in backups generated by the mobile operating system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.9', 'All security controls have a centralized implementation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.11', 'The app enforces a minimum deviceaccesssecurity policy, such as requiring the user to set a device passcode.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.5', 'The app doesn''t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrolments and account recovery.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.10', 'The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.8', 'All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.9', 'The app removes sensitive data from views when backgrounded.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.12', 'Remote endpoints verify that connecting clients use an uptodate version of the mobile app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.11', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 80057.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- PCIDSS ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.0', 'Protect stored cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.5', 'Physically secure all media. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.1', 'Use strong cryptography and security protocols to safeguard sensitive cardholder data during transmission over open, public networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.2', 'Secure cryptographic key distribution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.7', 'Ensure that security policies and operational procedures for developing and maintaining secure systems and applications are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.5', 'Assign to an individual or team the information security management responsibilities: Monitor and control all access to data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.4', 'Configure system security parameters to prevent misuse. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5', 'Documented change controls procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.4', 'Document and communicate authentication policies and procedures to all users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.3', 'Install perimeter firewalls between all wireless networks and the cardholder data environment, and configure these firewalls to deny or, if traffic is necessary for business purposes, permit only authorized traffic between the wireless environment and the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.3', 'Record the audit trail entry date and time for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.2', 'Maintain a written agreement that includes an acknowledgement that the service providers are responsible for the security of cardholder data the service providers possess or otherwise store, process or transmit on behalf of the customer, or to the extent that they could impact the security of the customers cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.5', 'Deploy a changedetection mechanism (for example, fileintegrity monitoring tools) to alert personnel to unauthorized modification (including changes, additions, and deletions) of critical system files, configuration files, or content files; and configure the software to perform critical file comparisons at least weekly. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.1.1', 'For wireless environments connected to the cardholder data environment or transmitting cardholder data, change ALL wireless vendor defaults at installation, including but not limited to default wireless encryption keys, passwords, and SNMP community strings. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.6', 'Upon completion of a significant change, all relevant PCI DSS requirements must be implemented on all new or changed systems and networks, and documentation updated as applicable. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.4', 'Remove/disable inactive user accounts within 90 days. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.2', 'Restrict access to cryptographic keys to the fewest number of custodians necessary. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.1', 'Review security events at least daily.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2', 'Implement automated audit trails for all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.7', 'Implemented mitigation for crosssite scripting (XSS).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.3', 'Designate specific personnel to be available on a 24/7 basis to respond to alerts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.2', 'Develop procedures to easily distinguish between onsite personnel and visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.3', 'Perform internal and external scans, and rescans as needed, after any significant change. Scans must be performed by qualified personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.2', 'Ensure that all system components and software are protected from known vulnerabilities by installing applicable vendorsupplied security patches. Install critical security patches within one month of release. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.1', 'Do not store the full contents of any track (from the magnetic stripe located on the back of a card, equivalent data contained on a chip, or elsewhere) after authorization. This data is alternatively called full track, track, track 1, track 2, and magneticstripe data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.6', 'Documentation of business justification and approval for use of all services, protocols, and ports allowed, including documentation of security features implemented for those protocols considered to be insecure.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1', 'Define and implement policies and procedures to ensure proper user identification management for nonconsumer users and administrators on all system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.0', 'Install and maintain a firewall configuration to protect cardholder data', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.4', 'Ensure that the security policy and procedures clearly define information security responsibilities for all personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.3', 'Passwords/passphrases are strong and not weak.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.1', 'Coverage of all system components ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.4.1', 'If disk encryption is used (rather than file or columnlevel database encryption), logical access must be managed separately and independently of native operating system authentication and access control mechanisms (for example, by not using local user account databases or general network login credentials). Decryption keys must not be associated with user accounts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.4', 'A method to accurately and readily determine owner, contact information, and purpose (for example, labeling, coding, and/or inventorying of devices).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.2', 'Review logs of all other system components periodically based on the organization?s policies and risk management strategy, as determined by the organization?s annual risk assessment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.2', 'Ensure that all antivirus mechanisms are maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2', 'Develop configuration standards for all system components. Assure that these standards address all known security vulnerabilities and are consistent with industryaccepted system hardening standards. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.4', 'If segmentation is used to isolate the CDE from other networks, perform penetration tests at least annually and after any changes to segmentation controls/methods to verify that the segmentation methods are operational and effective, and isolate all outofscope systems from systems in the CDE. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.5', 'Create audit logs for all use of and changes to identification and authentication mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3.2', 'Review custom code prior to release to production or customers in order to identify any potential coding vulnerability (using either manual or automated processes).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5', 'Secure audit trails so they cannot be altered. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.4.1', 'Additional requirement for service providers only: Executive management shall establish responsibility for the protection of cardholder data and a PCI DSS compliance program.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.2', 'Verify user identity before modifying any authentication credential for example, performing password resets, provisioning new tokens, or generating new keys. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.3', 'Current diagram that shows all cardholder data flows across systems and networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.3', 'Immediately revoke access for any terminated users. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.6', 'All high risk vulnerabilities identified in the vulnerability identification process (as defined in PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.5', 'Include alerts from security monitoring systems, including but not limited to intrusiondetection, intrusionprevention, firewalls, and fileintegrity monitoring systems. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10', 'Implement an incident response plan. Be prepared to respond immediately to a system breach. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.1', 'Visitors are authorized before entering, and escorted at all times within, areas where cardholder data is processed or maintained. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.5', 'Permit only established connections into the network. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.6', 'Record the audit trail entry identity or name of affected data, system component, or resource for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3', 'Secure all individual nonconsole administrative access and all remote access to the CDE using multifactor authentication. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.2', 'Secure and synchronize router configuration files. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.2', 'Separation of duties between development/test and production environments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.0', 'Regularly test security systems and processes. ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.4', 'Assign to an individual or team the information security management responsibilities: Administer user accounts, including additions, deletions, and modifications. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.4', 'Maintain an inventory of system components that are in scope for PCI DSS. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.1', 'Generation of strong cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.0', 'Maintain a policy that addresses information security for all personnel. ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.2', 'Implement a riskassessment process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.1.1', 'Ensure wireless networks transmitting cardholder data or connected to the cardholder data environment, use industry best practices to implement strong encryption for authentication and transmission. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.9', 'Ensure that security policies and operational procedures for monitoring all access to network resources and cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.5.1', 'Store media backups in a secure location, preferably an offsite facility, such as an alternate or backup site, or a commercial storage facility. Review the location''s security at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8.2', 'Render cardholder data on electronic media unrecoverable so that cardholder data cannot be reconstructed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.3', 'Visitors are asked to surrender the badge or identification before leaving the facility or at the date of expiration. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1.1', 'Maintain an inventory of authorized wireless access points including a documented business justification. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.2', 'Periodically inspect device surfaces to detect tampering (for example, addition of card skimmers to devices), or substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.4', 'Cryptographic key changes for keys that have reached the end of their cryptoperiod (for example, after a defined period of time has passed and/or after a certain amount of ciphertext has been produced by a given key), as defined by the associated application vendor or key owner, and based on industry best practices and guidelines (for example, NIST Special Publication 80057). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.10', 'Implemented mitigation for broken authentication and session management. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.5.1', 'Implement a process to respond to any alerts generated by the changedetection solution. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.2', 'Time data is protected. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.7', 'Ensure that security policies and operational procedures for protecting stored cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.2', 'Documented change approval by authorized parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.7', 'Maintain strict control over the storage and accessibility of media. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6.1', 'Educate personnel upon hire and at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.2', 'Enable only necessary services, protocols, daemons, etc., as required for the function of the system. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1.1', 'Ensure that antivirus programs are capable of detecting, removing, and protecting against all known types of malicious software. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.1', 'Record the audit trail entry user identification for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.5.1', 'Additional requirement for service providers only: Service providers with remote access to customer premises (for example, for support of POS systems or servers) must use a unique authentication credential (such as a password/phrase) for each customer. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.2', 'Authentication for use of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.4', 'Require documented approval by authorized parties specifying required privileges. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.1', 'Implement a DMZ to limit inbound traffic to only system components that provide authorized publicly accessible services, protocols, and ports. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.1', 'Implemented mitigation for injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.4', 'Maintain a program to monitor service providers? PCI DSS compliance status at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.5', 'Use fileintegrity monitoring or changedetection software on logs to ensure that existing log data cannot be changed without generating alerts (although new data being added should not cause an alert). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.6', 'Limit repeated access attempts by locking out the user ID after not more than six attempts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1', 'Establish and implement firewall and router configuration standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.2', 'Implement physical and/or logical controls to restrict access to publicly accessible network jacks. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.1', 'Perform external penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.2', 'Create audit logs for all actions taken by any individual with root or administrative privileges ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.3', 'Do not store the personal identification number (PIN) or the encrypted PIN block after authorization. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.3', 'Ensure that security policies and operational procedures for restricting access to cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.9', 'Activation of remoteaccess technologies for vendors and business partners only when needed by vendors and business partners, with immediate deactivation after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.4', 'Ensure that security policies and operational procedures for protecting systems against malware are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.3', 'Default denyall setting. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.3', 'Mask PAN when displayed (the first six and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the first six/last four digits of the PAN. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.6', 'Acceptable network locations for the technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.3', 'Create audit logs for all access to all audit trails.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.2', 'Perform internal penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.1', 'Use either video cameras or access control mechanisms (or both) to monitor individual physical access to sensitive areas. Review collected data and correlate with other entries. Store for at least three months, unless otherwise restricted by law. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2', 'In addition to assigning a unique ID, ensure proper userauthentication management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.0', 'Protect all systems against malware and regularly update antivirus software or programs ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.1', 'A formal process for approving and testing all network connections and changes to the firewall and router configurations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.2', 'Protect audit trail files from unauthorized modifications. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.5', 'Maintain information about which PCI DSS requirements are managed by each service provider, and which are managed by the entity. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.7', 'Do not disclose private IP addresses and routing information to unauthorized parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.4', 'Implemented mitigation for insecure communications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.11', 'Additional requirement for service providers only: Perform reviews at least quarterly to confirm personnel are following security policies and operational procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.0', 'Restrict physical access to cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.5', 'Do not allow an individual to submit a new password/passphrase that is the same as any of the last four passwords/passphrases he or she has used. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2', 'Build firewall and router configurations that restrict connections between untrusted networks and any system components in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.7', 'Prevention of unauthorized substitution of cryptographic keys. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.1', 'Critical systems have the correct and consistent time. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.0', 'Develop and maintain secure systems and applications ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.1', 'Perform quarterly internal vulnerability scans. Address vulnerabilities and perform rescans to verify all high risk vulnerabilities are resolved in accordance with the entity''s vulnerability ranking (per Requirement 6.1). Scans must be performed by qualified personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.2', 'Assign to an individual or team the information security management responsibilities: Monitor and analyze security alerts and information, and distribute to appropriate personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.6', 'Shared hosting providers must protect each entity?s hosted environment and cardholder data. These providers must meet specific requirements as detailed in Appendix A1: Additional PCI DSS Requirements for Shared Hosting Providers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4', 'Follow change control processes and procedures for all changes to system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.3', 'Ensure that security policies and operational procedures for encrypting transmissions of cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.1', 'Define access needs for each role.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.4', 'Do not allow unauthorized outbound traffic from the cardholder data environment to the Internet. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.4', 'Store cryptographic keys in the fewest possible locations. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.6', 'Where other authentication mechanisms are used (for example, physical or logical security tokens, smart cards, certificates, etc.), use of these mechanisms must be assigned.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.1', 'Explicit approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8', 'Destroy media when it is no longer needed for business or legal reasons.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.3', 'Functionality testing to verify that the change does not adversely impact the security of the system. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.8', 'Additional requirement for service providers only: Implement a process for the timely detection and reporting of failures of critical security control systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.1', 'Classify media so the sensitivity of the data can be determined. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8', 'Maintain and implement policies and procedures to manage service providers with whom cardholder data is shared, or that could affect the security of cardholder data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.7', 'All access to any database containing cardholder data (including access by applications, administrators, and all other users) is restricted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3', 'Develop usage policies for critical technologies and define proper use of these technologies. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.2', 'Restrict access to privileged user IDs to least privileges necessary to perform job responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.3', 'Implement antispoofing measures to detect and block forged source IP addresses from entering the network. (For example, block traffic originating from the Internet with an internal source address.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.3', 'Store secret and private keys used to encrypt/decrypt cardholder data in one (or more) of the following forms at all times.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.4', 'Backout procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.7.1', 'Properly maintain inventory logs of all media and conduct media inventories at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.7', 'Retain audit trail history for at least one year, with a minimum of three months immediately available for analysis (for example, online, archived, or restorable from backup). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.2', 'Send the media by secured courier or other delivery method that can be accurately tracked. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.7', 'Screen potential personnel prior to hire to minimize the risk of attacks from internal sources. (Examples of background checks include previous employment history, criminal record, credit history, and reference checks.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.7', 'Requirement to review firewall and router rule sets at least every six months.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.6', 'If manual cleartext cryptographic keymanagement operations are used, these operations must be managed using split knowledge and dual control. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.6', 'Set passwords/passphrases for firsttime use and upon reset to a unique value for each user, and change immediately after the first use. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4', 'Using timesynchronization technology, synchronize all critical system clocks and times and ensure that the following is implemented for acquiring, distributing, and storing time. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.5', 'Ensure that security policies and operational procedures for managing vendor defaults and other security parameters are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2', 'Run internal and external network vulnerability scans at least quarterly and after any significant change in the network (such as new system component installations, changes in network topology, firewall rule modifications, product upgrades). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.1', 'Assign to an individual or team the following information security management responsibilities: * Establish, document, and distribute security policies and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.10', 'Ensure that security policies and operational procedures for restricting physical access to cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.1', 'Separate development/test environments from production environments, and enforce the separation with access controls. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.2', 'Current network diagram that identifies all connections between the cardholder data environment and other networks, including any wireless networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.8', 'If a session has been idle for more than 15 minutes, require the user to reauthenticate to reactivate the terminal or session. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.3', 'Promptly back up audit trail files to a centralized log server or media that is difficult to alter. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.4', 'Install personal firewall software or equivalent functionality on any portable computing devices (including company and/or employeeowned) that connect to the Internet when outside the network (for example, laptops used by employees), and which are also used to access the CDE. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.9', 'Additional requirement for service providers only: Service providers acknowledge in writing to customers that they are responsible for the security of cardholder data the service provider possesses.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.6', 'Develop a process to modify and evolve the incident response plan according to lessons learned and to incorporate industry developments. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.3', 'Implemented mitigation for insecure cryptographic storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.3', 'Ensure that antivirus mechanisms are actively running and cannot be disabled or altered by users, unless specifically authorized by management on a casebycase basis for a limited time period. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.7', 'List of companyapproved products.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.2', 'Assignment of privileges to individuals based on job classification and function. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.4', 'Render PAN unreadable anywhere it is stored (including on portable digital media, backup media, and in logs)', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.4', 'Create audit logs for all invalid logical access attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.3', 'Exploitable vulnerabilities found during penetration testing are corrected and testing is repeated to verify the corrections. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1', 'Use appropriate facility entry controls to limit and monitor physical access to systems in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.3', 'Restrict physical access to wireless access points, gateways, handheld devices, networking/communications hardware, and telecommunication lines. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3', 'Implement a methodology for penetration testing.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.1', 'Create audit logs for all individual user accesses to cardholder data ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.8', 'Automatic disconnect of sessions for remoteaccess technologies after a specific period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.2', 'Do not store the card verification code or value (threedigit or fourdigit number printed on the front or back of a payment card used to verify cardnotpresent transactions) after authorization. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.1', 'Establish a process to identify security vulnerabilities, using reputable outside sources for security vulnerability information, and assign a risk ranking (for example, as high, medium or low) to newly discovered security vulnerabilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.2', 'Implemented mitigation for buffer overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.5', 'Ensure that security policies and operational procedures for managing firewalls are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.3', 'Ensure there is an established process for engaging service providers including proper due diligence prior to engagement. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.4', 'Write logs for externalfacing technologies onto a secure, centralized, internal log server or media device. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.0', 'Do not use vendorsupplied defaults for system passwords and other security parameters ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.7', 'Set the lockout duration to a minimum of 30 minutes or until an administrator enables the user ID. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.1', 'Documentation of impact. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.3', 'Implement additional security features for any required services, protocols, or daemons that are considered to be insecure.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.3', 'Ensure management approves any and all media that is moved from a secured area (including when media is distributed to individuals). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6.2', 'Require personnel to acknowledge at least annually that they have read and understood the security policy and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.2', 'Record the audit trail entry type of event for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1', 'Deploy antivirus software on all systems commonly affected by malicious software (particularly personal computers and servers). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.3', 'Assign access based on individual personnel''s job classification and function. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.2', 'Limit inbound Internet traffic to IP addresses within the DMZ. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.5', 'Do not use group, shared, or generic IDs, passwords, or other authentication methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.3', 'A list of all such devices and personnel with access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.2', 'Visitors are identified and given a badge or other identification that expires and that visibly distinguishes the visitors from onsite personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1.2', 'Implement incident response procedures in the event unauthorized wireless access points are detected. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.1', 'Keep cardholder data storage to a minimum by implementing data retention and disposal policies, procedures and processes that include at least the following for all cardholder data (CHD) storage: . Limiting data storage amount and retention time to that which is required for legal, regulatory, and/or business requirements . Specific retention requirements for cardholder data . Processes for secure deletion of data when no longer needed . A quarterly process for identifying and securely deleting stored cardholder data that exceeds defined retention. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.3', 'Provide training for personnel to be aware of attempted tampering or replacement of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.6', 'Ensure that security policies and operational procedures for security monitoring and testing are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.5', 'Retirement or replacement (for example, archiving, destruction, and/or revocation) of keys as deemed necessary when the integrity of the key has been weakened (for example, departure of an employee with knowledge of a cleartext key component), or keys are suspected of being compromised. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.9', 'Implemented mitigation for crosssite request forgery (CSRF).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.8', 'Requirement for cryptographic key custodians to formally acknowledge that they understand and accept their keycustodian responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.3', 'Time settings are received from industryaccepted time sources. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.1.1', 'Review the security policy at least annually and update the policy when the environment changes. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1', 'Limit access to system components and cardholder data to only those individuals whose job requires such access. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6', 'Fully document and implement all keymanagement processes and procedures for cryptographic keys used for encryption of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.2', 'Never send unprotected PANs by enduser messaging technologies (for example, email, instant messaging, SMS, chat, etc.). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.8.1', 'Additional requirement for service providers only: Respond to failures of any critical security controls in a timely manner. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6', 'Maintain strict control over the internal or external distribution of any kind of media, including the following: ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8.1', 'Shred, incinerate, or pulp hardcopy materials so that cardholder data cannot be reconstructed. Secure storage containers used for materials that are to be destroyed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.5', 'Record the audit trail entry origination of event for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.1', 'Restrict inbound and outbound traffic to that which is necessary for the cardholder data environment, and specifically deny all other traffic. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3.1', 'Incorporate multifactor authentication for all nonconsole access into the CDE for personnel with administrative access. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.3', 'Production data (live PANs) are not used for testing or development. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.3', 'Encrypt all nonconsole administrative access using strong cryptography. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.3', 'Assign to an individual or team the information security management responsibilities: Establish, document, and distribute security incident response and escalation procedures to ensure timely and effective handling of all situations. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.1', 'Limit viewing of audit trails to those with a jobrelated need. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.0', 'Identify and authenticate access to system components ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3.1', 'Remove development, test and/or custom application accounts, user IDs, and passwords before applications become active or are released to customers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.4', 'Requirements for a firewall at each Internet connection and between any demilitarized zone (DMZ) and the internal network zone.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.2', 'Control addition, deletion, and modification of user IDs, credentials, and other identifier objects. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.1', 'Using strong cryptography, render all authentication credentials (such as passwords/phrases) unreadable during transmission and storage on all system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.4', 'Provide appropriate training to staff with security breach response responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.5', 'Implemented mitigation for improper error handling.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.6', 'Place system components that store cardholder data (such as a database) in an internal network zone, segregated from the DMZ and other untrusted networks. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.1', 'Create the incident response plan to be implemented in the event of system breach. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4', 'Implement procedures to identify and authorize visitors. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.5', 'Acceptable uses of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2', 'Establish an access control system(s) for systems components that restricts access based on a user''s need to know, and is set to deny all unless specifically allowed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5', 'Document and implement procedures to protect keys used to secure stored cardholder data against disclosure and misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1.2', 'For systems considered to be not commonly affected by malicious software, perform periodic evaluations to identify and evaluate evolving malware threats in order to confirm whether such systems continue to not require antivirus software. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.3', 'Follow up exceptions and anomalies identified during the review process. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.4.1', 'Additional requirement for service providers only: If segmentation is used, confirm PCI DSS scope by performing penetration testing on segmentation controls at least every six months and after any changes to segmentation controls/methods. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.8', 'Ensure that security policies and operational procedures for identification and authentication are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.1', 'Implement only one primary function per server to prevent functions that require different security levels from coexisting on the same server. (For example, web servers, database servers, and DNS should be implemented on separate servers.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.6', 'Create audit logs for all initialization, stopping, or pausing of the audit logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.8', 'Implemented mitigation for improper access control (such as insecure direct object references, failure to restrict URL access, directory traversal, and failure to restrict user access to functions). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.1', 'Implement audit trails to link all access to system components to each individual user. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.2', 'Review and test the plan, including all elements listed in Requirement 12.10.1, at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.3', 'Control physical access for onsite personnel to sensitive areas.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.2', 'Perform quarterly external vulnerability scans, via an Approved Scanning Vendor (ASV) approved by the Payment Card Industry Security Standards Council (PCI SSC). Perform rescans as needed, until passing scans are achieved. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3', 'Develop internal and external software applications (including webbased administrative access to applications) securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.10', 'For personnel accessing cardholder data via remoteaccess technologies, prohibit the copying, moving, and storage of cardholder data onto local hard drives and removable electronic media, unless explicitly authorized for a defined business need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.4', 'Change user passwords/passphrases at least once every 90 days.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2', 'Do not store sensitive authentication data after authorization (even if encrypted). If sensitive authentication data is received, render all data unrecoverable upon completion of the authorization process. It is permissible for issuers and companies that support issuing services to store sensitive authentication data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.5', 'Description of groups, roles, and responsibilities for management of network components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.1', 'Assign all users a unique ID before allowing them to access system components or cardholder data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.1', 'Always change vendorsupplied defaults and remove or disable unnecessary default accounts before installing a system on the network. This applies to ALL default passwords, including but not limited to those used by operating systems, software that provides security services, application and system accounts, pointofsale (POS) terminals, payment applications, Simple Network Management Protocol (SNMP) community strings, etc.). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.1', 'Maintain a list of service providers including a description of the service provided. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.4', 'Use intrusiondetection and/or intrusionprevention techniques to detect and/or prevent intrusions into the network. Monitor all traffic at the perimeter of the cardholder data environment as well as at critical points in the cardholder data environment, and alert personnel to suspected compromises. Keep all intrusiondetection and prevention engines, baselines, and signatures up to date. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.7', 'Create audit logs for all creation and deletion of systemlevel objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5', 'Address common coding vulnerabilities in softwaredevelopment processes as follows: * Train developers at least annually in uptodate secure coding techniques, including how to avoid common coding vulnerabilities. * Develop applications based on secure coding guidelines. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.1', 'Additional requirement for service providers only: Maintain a documented description of the cryptographic architecture', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.5', 'Manage IDs used by third parties to access, support, or maintain system components via remote access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.0', 'Track and monitor all access to network resources and cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6', 'Review logs and security events for all system components to identify anomalies or suspicious activity. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.5', 'Remove all unnecessary functionality, such as scripts, drivers, features, subsystems, file systems, and unnecessary web servers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6', 'Implement a formal security awareness program to make all personnel aware of the cardholder data security policy and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.4', 'Removal of test data and accounts from system components before the system becomes active / goes into production. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3', 'Prohibit direct public access between the Internet and any system component in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3.2', 'Incorporate multifactor authentication for all remote network access (both user and administrator, and including thirdparty access for support or maintenance) originating from outside the entity''s network. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.4', 'Record the audit trail entry success or failure indication for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.1', 'Maintain an uptodate list of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.4', 'A visitor log is used to maintain a physical audit trail of visitor activity to the facility as well as computer rooms and data centers where cardholder data is stored or transmitted. Document the visitors name, the firm represented, and the onsite personnel authorizing physical access on the log. Retain this log for a minimum of three months, unless otherwise restricted by law. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1', 'Implement processes to test for the presence of wireless access points (802.11), and detect and identify all authorized and unauthorized wireless access points on a quarterly basis. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.0', 'Encrypt transmission of cardholder data across open, public networks ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.1', 'Establish, publish, maintain, and disseminate a security policy. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.3', 'Secure cryptographic key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.6', 'For publicfacing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.0', 'Restrict access to cardholder data by business need to know ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9', 'Protect devices that capture payment card data via direct physical interaction with the card from tampering and substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.0', 'Protect stored cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.5', 'Physically secure all media. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.1', 'Use strong cryptography and security protocols to safeguard sensitive cardholder data during transmission over open, public networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.2', 'Secure cryptographic key distribution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.7', 'Ensure that security policies and operational procedures for developing and maintaining secure systems and applications are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.5', 'Assign to an individual or team the information security management responsibilities: Monitor and control all access to data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.4', 'Configure system security parameters to prevent misuse. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5', 'Documented change controls procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.4', 'Document and communicate authentication policies and procedures to all users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.3', 'Install perimeter firewalls between all wireless networks and the cardholder data environment, and configure these firewalls to deny or, if traffic is necessary for business purposes, permit only authorized traffic between the wireless environment and the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.3', 'Record the audit trail entry date and time for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.2', 'Maintain a written agreement that includes an acknowledgement that the service providers are responsible for the security of cardholder data the service providers possess or otherwise store, process or transmit on behalf of the customer, or to the extent that they could impact the security of the customers cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.5', 'Deploy a changedetection mechanism (for example, fileintegrity monitoring tools) to alert personnel to unauthorized modification (including changes, additions, and deletions) of critical system files, configuration files, or content files; and configure the software to perform critical file comparisons at least weekly. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.1.1', 'For wireless environments connected to the cardholder data environment or transmitting cardholder data, change ALL wireless vendor defaults at installation, including but not limited to default wireless encryption keys, passwords, and SNMP community strings. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.6', 'Upon completion of a significant change, all relevant PCI DSS requirements must be implemented on all new or changed systems and networks, and documentation updated as applicable. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.4', 'Remove/disable inactive user accounts within 90 days. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.2', 'Restrict access to cryptographic keys to the fewest number of custodians necessary. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.1', 'Review security events at least daily.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2', 'Implement automated audit trails for all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.7', 'Implemented mitigation for crosssite scripting (XSS).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.3', 'Designate specific personnel to be available on a 24/7 basis to respond to alerts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.2', 'Develop procedures to easily distinguish between onsite personnel and visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.3', 'Perform internal and external scans, and rescans as needed, after any significant change. Scans must be performed by qualified personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.2', 'Ensure that all system components and software are protected from known vulnerabilities by installing applicable vendorsupplied security patches. Install critical security patches within one month of release. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.1', 'Do not store the full contents of any track (from the magnetic stripe located on the back of a card, equivalent data contained on a chip, or elsewhere) after authorization. This data is alternatively called full track, track, track 1, track 2, and magneticstripe data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.6', 'Documentation of business justification and approval for use of all services, protocols, and ports allowed, including documentation of security features implemented for those protocols considered to be insecure.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1', 'Define and implement policies and procedures to ensure proper user identification management for nonconsumer users and administrators on all system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.0', 'Install and maintain a firewall configuration to protect cardholder data', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.4', 'Ensure that the security policy and procedures clearly define information security responsibilities for all personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.3', 'Passwords/passphrases are strong and not weak.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.1', 'Coverage of all system components ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.4.1', 'If disk encryption is used (rather than file or columnlevel database encryption), logical access must be managed separately and independently of native operating system authentication and access control mechanisms (for example, by not using local user account databases or general network login credentials). Decryption keys must not be associated with user accounts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.4', 'A method to accurately and readily determine owner, contact information, and purpose (for example, labeling, coding, and/or inventorying of devices).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.2', 'Review logs of all other system components periodically based on the organization?s policies and risk management strategy, as determined by the organization?s annual risk assessment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.2', 'Ensure that all antivirus mechanisms are maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2', 'Develop configuration standards for all system components. Assure that these standards address all known security vulnerabilities and are consistent with industryaccepted system hardening standards. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.4', 'If segmentation is used to isolate the CDE from other networks, perform penetration tests at least annually and after any changes to segmentation controls/methods to verify that the segmentation methods are operational and effective, and isolate all outofscope systems from systems in the CDE. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.5', 'Create audit logs for all use of and changes to identification and authentication mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3.2', 'Review custom code prior to release to production or customers in order to identify any potential coding vulnerability (using either manual or automated processes).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5', 'Secure audit trails so they cannot be altered. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.4.1', 'Additional requirement for service providers only: Executive management shall establish responsibility for the protection of cardholder data and a PCI DSS compliance program.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.2', 'Verify user identity before modifying any authentication credential for example, performing password resets, provisioning new tokens, or generating new keys. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.3', 'Current diagram that shows all cardholder data flows across systems and networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.3', 'Immediately revoke access for any terminated users. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.6', 'All high risk vulnerabilities identified in the vulnerability identification process (as defined in PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.5', 'Include alerts from security monitoring systems, including but not limited to intrusiondetection, intrusionprevention, firewalls, and fileintegrity monitoring systems. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10', 'Implement an incident response plan. Be prepared to respond immediately to a system breach. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.1', 'Visitors are authorized before entering, and escorted at all times within, areas where cardholder data is processed or maintained. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.5', 'Permit only established connections into the network. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.6', 'Record the audit trail entry identity or name of affected data, system component, or resource for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3', 'Secure all individual nonconsole administrative access and all remote access to the CDE using multifactor authentication. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.2', 'Secure and synchronize router configuration files. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.2', 'Separation of duties between development/test and production environments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.0', 'Regularly test security systems and processes. ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.4', 'Assign to an individual or team the information security management responsibilities: Administer user accounts, including additions, deletions, and modifications. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.4', 'Maintain an inventory of system components that are in scope for PCI DSS. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.1', 'Generation of strong cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.0', 'Maintain a policy that addresses information security for all personnel. ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.2', 'Implement a riskassessment process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.1.1', 'Ensure wireless networks transmitting cardholder data or connected to the cardholder data environment, use industry best practices to implement strong encryption for authentication and transmission. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.9', 'Ensure that security policies and operational procedures for monitoring all access to network resources and cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.5.1', 'Store media backups in a secure location, preferably an offsite facility, such as an alternate or backup site, or a commercial storage facility. Review the location''s security at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8.2', 'Render cardholder data on electronic media unrecoverable so that cardholder data cannot be reconstructed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.3', 'Visitors are asked to surrender the badge or identification before leaving the facility or at the date of expiration. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1.1', 'Maintain an inventory of authorized wireless access points including a documented business justification. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.2', 'Periodically inspect device surfaces to detect tampering (for example, addition of card skimmers to devices), or substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.4', 'Cryptographic key changes for keys that have reached the end of their cryptoperiod (for example, after a defined period of time has passed and/or after a certain amount of ciphertext has been produced by a given key), as defined by the associated application vendor or key owner, and based on industry best practices and guidelines (for example, NIST Special Publication 80057). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.10', 'Implemented mitigation for broken authentication and session management. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.5.1', 'Implement a process to respond to any alerts generated by the changedetection solution. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.2', 'Time data is protected. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.7', 'Ensure that security policies and operational procedures for protecting stored cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.2', 'Documented change approval by authorized parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.7', 'Maintain strict control over the storage and accessibility of media. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6.1', 'Educate personnel upon hire and at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.2', 'Enable only necessary services, protocols, daemons, etc., as required for the function of the system. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1.1', 'Ensure that antivirus programs are capable of detecting, removing, and protecting against all known types of malicious software. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.1', 'Record the audit trail entry user identification for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.5.1', 'Additional requirement for service providers only: Service providers with remote access to customer premises (for example, for support of POS systems or servers) must use a unique authentication credential (such as a password/phrase) for each customer. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.2', 'Authentication for use of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.4', 'Require documented approval by authorized parties specifying required privileges. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.1', 'Implement a DMZ to limit inbound traffic to only system components that provide authorized publicly accessible services, protocols, and ports. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.1', 'Implemented mitigation for injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.4', 'Maintain a program to monitor service providers? PCI DSS compliance status at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.5', 'Use fileintegrity monitoring or changedetection software on logs to ensure that existing log data cannot be changed without generating alerts (although new data being added should not cause an alert). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.6', 'Limit repeated access attempts by locking out the user ID after not more than six attempts. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1', 'Establish and implement firewall and router configuration standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.2', 'Implement physical and/or logical controls to restrict access to publicly accessible network jacks. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.1', 'Perform external penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.2', 'Create audit logs for all actions taken by any individual with root or administrative privileges ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.3', 'Do not store the personal identification number (PIN) or the encrypted PIN block after authorization. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.3', 'Ensure that security policies and operational procedures for restricting access to cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.9', 'Activation of remoteaccess technologies for vendors and business partners only when needed by vendors and business partners, with immediate deactivation after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.4', 'Ensure that security policies and operational procedures for protecting systems against malware are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.3', 'Default denyall setting. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.3', 'Mask PAN when displayed (the first six and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the first six/last four digits of the PAN. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.6', 'Acceptable network locations for the technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.3', 'Create audit logs for all access to all audit trails.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.2', 'Perform internal penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.1', 'Use either video cameras or access control mechanisms (or both) to monitor individual physical access to sensitive areas. Review collected data and correlate with other entries. Store for at least three months, unless otherwise restricted by law. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2', 'In addition to assigning a unique ID, ensure proper userauthentication management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.0', 'Protect all systems against malware and regularly update antivirus software or programs ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.1', 'A formal process for approving and testing all network connections and changes to the firewall and router configurations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.2', 'Protect audit trail files from unauthorized modifications. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.5', 'Maintain information about which PCI DSS requirements are managed by each service provider, and which are managed by the entity. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.7', 'Do not disclose private IP addresses and routing information to unauthorized parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.4', 'Implemented mitigation for insecure communications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.11', 'Additional requirement for service providers only: Perform reviews at least quarterly to confirm personnel are following security policies and operational procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.0', 'Restrict physical access to cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.5', 'Do not allow an individual to submit a new password/passphrase that is the same as any of the last four passwords/passphrases he or she has used. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2', 'Build firewall and router configurations that restrict connections between untrusted networks and any system components in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.7', 'Prevention of unauthorized substitution of cryptographic keys. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.1', 'Critical systems have the correct and consistent time. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.0', 'Develop and maintain secure systems and applications ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.1', 'Perform quarterly internal vulnerability scans. Address vulnerabilities and perform rescans to verify all high risk vulnerabilities are resolved in accordance with the entity''s vulnerability ranking (per Requirement 6.1). Scans must be performed by qualified personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.2', 'Assign to an individual or team the information security management responsibilities: Monitor and analyze security alerts and information, and distribute to appropriate personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.6', 'Shared hosting providers must protect each entity?s hosted environment and cardholder data. These providers must meet specific requirements as detailed in Appendix A1: Additional PCI DSS Requirements for Shared Hosting Providers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4', 'Follow change control processes and procedures for all changes to system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.3', 'Ensure that security policies and operational procedures for encrypting transmissions of cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.1', 'Define access needs for each role.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.4', 'Do not allow unauthorized outbound traffic from the cardholder data environment to the Internet. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.4', 'Store cryptographic keys in the fewest possible locations. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.6', 'Where other authentication mechanisms are used (for example, physical or logical security tokens, smart cards, certificates, etc.), use of these mechanisms must be assigned.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.1', 'Explicit approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8', 'Destroy media when it is no longer needed for business or legal reasons.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.3', 'Functionality testing to verify that the change does not adversely impact the security of the system. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.8', 'Additional requirement for service providers only: Implement a process for the timely detection and reporting of failures of critical security control systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.1', 'Classify media so the sensitivity of the data can be determined. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8', 'Maintain and implement policies and procedures to manage service providers with whom cardholder data is shared, or that could affect the security of cardholder data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.7', 'All access to any database containing cardholder data (including access by applications, administrators, and all other users) is restricted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3', 'Develop usage policies for critical technologies and define proper use of these technologies. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.2', 'Restrict access to privileged user IDs to least privileges necessary to perform job responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.3', 'Implement antispoofing measures to detect and block forged source IP addresses from entering the network. (For example, block traffic originating from the Internet with an internal source address.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.3', 'Store secret and private keys used to encrypt/decrypt cardholder data in one (or more) of the following forms at all times.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.4', 'Backout procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.7.1', 'Properly maintain inventory logs of all media and conduct media inventories at least annually. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.7', 'Retain audit trail history for at least one year, with a minimum of three months immediately available for analysis (for example, online, archived, or restorable from backup). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.2', 'Send the media by secured courier or other delivery method that can be accurately tracked. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.7', 'Screen potential personnel prior to hire to minimize the risk of attacks from internal sources. (Examples of background checks include previous employment history, criminal record, credit history, and reference checks.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.7', 'Requirement to review firewall and router rule sets at least every six months.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.6', 'If manual cleartext cryptographic keymanagement operations are used, these operations must be managed using split knowledge and dual control. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.6', 'Set passwords/passphrases for firsttime use and upon reset to a unique value for each user, and change immediately after the first use. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4', 'Using timesynchronization technology, synchronize all critical system clocks and times and ensure that the following is implemented for acquiring, distributing, and storing time. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.5', 'Ensure that security policies and operational procedures for managing vendor defaults and other security parameters are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2', 'Run internal and external network vulnerability scans at least quarterly and after any significant change in the network (such as new system component installations, changes in network topology, firewall rule modifications, product upgrades). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.1', 'Assign to an individual or team the following information security management responsibilities: * Establish, document, and distribute security policies and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.10', 'Ensure that security policies and operational procedures for restricting physical access to cardholder data are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.1', 'Separate development/test environments from production environments, and enforce the separation with access controls. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.2', 'Current network diagram that identifies all connections between the cardholder data environment and other networks, including any wireless networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.8', 'If a session has been idle for more than 15 minutes, require the user to reauthenticate to reactivate the terminal or session. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.3', 'Promptly back up audit trail files to a centralized log server or media that is difficult to alter. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.4', 'Install personal firewall software or equivalent functionality on any portable computing devices (including company and/or employeeowned) that connect to the Internet when outside the network (for example, laptops used by employees), and which are also used to access the CDE. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.9', 'Additional requirement for service providers only: Service providers acknowledge in writing to customers that they are responsible for the security of cardholder data the service provider possesses.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.6', 'Develop a process to modify and evolve the incident response plan according to lessons learned and to incorporate industry developments. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.3', 'Implemented mitigation for insecure cryptographic storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.3', 'Ensure that antivirus mechanisms are actively running and cannot be disabled or altered by users, unless specifically authorized by management on a casebycase basis for a limited time period. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.7', 'List of companyapproved products.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2.2', 'Assignment of privileges to individuals based on job classification and function. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.4', 'Render PAN unreadable anywhere it is stored (including on portable digital media, backup media, and in logs)', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.4', 'Create audit logs for all invalid logical access attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.3', 'Exploitable vulnerabilities found during penetration testing are corrected and testing is repeated to verify the corrections. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1', 'Use appropriate facility entry controls to limit and monitor physical access to systems in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.1.3', 'Restrict physical access to wireless access points, gateways, handheld devices, networking/communications hardware, and telecommunication lines. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3', 'Implement a methodology for penetration testing.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.1', 'Create audit logs for all individual user accesses to cardholder data ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.8', 'Automatic disconnect of sessions for remoteaccess technologies after a specific period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2.2', 'Do not store the card verification code or value (threedigit or fourdigit number printed on the front or back of a payment card used to verify cardnotpresent transactions) after authorization. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.1', 'Establish a process to identify security vulnerabilities, using reputable outside sources for security vulnerability information, and assign a risk ranking (for example, as high, medium or low) to newly discovered security vulnerabilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.2', 'Implemented mitigation for buffer overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.5', 'Ensure that security policies and operational procedures for managing firewalls are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.3', 'Ensure there is an established process for engaging service providers including proper due diligence prior to engagement. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.4', 'Write logs for externalfacing technologies onto a secure, centralized, internal log server or media device. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.0', 'Do not use vendorsupplied defaults for system passwords and other security parameters ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.7', 'Set the lockout duration to a minimum of 30 minutes or until an administrator enables the user ID. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.5.1', 'Documentation of impact. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.3', 'Implement additional security features for any required services, protocols, or daemons that are considered to be insecure.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6.3', 'Ensure management approves any and all media that is moved from a secured area (including when media is distributed to individuals). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6.2', 'Require personnel to acknowledge at least annually that they have read and understood the security policy and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.2', 'Record the audit trail entry type of event for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1', 'Deploy antivirus software on all systems commonly affected by malicious software (particularly personal computers and servers). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1.3', 'Assign access based on individual personnel''s job classification and function. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.2', 'Limit inbound Internet traffic to IP addresses within the DMZ. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.5', 'Do not use group, shared, or generic IDs, passwords, or other authentication methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.3', 'A list of all such devices and personnel with access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.2', 'Visitors are identified and given a badge or other identification that expires and that visibly distinguishes the visitors from onsite personnel. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1.2', 'Implement incident response procedures in the event unauthorized wireless access points are detected. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.1', 'Keep cardholder data storage to a minimum by implementing data retention and disposal policies, procedures and processes that include at least the following for all cardholder data (CHD) storage: . Limiting data storage amount and retention time to that which is required for legal, regulatory, and/or business requirements . Specific retention requirements for cardholder data . Processes for secure deletion of data when no longer needed . A quarterly process for identifying and securely deleting stored cardholder data that exceeds defined retention. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.3', 'Provide training for personnel to be aware of attempted tampering or replacement of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.6', 'Ensure that security policies and operational procedures for security monitoring and testing are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.5', 'Retirement or replacement (for example, archiving, destruction, and/or revocation) of keys as deemed necessary when the integrity of the key has been weakened (for example, departure of an employee with knowledge of a cleartext key component), or keys are suspected of being compromised. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.9', 'Implemented mitigation for crosssite request forgery (CSRF).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.8', 'Requirement for cryptographic key custodians to formally acknowledge that they understand and accept their keycustodian responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.4.3', 'Time settings are received from industryaccepted time sources. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.1.1', 'Review the security policy at least annually and update the policy when the environment changes. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.1', 'Limit access to system components and cardholder data to only those individuals whose job requires such access. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6', 'Fully document and implement all keymanagement processes and procedures for cryptographic keys used for encryption of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.2', 'Never send unprotected PANs by enduser messaging technologies (for example, email, instant messaging, SMS, chat, etc.). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.8.1', 'Additional requirement for service providers only: Respond to failures of any critical security controls in a timely manner. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.6', 'Maintain strict control over the internal or external distribution of any kind of media, including the following: ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.8.1', 'Shred, incinerate, or pulp hardcopy materials so that cardholder data cannot be reconstructed. Secure storage containers used for materials that are to be destroyed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.5', 'Record the audit trail entry origination of event for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.2.1', 'Restrict inbound and outbound traffic to that which is necessary for the cardholder data environment, and specifically deny all other traffic. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3.1', 'Incorporate multifactor authentication for all nonconsole access into the CDE for personnel with administrative access. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.3', 'Production data (live PANs) are not used for testing or development. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.3', 'Encrypt all nonconsole administrative access using strong cryptography. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.5.3', 'Assign to an individual or team the information security management responsibilities: Establish, document, and distribute security incident response and escalation procedures to ensure timely and effective handling of all situations. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.5.1', 'Limit viewing of audit trails to those with a jobrelated need. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.0', 'Identify and authenticate access to system components ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3.1', 'Remove development, test and/or custom application accounts, user IDs, and passwords before applications become active or are released to customers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.4', 'Requirements for a firewall at each Internet connection and between any demilitarized zone (DMZ) and the internal network zone.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.2', 'Control addition, deletion, and modification of user IDs, credentials, and other identifier objects. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.1', 'Using strong cryptography, render all authentication credentials (such as passwords/phrases) unreadable during transmission and storage on all system components. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.4', 'Provide appropriate training to staff with security breach response responsibilities. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.5', 'Implemented mitigation for improper error handling.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3.6', 'Place system components that store cardholder data (such as a database) in an internal network zone, segregated from the DMZ and other untrusted networks. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.1', 'Create the incident response plan to be implemented in the event of system breach. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4', 'Implement procedures to identify and authorize visitors. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.5', 'Acceptable uses of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '7.2', 'Establish an access control system(s) for systems components that restricts access based on a user''s need to know, and is set to deny all unless specifically allowed. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5', 'Document and implement procedures to protect keys used to secure stored cardholder data against disclosure and misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '5.1.2', 'For systems considered to be not commonly affected by malicious software, perform periodic evaluations to identify and evaluate evolving malware threats in order to confirm whether such systems continue to not require antivirus software. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6.3', 'Follow up exceptions and anomalies identified during the review process. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.3.4.1', 'Additional requirement for service providers only: If segmentation is used, confirm PCI DSS scope by performing penetration testing on segmentation controls at least every six months and after any changes to segmentation controls/methods. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.8', 'Ensure that security policies and operational procedures for identification and authentication are documented, in use, and known to all affected parties. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.1', 'Implement only one primary function per server to prevent functions that require different security levels from coexisting on the same server. (For example, web servers, database servers, and DNS should be implemented on separate servers.) ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.6', 'Create audit logs for all initialization, stopping, or pausing of the audit logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5.8', 'Implemented mitigation for improper access control (such as insecure direct object references, failure to restrict URL access, directory traversal, and failure to restrict user access to functions). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.1', 'Implement audit trails to link all access to system components to each individual user. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.10.2', 'Review and test the plan, including all elements listed in Requirement 12.10.1, at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.3', 'Control physical access for onsite personnel to sensitive areas.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.2.2', 'Perform quarterly external vulnerability scans, via an Approved Scanning Vendor (ASV) approved by the Payment Card Industry Security Standards Council (PCI SSC). Perform rescans as needed, until passing scans are achieved. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.3', 'Develop internal and external software applications (including webbased administrative access to applications) securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.3.10', 'For personnel accessing cardholder data via remoteaccess technologies, prohibit the copying, moving, and storage of cardholder data onto local hard drives and removable electronic media, unless explicitly authorized for a defined business need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.2.4', 'Change user passwords/passphrases at least once every 90 days.  ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.2', 'Do not store sensitive authentication data after authorization (even if encrypted). If sensitive authentication data is received, render all data unrecoverable upon completion of the authorization process. It is permissible for issuers and companies that support issuing services to store sensitive authentication data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.1.5', 'Description of groups, roles, and responsibilities for management of network components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.1', 'Assign all users a unique ID before allowing them to access system components or cardholder data. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.1', 'Always change vendorsupplied defaults and remove or disable unnecessary default accounts before installing a system on the network. This applies to ALL default passwords, including but not limited to those used by operating systems, software that provides security services, application and system accounts, pointofsale (POS) terminals, payment applications, Simple Network Management Protocol (SNMP) community strings, etc.). ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.8.1', 'Maintain a list of service providers including a description of the service provided. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.4', 'Use intrusiondetection and/or intrusionprevention techniques to detect and/or prevent intrusions into the network. Monitor all traffic at the perimeter of the cardholder data environment as well as at critical points in the cardholder data environment, and alert personnel to suspected compromises. Keep all intrusiondetection and prevention engines, baselines, and signatures up to date. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.2.7', 'Create audit logs for all creation and deletion of systemlevel objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.5', 'Address common coding vulnerabilities in softwaredevelopment processes as follows: * Train developers at least annually in uptodate secure coding techniques, including how to avoid common coding vulnerabilities. * Develop applications based on secure coding guidelines. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.5.1', 'Additional requirement for service providers only: Maintain a documented description of the cryptographic architecture', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.1.5', 'Manage IDs used by third parties to access, support, or maintain system components via remote access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.0', 'Track and monitor all access to network resources and cardholder data ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.6', 'Review logs and security events for all system components to identify anomalies or suspicious activity. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '2.2.5', 'Remove all unnecessary functionality, such as scripts, drivers, features, subsystems, file systems, and unnecessary web servers. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.6', 'Implement a formal security awareness program to make all personnel aware of the cardholder data security policy and procedures. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.4.4', 'Removal of test data and accounts from system components before the system becomes active / goes into production. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.3', 'Prohibit direct public access between the Internet and any system component in the cardholder data environment. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '8.3.2', 'Incorporate multifactor authentication for all remote network access (both user and administrator, and including thirdparty access for support or maintenance) originating from outside the entity''s network. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '10.3.4', 'Record the audit trail entry success or failure indication for all system components for each event. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.9.1', 'Maintain an uptodate list of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '9.4.4', 'A visitor log is used to maintain a physical audit trail of visitor activity to the facility as well as computer rooms and data centers where cardholder data is stored or transmitted. Document the visitors name, the firm represented, and the onsite personnel authorizing physical access on the log. Retain this log for a minimum of three months, unless otherwise restricted by law. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '11.1', 'Implement processes to test for the presence of wireless access points (802.11), and detect and identify all authorized and unauthorized wireless access points on a quarterly basis. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '4.0', 'Encrypt transmission of cardholder data across open, public networks ', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '12.1', 'Establish, publish, maintain, and disseminate a security policy. ', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '3.6.3', 'Secure cryptographic key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '6.6', 'For publicfacing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks.', '999'); 
---
--- Custom ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (8, '20.0', 'Custom checklist title example', '0'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (8, '20.1', 'Custom checklist item example, lorum ipsum', '14'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (8, '20.0', 'Custom checklist title example', '0'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (8, '20.1', 'Custom checklist item example, lorum ipsum', '14'); 

