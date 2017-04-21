--
-- Table structure for table `users`
--
drop table if exists `users`;
CREATE TABLE `users` (
`userID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilegeID` int(11) NOT NULL,
`userName` varchar(255) NOT NULL UNIQUE,
`email` varchar(255) ,
`password` varchar(255) NOT NULL,
`accessToken` varchar(255),
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
`status` varchar(255) NOT NULL,
`message` varchar(255) NOT NULL
);


--
-- Table structure for table `checklists`
--
drop table if exists `checklists`;
CREATE TABLE `checklists` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` int(11),
`content` varchar(255) NOT NULL,
`level` int(11),
`testguideID` int(11),
`cweID` int(11),
`nistID` int(11)
);

--
-- Table structure for table `questions`
--
drop table if exists `questions`;
CREATE TABLE `questions` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`question` varchar(255) NOT NULL,
`include_always` int(11),
`include_first` int(11)
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
`checklistID` int(11),
`content` varchar(255) NOT NULL,
`level` int(11),
`testguideID` int(11),
`cweID` int(11),
`nistID` int(11)
);


--
-- Table structure for table `checklists_kb`
--
drop table if exists `checklists_kb`;
CREATE TABLE `checklists_kb` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklistID` int(11),
`questionID` int(11),
`kbID` int(11),
`codeID_php` int(11),
`codeID_asp` int(11),
`codeID_java` int(11),
`codeID_python` int(11)
);
