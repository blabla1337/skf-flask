-- 
-- Table structure for table `parameters`
-- 
drop table if exists `parameters`;
CREATE TABLE `parameters` (
`paramID` INTEGER PRIMARY KEY AUTOINCREMENT,
`functionName` varchar(250) NOT NULL,
`tech` varchar(250) NOT NULL,
`techVuln` varchar(11) NOT NULL,
`projectID` varchar(11) NOT NULL,
`functionDesc` text CHARACTER NOT NULL,
`entryDate` timestamp NOT NULL,
`userID` int(11) NOT NULL
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
-- Table structure for table `groupMembers`
--
drop table if exists `groupMembers`;
CREATE TABLE `groupMembers` (
`memberID` INTEGER PRIMARY KEY AUTOINCREMENT,
`userID` int(11) NOT NULL,
`groupID` int(11) NOT NULL,
`ownerID` int(11) NOT NULL,
`timestamp` timestamp
);

INSERT OR REPLACE INTO `groupMembers` (`memberID`, `userID`, `groupID`, `ownerID`) VALUES (1, 1, 1, 1);

-- 
-- Table structure for table `techhacks`
-- 
drop table if exists `techhacks`;
CREATE TABLE `techhacks` (
`techID` int(11) NOT NULL,
`techName` varchar(255) NOT NULL,
`vulnID` int(11) NOT NULL
);

INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (1, 'SQL commands', 46);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (2, 'Path or Filenames', 1);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (3, 'File inclusion', 1);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (4, 'X-Path', 7);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (5, 'User-input in HTML output', 3);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (6, 'LDAP commands', 11);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (7, 'HTTP headers', 71);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (8, 'XSLT input and output', 9);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (9, 'SSI commands', 12);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (10, 'System commands', 4);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (11, 'Private user data', 34);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (12, 'Eval type functions', 4);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (13, 'Regular expressions', 36);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (14, 'File upload ', 13);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (15, 'File Download', 160);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (16, 'XML files', 8);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (17, 'External XML files', 6);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (18, 'JSON ', 3);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (19, 'GET variables or parameters', 72);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (20, 'Forward or redirect', 67);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (21, 'Password forget functions', 153);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (22, 'Sessions', 154);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (23, 'Forms', 155);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (24, 'User registration', 157);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (25, 'Access controls or Login systems', 152);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (26, 'sub-domains', 158);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (27, 'HTML', 159);
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES (28, 'third party software', 14);


-- 
-- Table structure for table `questionlist`
-- 
drop table if exists `questionlist`;
CREATE TABLE `questionlist` (
`listID` INTEGER PRIMARY KEY AUTOINCREMENT,
`answer` varchar(255) NOT NULL,
`projectID` varchar(255) NOT NULL,
`projectName` varchar(255) NOT NULL,
`questionID` varchar(255) NOT NULL,
`vulnID` varchar(255) NOT NULL,
`listName` varchar(255) NOT NULL,
`entryDate` timestamp NOT NULL,
`userID` int(11) NOT NULL
);

-- 
-- Table structure for table `users`
-- 
drop table if exists `users`;
CREATE TABLE `users` (
`userID` INTEGER PRIMARY KEY AUTOINCREMENT,
`privilegeID` int(11) NOT NULL,
`userName` varchar(255) NOT NULL,
`email` varchar(255) ,
`password` varchar(255) NOT NULL,
`accessToken` varchar(255),
`access` varchar(255) NOT NULL
);

-- 
-- Table structure for table `counter`
-- 
drop table if exists `counter`;
CREATE TABLE `counter` (
`counterID` INTEGER PRIMARY KEY AUTOINCREMENT,
`userID` int(11) NOT NULL,
`countEvil` int(11) NOT NULL,
`block` int(11) NOT NULL
);

INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `username`, `password`, `access`) VALUES (1, 1, "superadmin", "$2a$12$Da5N2VrqE/rFHjSP2QJt.uo6QmgA0OoBDx3AwDAlJkQhNY7IT/teu", "true");


INSERT OR REPLACE INTO `counter` (`counterID`, `userID`, `countEvil`, `block`) VALUES (1, 1, 0, 0);



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



