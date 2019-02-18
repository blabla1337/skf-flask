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

INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "$2b$12$BlLgoO6rSAsyoioB3Qo9AuDwQlRnGIchSpyY12Hiks1mNziNgcsCu", "1234", "True", "True", "example@owasp.org");

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

INSERT OR REPLACE INTO `kb_items` ( `title`, `content`) VALUES ( "test title kb item 1", "test content kb item 1");
INSERT OR REPLACE INTO `kb_items` ( `title`, `content`) VALUES ( "test title kb item 2", "test content kb item 2");
INSERT OR REPLACE INTO `kb_items` ( `title`, `content`) VALUES ( "test title kb item 3", "test content kb item 3");
INSERT OR REPLACE INTO `kb_items` ( `title`, `content`) VALUES ( "test title kb item 4", "test content kb item 4");
INSERT OR REPLACE INTO `kb_items` ( `title`, `content`) VALUES ( "test title kb item 5", "test content kb item 5");

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

INSERT OR REPLACE INTO `code_items` ( `code_lang`, `content`, `title`) VALUES ("php", "test php code item 1", "test php content code item 1");
INSERT OR REPLACE INTO `code_items` ( `code_lang`, `content`, `title`) VALUES ("php", "test php code item 2", "test php content code item 2");
INSERT OR REPLACE INTO `code_items` ( `code_lang`, `content`, `title`) VALUES ("asp", "test asp code item 1", "test asp content code item 1");
INSERT OR REPLACE INTO `code_items` ( `code_lang`, `content`, `title`) VALUES ("asp", "test asp code item 2", "test asp content code item 2");


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

INSERT OR REPLACE INTO `questions_sprint` ( `checklist_type`, `question`) VALUES ( "1", "test-question-sprint");
INSERT OR REPLACE INTO `questions_sprint` ( `checklist_type`, `question`) VALUES ( "2", "test-question-sprint");

--
-- Table structure for table `questions_pre`
--
drop table if exists `questions_pre`;
CREATE TABLE `questions_pre` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);


INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES ( "1", "test-question-pre");
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES ( "2", "test-question-pre");

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
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "empty-checklist-for-testing", "TBD");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "filled-checklist-for-testing", "TBD");

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
`checklist_type` int(11),
`cwe` int(11)
); 

INSERT OR REPLACE INTO `checklists_kb` VALUES (1,'1.1','test content checklist item 1',0,2,1,'True','False',2, 123);
INSERT OR REPLACE INTO `checklists_kb` VALUES (2,'1.2','test content checklist item 2',0,0,2,'False','False',2, 124);
INSERT OR REPLACE INTO `checklists_kb` VALUES (3,'1.3','test content checklist item 3',2,0,3,'false','true',2, 125);
INSERT OR REPLACE INTO `checklists_kb` VALUES (4,'1.4','test content checklist item 4',0,2,3,'false','false',2, 126);
