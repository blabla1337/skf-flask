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
`entryDate` timestamp NOT NULL
);

-- 
-- Table structure for table `projects`
--
drop table if exists `projects`;
CREATE TABLE `projects` (
`projectID` INTEGER PRIMARY KEY AUTOINCREMENT,
`projectName` varchar(250) NOT NULL,
`projectVersion` varchar(250) NOT NULL,
`projectDesc` text NOT NULL,
`timestamp` timestamp NOT NULL
);

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
`entryDate` timestamp NOT NULL
);



