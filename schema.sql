-- 
-- Table structure for table `parameters`
-- 
drop table if exists `parameters`;
CREATE TABLE `parameters` (
`paramID` int(11) NOT NULL AUTO_INCREMENT,
`functionName` varchar(250) NOT NULL,
`tech` int(11) NOT NULL,
`projectID` int(11) NOT NULL,
`userID` int(11) NOT NULL,
`functionDesc` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
`techVuln` int(11) NOT NULL,
`entryDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`paramID`)
);

-- 
-- Table structure for table `projects`
--
drop table if exists `projects`;
CREATE TABLE `projects` (
`projectID` int(11) NOT NULL AUTO_INCREMENT,
`projectName` varchar(250) NOT NULL,
`projectVersion` varchar(250) NOT NULL,
`projectDesc` text NOT NULL,
`userID` int(11) NOT NULL,
`timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`projectID`)
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
`techVulnID` int(11) NOT NULL AUTO_INCREMENT,
`techID` int(11) NOT NULL,
`vulnID` int(11) NOT NULL,
PRIMARY KEY (`techVulnID`)
);
