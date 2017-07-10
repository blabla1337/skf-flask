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
`level` int(11) NOT NULL
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
`question` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (1, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (2, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (3, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (4, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (5, "Does the sprint implement/changes functions that send parameters and data any request methods other then POST and GET?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (6, "Does the sprint implement/changes functions that use SQL?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (7, "Does the sprint implement/changes functions that use LDAP?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (8, "Does the sprint implement/changes functions that perform system commands?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (9, "Does the sprint implement/changes functions that perform local/remote file inclusion?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (10, "Does the sprint implement/changes functions that uses/parses XML?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (11, "Does the sprint implement/changess functions that reflect user supplied input on the client-side?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (12, "Does the sprint implement/changess functions that use automatic variable binding (ORM)?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (13, "Does the sprint implement/changess WYSIWIG like editors?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (14, "Does the sprint implement/changes JSON?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (15, "Does the sprint implement/changes functionality that stores data in the local/client/session storage?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (16, "Does the sprint implement/changes functionality that needs secure random tokens (password forget link, CSRF, ETC)?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (17, "Does the sprint implement/changes functionality that requires encryption?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (18, "Does the sprint implement/changes functionality which allows users to upload files or other data structures to the application?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (19, "Does the sprint implement/changes functionality which implement/changess functionality that needs to share data 'Cross Origin'?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (20, "Does the sprint implement/changes functionality that contain forwards or redirects?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (21, "Does the sprint implement/changes functionality that are API?");
INSERT OR REPLACE INTO `questions_sprint` (`id`, `question`) VALUES (22, "Does the sprint implement/changes functionality that are mobile (native, xamarin, corona, etc)?");


--
-- Table structure for table `questions_pre`
--
drop table if exists `questions_pre`;
CREATE TABLE `questions_pre` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`question` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `questions_pre` (`id`, `question`) VALUES (1, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`id`, `question`) VALUES (2, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`id`, `question`) VALUES (3, "You have a central Single Sign On service and validated this service using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`id`, `question`) VALUES (4, "You have a central Identity Management System service and validated this service using ASVS?");


--
-- Table structure for table `checklists`
--
drop table if exists `checklists`;
CREATE TABLE `checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`content` varchar(255) NOT NULL,
`level` int(11),
`kbID` int(11)
);


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
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;
CREATE TABLE `checklists_kb` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`question_sprint_ID` int(11),
`question_pre_ID` int(11),
`kbID` int(11),
`codeID_php` int(11),
`codeID_asp` int(11),
`codeID_java` int(11),
`codeID_python` int(11),
`include_always` boolean,
`include_first` boolean
); 


INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.9', 0, 1, 185, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.1', 0, 0, 15, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.2', 0, 0, 251, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.3', 0, 0, 83, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.4', 0, 0, 99, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.5', 0, 0, 100, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.6', 0, 0, 45, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.7', 0, 0, 78, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.8', 0, 0, 236, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.9', 0, 0, 134, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.10', 0, 1, 74, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.10', 0, 0, 107, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.11', 0, 0, 45, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.12', 0, 0, 191, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('8.13', 0, 0, 210, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.1', 0, 0, 140, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.2', 0, 0, 999, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.3', 3, 0, 72, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.3', 4, 0, 72, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.3', 5, 0, 72, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.4', 0, 0, 19, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.5', 0, 0, 145, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.11', 0, 1, 208, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.6', 0, 0, 135, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.7', 0, 0, 142, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.8', 0, 0, 125, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.9', 0, 0, 190, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.10', 0, 0, 235, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('9.11', 0, 0, 135, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.1', 0, 0, 101, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.3', 0, 0, 244, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.4', 0, 0, 103, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.5', 0, 0, 139, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.6', 0, 0, 84, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.8', 0, 0, 127, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.10', 0, 0, 168, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.11', 0, 0, 192, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.12', 0, 0, 255, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.13', 0, 0, 170, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.14', 0, 0, 139, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.15', 0, 0, 198, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('10.16', 0, 0, 247, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.1', 0, 3, 45, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.1', 3, 2, 129, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.1', 4, 2, 129, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.1', 5, 2, 129, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.2', 0, 2, 104, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.3', 0, 2, 131, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.4', 0, 2, 20, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.5', 0, 2, 130, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.6', 14, 2, 193, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.7', 0, 2, 178, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('11.8', 0, 2, 21, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('13.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.2', 1, 3, 113, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('13.1', 0, 2, 239, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('13.2', 0, 2, 105, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('15.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('15.1', 0, 0, 110, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('15.2', 0, 0, 125, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.1', 20, 0, 67, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.2', 8, 0, 225, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.3', 18, 0, 226, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.4', 9, 0, 250, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.4', 1, 3, 43, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.5', 19, 0, 112, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.6', 18, 0, 227, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.7', 9, 0, 138, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.8', 18, 0, 13, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('16.9', 0, 0, 194, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.1', 22, 0, 211, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.2', 22, 0, 212, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.3', 22, 0, 213, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.4', 22, 0, 214, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.6', 1, 3, 114, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.5', 22, 0, 215, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.6', 22, 0, 216, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.7', 22, 0, 217, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.8', 22, 0, 218, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.9', 22, 0, 219, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.10', 22, 0, 220, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('17.11', 22, 0, 221, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.1', 21, 0, 33, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.2', 21, 0, 187, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.7', 1, 3, 59, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.3', 21, 0, 175, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.4', 21, 0, 176, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.5', 21, 0, 197, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.6', 21, 0, 152, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.7', 21, 0, 224, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.8', 21, 0, 160, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.9', 21, 0, 195, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('18.10', 21, 0, 80, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.1', 0, 2, 14, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.8', 2, 3, 85, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.2', 0, 2, 102, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.3', 0, 2, 246, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.4', 0, 2, 106, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.5', 0, 2, 199, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.6', 0, 2, 237, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.7', 0, 2, 200, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.8', 0, 2, 238, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.9', 0, 2, 201, 0, 0, 0, 0, 'False', 'True');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('19.10', 0, 2, 223, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.1', 0, 1, 161, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.9', 2, 3, 86, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.12', 1, 3, 76, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.13', 1, 3, 51, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.16', 2, 3, 122, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.17', 2, 3, 243, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.18', 2, 3, 70, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.19', 0, 3, 63, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.20', 1, 3, 29, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.21', 1, 3, 65, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.22', 2, 3, 115, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.2', 0, 1, 162, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.23', 1, 3, 182, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.24', 2, 3, 87, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.25', 1, 3, 88, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.26', 1, 3, 233, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.27', 1, 3, 222, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.28', 1, 3, 165, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.29', 1, 3, 251, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.31', 1, 3, 231, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.32', 1, 3, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('2.33', 1, 3, 209, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.3', 0, 1, 163, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.1', 1, 3, 132, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.2', 1, 3, 57, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.3', 1, 3, 60, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.4', 1, 3, 89, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.5', 1, 3, 90, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.6', 1, 3, 91, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.7', 2, 3, 58, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.10', 1, 3, 56, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.11', 1, 3, 55, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.4', 0, 1, 163, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.12', 1, 3, 92, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.16', 1, 3, 188, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.17', 1, 3, 253, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('3.18', 2, 3, 254, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.1', 0, 4, 126, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.4', 0, 4, 44, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.5', 0, 4, 61, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.8', 1, 4, 242, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.9', 1, 4, 240, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.5', 0, 1, 260, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.10', 1, 4, 258, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.11', 1, 4, 259, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.12', 1, 4, 232, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.13', 3, 4, 5, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.14', 3, 4, 116, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.14', 4, 4, 116, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.15', 2, 4, 111, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('4.16', 1, 4, 241, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.1', 0, 0, 146, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.3', 3, 0, 95, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.3', 4, 0, 95, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.3', 5, 0, 95, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.6', 0, 1, 172, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.5', 3, 0, 108, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.5', 4, 0, 108, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.5', 5, 0, 108, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.6', 3, 0, 96, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.6', 4, 0, 96, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.6', 5, 0, 96, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.10', 6, 0, 46, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.11', 7, 0, 11, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.12', 8, 0, 4, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.13', 9, 0, 173, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.14', 10, 0, 183, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.15', 11, 0, 3, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.16', 12, 0, 147, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.17', 3, 0, 71, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.17', 4, 0, 71, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.17', 5, 0, 71, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.7', 0, 1, 184, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.18', 3, 0, 166, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.18', 4, 0, 166, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.18', 5, 0, 166, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.19', 0, 0, 167, 0, 0, 0, 0, 'True', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.20', 3, 0, 234, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.20', 4, 0, 234, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.20', 5, 0, 234, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.21', 3, 0, 202, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.21', 4, 0, 202, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.21', 5, 0, 202, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.22', 13, 0, 180, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.23', 11, 0, 189, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.24', 11, 0, 179, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.25', 14, 0, 181, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('5.26', 15, 0, 249, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.0', 0, 0, 0, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('1.8', 0, 1, 206, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.2', 17, 0, 149, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.6', 1, 0, 118, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.6', 2, 0, 118, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.6', 16, 0, 118, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.7', 17, 0, 119, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.8', 17, 0, 141, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.9', 17, 0, 121, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.11', 17, 0, 196, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.12', 17, 0, 207, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.13', 17, 0, 203, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.14', 17, 0, 204, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.15', 1, 0, 205, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.15', 2, 0, 205, 0, 0, 0, 0, 'False', 'False');
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `question_sprint_ID`, `question_pre_ID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES ('7.15', 16, 0, 205, 0, 0, 0, 0, 'False', 'False');
