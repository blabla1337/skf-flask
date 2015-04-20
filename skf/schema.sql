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



