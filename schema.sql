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
`vulnID` int(11) NOT NULL,
PRIMARY KEY (`techID`)
);
INSERT INTO `techhacks` (`techID`, `techName`, `vulnID`) VALUES
(1, 'SQL commands', 46),
(2, 'Path/Filenames', 1),
(3, 'File inclusion', 1),
(4, 'X-Path commands', 7),
(5, 'HTML output', 3),
(6, 'LDAP commands', 11),
(7, 'HTTP headers', 1),
(8, 'XSL(T) input/output', 9),
(9, 'SSI commands', 12),
(10, 'System commands', 4),
(11, 'Resource identifiers', 34),
(12, '"Eval" type functions', 4),
(13, 'Regular expressions', 36),
(14, 'File upload ', 13),
(20, 'XML files', 8),
(21, 'External XML files', 6),
(22, 'JSON ', 3),
(23, 'GET variables/parameters', 72),
(24, 'Forward or/ redirect', 67),
(25, 'Access controls/Login systems', 152);

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



