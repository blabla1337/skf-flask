-- 
-- Table structure for table `parameters`
-- 
drop table if exists `parameters`;
CREATE TABLE `parameters` (
`paramID` INTEGER PRIMARY KEY AUTOINCREMENT,
`functionName` varchar(250) NOT NULL,
`tech` int(11) NOT NULL,
`projectID` int(11) NOT NULL,
`functionDesc` text CHARACTER NOT NULL,
`techVuln` int(11) NOT NULL,
`entryDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
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
`timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
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

-- 
-- Table structure for table `techvuln`
-- 
drop table if exists `techvuln`;
CREATE TABLE `techvuln` (
`techVulnID` INTEGER PRIMARY KEY AUTOINCREMENT,
`techID` int(11) NOT NULL,
`vulnID` int(11) NOT NULL
);
