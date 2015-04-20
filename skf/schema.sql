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

INSERT INTO `techhacks` ('techID', 'techName', 'vulnID') VALUES
(1, 'SQL commands', 46),
(2, 'Path or Filenames', 1),
(3, 'File inclusion', 1),
(4, 'X-Path commands', 7),
(5, 'HTML output', 3),
(6, 'LDAP commands', 11),
(7, 'HTTP headers', 1),
(8, 'XSLT input and output', 9),
(9, 'SSI commands', 12),
(10, 'System commands', 4),
(11, 'Resource identifiers', 34),
(12, 'Eval type functions', 4),
(13, 'Regular expressions', 36),
(14, 'File upload ', 13),
(15, 'XML files', 8),
(16, 'External XML files', 6),
(17, 'JSON ', 3),
(18, 'GET variables or parameters', 72),
(19, 'Forward or redirect', 67),
(20, 'Password forget functions', 153),
(21, 'Sessions', 154),
(22, 'Submit forms', 155),
(23, 'User registration', 157),
(24, 'Access controls or Login systems', 152);
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



