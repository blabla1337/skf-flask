


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
-- Table structure for table `techhacks`
--
drop table if exists `techhacks`;
CREATE TABLE `techhacks` (
`techID` int(11) NOT NULL,
`techName` varchar(255) NOT NULL
);

INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (1, 'SQL commands');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (2, 'Path or Filenames');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (3, 'File inclusion');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (4, 'X-Path');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (5, 'User-input in HTML output');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (6, 'LDAP commands');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (7, 'HTTP headers');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (8, 'XSLT input and output');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (9, 'SSI commands');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (10, 'System commands');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (11, 'Private user data');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (12, 'Eval type functions');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (13, 'Regular expressions');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (14, 'File upload ');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (15, 'File Download');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (16, 'XML files');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (17, 'GET variables or parameters');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (18, 'Forward or redirect');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (19, 'Password forget functions');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (20, 'Sessions');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (21, 'Forms');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (22, 'User registration');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (23, 'Access controls or Login systems');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (24, 'sub-domains');
INSERT OR REPLACE INTO `techhacks` (`techID`, `techName`) VALUES (25, 'third party software');
