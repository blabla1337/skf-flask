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
`timestamp` timestamp NOT NULL
);

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
-- Table structure for table `questions`
--
drop table if exists `questions`;
CREATE TABLE `questions` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`question` varchar(255) NOT NULL,

);

INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (1,  "Does the sprint implement/changes authentication");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (2,  "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (3,  "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (4,  "Does the sprint implement/changes functions that send parameters and data over a GET request method");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (5,  "Does the sprint implement/changes functions that send parameters and data any request methods other then POST and GET");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (6,  "Does the sprint implement/changes functions that use SQL");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (7,  "Does the sprint implement/changes functions that use LDAP");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (8,  "Does the sprint implement/changes functions that perform system commands");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (9,  "Does the sprint implement/changes functions that perform local/remote file inclusion");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (10, "Does the sprint implement/changes functions that uses/parses XML");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (11, "Does the sprint implement/changess functions that reflect user supplied input on the client-side");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (12, "Does the sprint implement/changess functions that use automatic variable binding (ORM)");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (13, "Does the sprint implement/changess WYSIWIG like editors");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (14, "Does the sprint implement/changes JSON");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (15, "Does the sprint implement/changes functionality that stores data in the local/client/session storage");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (16, "Does the sprint implement/changes functionality that needs secure random tokens (password forget link, CSRF, ETC)");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (17, "Does the sprint implement/changes functionality that requires encryption");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (18, "Does the sprint implement/changes functionality which allows users to upload files or other data structures to the application");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (19, "Does the sprint implement/changes functionality which implement/changess functionality that needs to share data "Cross Origin"");
INSERT OR REPLACE INTO `questions` (`id`, `question`) VALUES (20, "Does the sprint implement/changes functionality that contain forwards or redirects");


--
-- Table structure for table `questions_checklists`
--
drop table if exists `questions_checklists`;
CREATE TABLE `questions_checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`questionID` int(11) NOT NULL,
`checklistID` int(11) NOT NULL,
`level` varchar(255)
);


--
-- Table structure for table `checklists`
--
drop table if exists `checklists`;
CREATE TABLE `checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`content` varchar(255) NOT NULL,
`level` int(11)
);


--
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;
CREATE TABLE `checklists_kb` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`questionID` int(11),
`kbID` int(11),
`testguideID` int(11),
`cweID` int(11),
`nistID` int(11),
`codeID_php` int(11),
`codeID_asp` int(11),
`codeID_java` int(11),
`codeID_python` int(11)
);

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
`accessToken` varchar(255)NOT NULL UNIQUE,
`activated` varchar(255),
`access` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "false", "false", "example@owasp.org");

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
`timestamp` timestamp NOT NULL
);

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
-- Table structure for table `questions_checklists`
--
drop table if exists `questions_checklists`;
CREATE TABLE `questions_checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`questionID` int(11) NOT NULL,
`checklistID` int(11) NOT NULL,
`level` varchar(255)
);


--
-- Table structure for table `checklists`
--
drop table if exists `checklists`;
CREATE TABLE `checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`content` varchar(255) NOT NULL,
`level` int(11),
`testguideID` int(11),
`cweID` int(11),
`pcidssID` int(11),
`nistID` int(11)
);


--
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;
CREATE TABLE `checklists_kb` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` varchar(255),
`questionID` int(11),
`kbID` int(11),
`codeID_php` int(11),
`codeID_asp` int(11),
`codeID_java` int(11),
`codeID_python` int(11),
`include_always` bool,
`include_first` bool
);

INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.9, 0, 185, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.1, 0, 15, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.2, 0, 251, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.3, 0, 83, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.4, 0, 99, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.5, 0, 100, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.6, 0, 45, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.7, 0, 78, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.8, 0, 236, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.9, 0, 134, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.10, 0, 74, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.10, 0, 107, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.11, 0, 45, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.12, 0, 191, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (8.13, 0, 210, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.1, 0, 140, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.2, 0, 999, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.3, 0, 72, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.4, 0, 19, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.5, 0, 145, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.11, 0, 208, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.6, 0, 135, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.7, 0, 142, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.8, 0, 125, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.9, 0, 190, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.10, 0, 235, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (9.11, 0, 135, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.1, 0, 101, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.3, 0, 244, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.4, 0, 103, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (V2:, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.5, 0, 139, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.6, 0, 84, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.8, 0, 127, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.10, 0, 168, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.11, 0, 192, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.12, 0, 255, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.13, 0, 170, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.14, 0, 139, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.15, 0, 198, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (10.16, 0, 247, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.1, 0, 45, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.1, 0, 129, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.2, 0, 104, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.3, 0, 131, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.4, 0, 20, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.5, 0, 130, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.6, 0, 193, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.7, 0, 178, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (11.8, 0, 21, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (13.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.2, 0, 113, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (13.1, 0, 239, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (13.2, 0, 105, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (15.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (15.1, 0, 110, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (15.2, 0, 125, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.1, 0, 67, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.2, 0, 225, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.3, 0, 226, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.4, 0, 250, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.4, 0, 43, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.5, 0, 112, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.6, 0, 227, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.7, 0, 138, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.8, 0, 13, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (16.9, 0, 194, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.1, 0, 211, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.2, 0, 212, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.3, 0, 213, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.4, 0, 214, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.6, 0, 114, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.5, 0, 215, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.6, 0, 216, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.7, 0, 217, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.8, 0, 218, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.9, 0, 219, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.10, 0, 220, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (17.11, 0, 221, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.1, 0, 33, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.2, 0, 187, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.7, 0, 59, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.3, 0, 175, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.4, 0, 176, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.5, 0, 197, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.6, 0, 152, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.7, 0, 224, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.8, 0, 160, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.9, 0, 195, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (18.10, 0, 80, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.1, 0, 14, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.8, 0, 85, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.2, 0, 102, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.3, 0, 246, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.4, 0, 106, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.5, 0, 199, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.6, 0, 237, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.7, 0, 200, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.8, 0, 238, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.9, 0, 201, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (19.10, 0, 223, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.1, 0, 161, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.9, 0, 86, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.12, 0, 76, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.13, 0, 51, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.16, 0, 122, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.17, 0, 243, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.18, 0, 70, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.19, 0, 63, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.20, 0, 29, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.21, 0, 65, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.22, 0, 115, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.2, 0, 162, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.23, 0, 182, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.24, 0, 87, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.25, 0, 88, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.26, 0, 233, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.27, 0, 59, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.28, 0, 165, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.29, 0, 251, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.31, 0, 231, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.32, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (2.33, 0, 209, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.3, 0, 163, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.1, 0, 132, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.2, 0, 57, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.3, 0, 60, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.4, 0, 89, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.5, 0, 90, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.6, 0, 91, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.7, 0, 58, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.10, 0, 56, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.11, 0, 55, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.4, 0, 163, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.12, 0, 92, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.16, 0, 188, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.17, 0, 253, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (3.18, 0, 254, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.1, 0, 126, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.4, 0, 44, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.5, 0, 61, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.8, 0, 242, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.9, 0, 240, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.5, 0, 250, 0, 0, 0, 0, true, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.10, 0, 258, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.11, 0, 259, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.12, 0, 232, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.13, 0, 5, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.14, 0, 116, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.15, 0, 111, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (4.16, 0, 241, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.1, 0, 146, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.3, 0, 95, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.6, 0, 172, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.5, 0, 108, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.6, 0, 96, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.10, 0, 46, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.11, 0, 11, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.12, 0, 4, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.13, 0, 173, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.14, 0, 183, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.15, 0, 3, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.16, 0, 147, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.17, 0, 71, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.7, 0, 184, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.18, 0, 166, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.19, 0, 167, 0, 0, 0, 0, true, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.20, 0, 234, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.21, 0, 202, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.22, 0, 180, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.23, 0, 189, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.24, 0, 179, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.25, 0, 181, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (5.26, 0, 249, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.0, 0, 0, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (1.8, 0, 206, 0, 0, 0, 0, false, true);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.2, 0, 149, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.6, 0, 118, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.7, 0, 119, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.8, 0, 141, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.9, 0, 121, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.11, 0, 196, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.12, 0, 207, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.13, 0, 203, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.14, 0, 204, 0, 0, 0, 0, false, false);
INSERT OR REPLACE INTO `checklists_kb` (`checklistID`, `questionID`, `kbID`, `codeID_php`, `codeID_asp`, `codeID_java`, `codeID_python`, `include_always`, `include_first`) VALUES (7.15, 0, 205, 0, 0, 0, 0, false, false);
