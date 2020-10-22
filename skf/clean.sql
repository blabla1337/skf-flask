
--
-- Table structure for table `kb_items`
--
drop table if exists `kb_items`;
CREATE TABLE `kb_items` (
`kb_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL
);


--
-- Table structure for table `code_items`
--
drop table if exists `code_items`;
CREATE TABLE `code_items` (
`code_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`title` varchar(250) NOT NULL,
`content` varchar(250) NOT NULL,
`code_lang` varchar(250) NOT NULL
);


