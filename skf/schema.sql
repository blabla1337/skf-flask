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

INSERT OR REPLACE INTO `users` (`userID`, `privilegeID`, `userName`, `password`, `accessToken`, `access`, `activated`, `email`) VALUES (1, 1, "admin", "", "1234", "False", "False", "example@owasp.org");


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

--
--ASVS lvl 1
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (1, "Does the sprint implement/changes functions that send parameters and data any request methods other then POST and GET?");
--
--ASVS lvl 2
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (2, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (2, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
--
--ASVS lvl 3
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (3, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (3, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
--
--MASVS lvl 1
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (4, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--MASVS lvl 2
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (5, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--MASVS lvl 3
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes authentication?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that extend the primairy authentication mechanism (re-authentication/password forget/step-up/etc)?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (6, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--PCIDSS
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (10, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (10, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");
--
--CUSTOM
--
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (8, "Does the sprint implement/changes functions that sends parameters in the request body such as i.e POST requests?");
INSERT OR REPLACE INTO `questions_sprint` (`checklist_type`,  `question`) VALUES (8, "Does the sprint implement/changes functions that send parameters and data over a GET request method?");

--
-- Table structure for table `questions_pre`
--
drop table if exists `questions_pre`;
CREATE TABLE `questions_pre` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
`checklist_type` int(11),
`question` varchar(255) NOT NULL
);

--
--ASVS lvl 1
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (1, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (1, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--ASVS lvl 2
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (2, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (2, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--ASVS lvl 3
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a central Single Sign On service and validated this service using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (3, "You have a central Identity Management System service and validated this service using ASVS?");
--
--MASVS lvl 1
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (4, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (4, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--MASVS lvl 2
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (5, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (5, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--MASVS lvl 3
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a central Single Sign On service and validated this service using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (6, "You have a central Identity Management System service and validated this service using ASVS?");
--
--PCIDSS
--
INSERT OR REPLACE INTO `questions_pre` ( `checklist_type`, `question`) VALUES (10, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (10, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
--
--CUSTOM
--
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (8, "You have a blueprint for the design, architecture and validated this using ASVS?");
INSERT OR REPLACE INTO `questions_pre` (`checklist_type`, `question`) VALUES (8, "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");


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
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv1", "An application achieves ASVS Level 1 (or Opportunistic) if it adequately defends against application security vulnerabilities that are easy to discover, and included in the OWASP Top 10 and other similar checklists. Level 1 is typically appropriate for applications where low confidence in the correct use of security controls is required, or to provide a quick analysis of a fleet of enterprise applications, or assisting in developing a prioritized list of security requirements as part of a multi-phase effort. Level 1 controls can be ensured either automatically by tools or simply manually without access to source code. We consider Level 1 the minimum required for all applications. Threats to the application will most likely be from attackers who are using simple and low effort techniques to identify easy-to-find and easy-to-exploit vulnerabilities. This is in contrast to a determined attacker who will spend focused energy to specifically target the application. If data processed by your application has high value, you would rarely want to stop at a Level 1 review.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv2", "An application achieves ASVS Level 2 (or Standard) if it adequately defends against most of the risks associated with software today. Level 2 ensures that security controls are in place, effective, and used within the application. Level 2 is typically appropriate for applications that handle significant business-to-business transactions, including those that process healthcare information, implement businesscritical or sensitive functions, or process other sensitive assets. Threats to Level 2 applications will typically be skilled and motivated attackers focusing on specific targets using tools and techniques that are highly practiced and effective at discovering and exploiting weaknesses within applications.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "ASVS Lv3", "ASVS Level 3 is the highest level of verification within the ASVS. This level is typically reserved for applications that require significant levels of security verification, such as those that may be found within areas of military, health and safety, critical infrastructure, etc. Organisations may require ASVS Level 3 for applications that perform critical functions, where failure could significantly impact the organization's operations, and even its survivability. Example guidance on the application of ASVS Level 3 is provided below. An application achieves ASVS Level 3 (or Advanced) if it adequately defends against advanced application security vulnerabilities and also demonstrates principles of good security design. An application at ASVS Level 3 requires more in depth analysis, architecture, coding, and testing than all the other levels. A secure application is modularized in a meaningful way (to facilitate e.g. resiliency, scalability, and most of all, layers of security), and each module (separated by network connection and/or physical instance) takes care of its own security responsibilities (defence in depth), that need to be properly documented. Responsibilities include controls for ensuring confidentiality (e.g. encryption), integrity (e.g. transactions, input validation), availability (e.g. handling load gracefully), authentication (including between systems), non-repudiation, authorization, and auditing (logging).");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS Lv1", "A mobile app that achieves MASVS-L1 adheres to mobile application security best practices. It fulfills basic requirements in terms of code quality, handling of sensitive data, and interaction with the mobile environment. A testing process must be in place to verify the security controls. This level is appropriate for all mobile applications.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS Lv2", "MASVS-L2 introduces advanced security controls that go beyond the standard requirements. To fulfil L2, a threat model must exist, and security must be an integral part of the app's architecture and design. This level is appropriate for applications that handle sensitive data, such as mobile banking.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "MASVS LvR", "The app has state-of-the-art security, and is also resilient against specific, clearly defined client-side attacks, such as tampering, modding, or reverse engineering to extract sensitive code or data. Such an app either leverages hardware security features or sufficiently strong and verifiable software protection techniques. MASVS-R is applicable to apps that handle highly sensitive data and may serve as a means of protecting intellectual property or tamper-proofing an app.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "PCIDSS", "The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organizations that handle branded credit cards from the major card schemes. The PCI Standard is mandated by the card brands and administered by the Payment Card Industry Security Standards Council. The standard was created to increase controls around cardholder data to reduce credit card fraud. Validation of compliance is performed annually or quarterly,[1] either by an external Qualified Security Assessor (QSA) or by a firm specific Internal Security Assessor (ISA) that creates a Report on Compliance for organizations handling large volumes of transactions, or by Self-Assessment Questionnaire (SAQ) for companies handling smaller volumes.");
INSERT OR REPLACE INTO `checklist_types` ( `checklist_name`, `checklist_description`) VALUES ( "Custom", "This is a custom checklist");


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
`checklist_type` int(11)
); 

---
--- ASVS lvl 1 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (1, '1.0', 'TBD', '92'); 
---
--- ASVS lvl 2 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (2, '1.0', 'TBD', '92'); 
---
--- ASVS lvl 3 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.0', 'Architecture, Design and Threat Modeling Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.1', 'All app components are identified and known to be needed.', '161'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.2', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '162'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.3', 'A high-level architecture for the application and all connected remote services has been defined and security has been addressed in that architecture.', '163'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.4', 'Data considered sensitive in the context of the application is clearly identified.', '258'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.5', 'All app components are defined in terms of the business functions and/or security functions they provide.', '260'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.6', 'A rudimentary threat analysis has been made to determine which attackers are in scope, and which are currently not in scope.', '172'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.7', 'A detailed threat model for the application and the associated remote services has been produced that identifies potential threats and countermeasures.', '184'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.8', 'All security controls have a centralized implementation as to avoid duplication of critical code.', '206'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.9', 'Components are segregated from each other via a defined security control, such as network segmentation, firewall rules, or cloud based security groups.', '185'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.10', 'A mechanism for enforcing updates of the application exists.', '74'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.11', 'Security is addressed within all parts of the software development lifecycle.', '208'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.12', 'All application components, libraries, modules, frameworks, platform, and operating systems are free from known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '1.13', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced following a key management standard such as NIST SP 800-57.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.0', 'Authentication Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1', 'General Authenticator Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.1', 'Verify revocability of physical authenticators in case of theft or other loss. Ensure that revocation is immediately effective across all Identity Providers and Relying Parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.2', 'Verify that one or more anti-automation controls including rate limiting, CAPTCHA, increasing delays, IP address restrictions, risk-based restrictions are in place and effective to mitigate breached credential testing, brute force, and account lockout attacks. Verify that no more than 100 failed attempts is possible on a single account.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.3', 'Verify that biometric authenticators are limited to use only as secondary factors in conjunction with either something you have and something you know.', '999');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.4', 'Verify impersonation resistance against phishing, such as the use of multi-factor authentication, cryptographic devices with intent (such as connected keys with a push to authenticate), or at higher AAL levels, client-side certificates.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.5', 'Verify that in cases where a verifier and CSP are separate, mutually authenticated TLS is in place between the two endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.6', 'Verify replay resistance through the mandated use of OTP devices, cryptographic authenticators, or lookup codes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.7', 'Verify intent to authenticate by requiring the entry of an OTP token or user-initiated action such as a button press on a FIDO hardware key.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1.8', 'Verify that restricted authenticators such as email and SMS are not a preferred recovery mechanism or second factor, and at least one alternative is offered to the user first. If the user selects a restricted authenticator, a meaningful warning covering the potential risks of that restricted authenticator SHOULD be presented to the user, including that the future use of the restricted authenticator may be removed in the future.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.1', 'Authenticator Lifecycle Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.2.1', 'Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.2.2', 'Verify that enrollment and use of subscriber-provided authentication devices are supported, such as a U2F or FIDO tokens.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.2.3', 'Verify that renewal instructions are sent with sufficient time to renew time bound authenticators.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3', 'Authenticator Recovery Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.1', 'Verify that a system generated activation or recovery password is not sent in clear text to the user.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.2', 'Verify password hints or knowledge-based answers (so-called "secret questions") are not present.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.3', 'Verify password credential recovery does not reveal the current password in any way.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.4', 'Verify forgotten password, and other recovery paths use a TOTP or other soft token, mobile push, or another offline recovery mechanism.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.5', 'Verify identities cannot be re-bound to a different identity (spoofing), and shared accounts are not present ("root", "admin", or "sa").', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.6', 'Verify that if one or more multi-factor authentication factors are lost, that identity proofing and binding is performed at the same level as during enrollment. Once replaced, the verifier MAY use a single factor to re-bind the account to the new factor.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.3.7', 'Verify that if an authentication factor is changed or replaced, that the user is notified of this event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4', 'Memorized Secrets Authenticator Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.1', 'Verify that passwords are at least 8 characters in length.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.2', 'Verify that passwords 64 characters or longer are permitted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.3', 'Verify that passwords can contain spaces and truncation is not performed. Consecutive multiple spaces MAY optionally be coalesced.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.4', 'Verify that Unicode characters are permitted in passwords. A single Unicode code point is considered a character, so 8 emoji or 64 kanji characters should be valid and permitted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.5', 'Verify users can change their password, and the change validates the current secret.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.6', 'Verify that new or changed passwords are validated against a list of compromised secrets, and if found to be compromised, the user is prompted to choose another secret.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.7', 'Verify that a password strength meter is provided to help users set a stronger secret.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.8', 'Verify that there are no password composition rules limiting the type of characters permitted. There should be no requirement for upper or lower case or numbers or special characters.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.9', 'Verify that there are no arbitrary or periodic credential rotation requirements.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.10', 'Verify that the user is required to change their password if the credential has found to be compromised.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.11', 'Verify that "paste" functionality, browser password helpers, and external password managers are permitted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.4.12', 'Verify that the user can choose to either temporarily view the masked entered password, or temporarily view the last typed character of the password.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5', 'Credential Storage Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5.1', 'Verify that passwords are stored in a form that is resistant to offline attacks. Passwords SHALL be salted and hashed using an approved one-way key derivation or password hashing function. Key derivation and password hashing functions take a password, and a cost factor as inputs then generate a password hash.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5.2', 'Verify that the salt is at least 32 bits in length and be chosen arbitrarily to minimize salt value collisions among stored hashes. For each credential, a unique salt value and the resulting hash SHALL be stored.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5.3', 'Verify that if PBKDF2 is used, the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5.4', 'Verify that if bcrypt is used, the work factor SHOULD be as large as verification server performance will allow, typically at least 13.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.5.5', 'Verify that an additional iteration of a key derivation function using a salt value that is secret and known only to the verifier. This salt value, if used, SHALL be generated by an approved random bit generator [SP 800-90Ar1] and provide at least the minimum security strength specified in the latest revision of SP 800-131A. The secret salt value SHALL be stored separately from the hashed passwords (e.g., in a specialized device like a hardware security module).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6', 'Look-up Secret Verifier Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6.1', 'Verify that lookup secrets can be used only once.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6.2', 'Verify that lookup secrets have sufficient randomness (112 bits of entropy), or if less than 112 bits of entropy, salted with a unique and random 32-bit salt and hashed with an approved one-way hash.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6.3', 'Verify that lookup secrets are resistant to offline attacks, such as predictable values.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.6.4', 'Verify that lookup secrets are rate limited, particularly when using less than 64 bits of entropy.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7', 'Out of Band Verifier Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.1', 'Verify that prohibited unencrypted out of band authenticators, such as e-mail or VOIP, is not in use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.2', 'Verify that restricted out of band authenticators, such as SMS or PSTN, are not offered by default, and stronger alternatives such as push notifications are offered first.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.3', 'Verify that the out of band authenticator and verifier communicates over a secure independent channel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.4', 'Verify that the out of band verifier retains only a hashed version of the authentication key.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.5', 'Verify that the out of band verifier rejects out of band authentication attempts after 10 minutes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.6', 'Verify that the out of band verifier authentication keys is only usable once, and only for the original authentication request.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.7', 'Verify that the authentication key is generated by a secure random number generator, containing at least 20 bits of entropy (typically a six digital random number is sufficient).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.7.8', 'Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric authenticators).', '999'); 

INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8', 'Single Factor OTP Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8.1', 'Verify that symmetric keys used to verify submitted codes is highly protected, such as using an HSM or OS based key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8.2', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8.3', 'Verify that time-based tokens have a defined lifetime before needing re-seeding or replacement.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8.4', 'Verify that time-based OTP can be used only once within the validity period.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.8.5', 'Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric OTP authenticators).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9', 'Multi-factor OTP Verifier Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.1', 'Verify that symmetric keys used to verify submitted codes is highly protected, such as using an HSM or OS based key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.2', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.3', 'Verify that MFA OTP device is a multi-factor device. Otherwise, the device should be treated as a single factor OTP device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.4', 'Verify that time-based OTPs have a defined lifetime before needing re-seeding or replacement.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.5', 'Verify that time-based OTP can be used only once within the validity period.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.6', 'Verify that if a time-based OTP is re-used during the validity period, a warning is presented to the claimant, and optionally the user or the existing session.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.9.7', 'Verify that rate limiting is in place if the authentication secret uses less than 64 bits of entropy (typically all numeric OTP authenticators).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.10', 'Cryptographic Software and Devices Verifier Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.10.1', 'Verify that cryptographic keys used in verification are stored securely and protected against disclosure, such as using a TPM or HSM, or an OS service that can use this secure storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.10.2', 'Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.10.3', 'Verify that approved cryptographic algorithms are used in the generation, seeding, and verification.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.11', 'Service Authentication Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.11.1', 'Integration secrets SHOULD NOT rely on unchanging passwords, such as API keys or shared privileged accounts. If passwords are required, the credential should not be a default account and stored with sufficient protection to prevent offline recovery attacks, including local system access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '2.11.2', 'Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware trusted platform module (TPM), or a hardware security module (L3) is recommended for password storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.0', 'Session Management Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.1', 'Fundamental Session Management Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.1.1', 'Verify that the session token is never disclosed in URLs, error messages, or logs. This includes verifying that the application does not support URL rewriting of session cookies.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2', 'Session Binding Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2.1', 'Verify that session tokens are created or generated after authentication, not before.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2.2', 'Verify that session tokens are created using approved cryptographic algorithms with at least 64 bits of entropy.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2.3', 'Verify that session tokens are not stored in insecure local storage, such as HTML 5 local storage.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.2.4', 'Verify that active session functionality exists, which allows users to either selectively or completely log out all active devices / sessions.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3', 'Session logout and timeout Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3.1', 'Verify that logout timeout invalidates or erases any client- or server-side session storage, such that the back button or a downstream relying party does not resume an authenticated session, including across relying parties.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3.2', 'Verify that absolute or idle timeouts invalidates or erases any client- or server-side session storage.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3.3', 'Verify if authenticators permit users to remain logged in, that re-authentication occurs periodically both when actively used or after an idle period.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.3.4', 'Verify that the user can terminate all other active sessions after a successful change password process, and this is effective across the application, federated login (if present) and any relying parties.', '263'); 
iNSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4', 'Session logout and timeout Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4.1', 'Verify that cookie-based session IDs have the "Secure" attribute.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4.2', 'Verify that cookie-based session IDs have the "HttpOnly" attributes.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4.3', 'Verify that cookie-based session IDs have minimum practical hostnames, domain and path attributes, along with the "SameSite" attribute.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.4.4', 'Verify that cookie-based session IDs are set to expire soon after the default session timeout period.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.5', 'Token based Session Management', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.5.1', 'Verify that OAuth and refresh tokens are not considered as the presence of the subscriber; this pertains to high-value transactions where re-authentication may be required to protect the user.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.5.2', 'Verify single factor unchanging API secrets, and keys are not used, except with legacy implementations.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.5.3', 'Verify that stateless session tokens enveloping sensitive session data are digitally signed or encrypted and regularly verified in a timely fashion to protect against tampering, enveloping, replay, null cipher and key substitution attacks.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.6', 'Re-authentication from a federation or assertion', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.6.1', 'Verify that relying parties specify the maximum authentication time to CSPs and that CSPs re-authenticate the subscriber if they have not used a session within that period.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.6.2', 'Verify that CSPs inform relying parties of the last authentication event, to allow RPs to determine if they need to re-authenticate the subscriber.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.7', 'Defences against session management exploits', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.7.1', 'Verify that all post-reset, post-registration, and post-authentication high value or adminstrative functionality verifies the user session is both fully logged in and has a valid post-authentication role before permitting any changes or transactions, especially in relation to user profile updates, password changes, MFA enrollment, and administrative functionality.', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '3.7', 'Defences against session management exploits', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.0', 'Access Control Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.1', 'Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege.', '126'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.4', 'Verify that sensitive data and APIs are protected against direct object attacks targeting creation, reading, updating and deletion of records.', '44'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.5', 'Verify that directory browsing is disabled unless deliberately desired. Additionally, applications should not allow discovery or disclosure of file or directory metadata, such as Thumbs.db, .DS_Store, .git or .svn folders.', '61'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.8', 'Verify that access controls fail securely.', '242'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.9', 'Verify that the same access control rules implied by the presentation layer are enforced on the server side.', '240'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.10', 'Verify that all user and data attributes and policy information used by access controls cannot be manipulated by end users unless specifically authorized.', '258'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.11', 'Verify that there is preferably only one vetted access control mechanism for protecting access to protected data and resources, such that hard coded access control checks are not required throughout the application.', '259'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.12', 'Verify that all access control decisions can be logged and all failed decisions are logged.', '232'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.13', 'Verify that the application or framework enforces a strong anti-CSRF mechanism to protect any sensitive functionality.', '5'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.14', 'Verify the application has sufficient anti-automation to detect and protect against data exfiltration, excessive business logic requests, or denial of service attacks.', '116'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.15', 'Verify the application has additional authorization (such as step up or adaptive authentication) for lower value systems, and / or segregation of duties for high value applications to enforce anti-fraud controls as per the risk of application and past fraud.', '111'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.16', 'Verify that access control policy is enforced server-side.', '241'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.17', 'Verify that data-level access control is implemented such that access to individual records can be managed in a centralized and standard way.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '4.18', 'Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.0', 'Validation, Sanitization and Encoding Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1', 'Input Validation Reqirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.1', 'Verify that server side input validation failures result in request rejection and are logged.', '95'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.2', 'Verify that input validation routines are enforced on the server side.', '108'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.3', 'VVerify that the application uses a centralized input validation control mechanism.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.4', 'Verify that all untrusted HTML input from WYSIWYG editors or similar is properly sanitized with an HTML sanitizer library or framework feature.', '180'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.5', 'Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, or environment variables).', '71'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.6', 'Verify that all input data is validated, not only HTML form fields but all sources of input such as REST calls, query parameters, HTTP headers, cookies, batch files, or RSS feeds; using positive validation (whitelisting), then lesser forms of validation such as greylisting (eliminating known bad strings), or rejecting bad inputs (blacklisting).', '167'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.7', 'Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length and pattern (e.g. credit card numbers or telephone, or validating that two related fields are reasonable, such as validating suburbs and zip or postcodes match).', '234'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.1.8', 'Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length, and characters potentially harmful in given context should be escaped (e.g. names with Unicode or apostrophes, such as ねこ).', '202'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2', 'Output Encoding Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.1', 'Verify that output encoding occurs close to or by the interpreter for which it is intended.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.2', 'Verify that output encoding is relevant for the interpreter and context required. For example, use encoders specifically for HTML values, attributes, URL Parameters, HTTP headers, SMTP, and others as the context requires.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.3', 'Verify that output encoding preserves the users chosen character set and locale, such that any Unicode character point is valid and safely handled.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.4', 'Verify that context-aware, preferably automated - or at worst, manual - output escaping protects against reflected, stored, and DOM based XSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.5', 'Verify that any user-supplied data included in the browsers DOM or web views protects against JavaScript code execution and XSS attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.2.6', 'Verify that where parameterized or safer mechanisms are not present, that context-specific output encoding is used to protect against injection attacks, such as the use of SQL escaping to protect against SQL injection.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3', 'Injection Prevention Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.1', 'Verify that data selection or database queries (e.g. SQL, HQL, ORM, NoSQL) use parameterized queries, ORMs, entity frameworks, or otherwise protected from database injection attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.2', 'Verify that LDAP queries are not susceptible to LDAP Injection by using either parameterized LDAP queries or the use of contextual LDAP output encoding.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.3', 'Verify that operating system calls are not susceptible to OS command injection by using either parameterized OS queries or the use of contextual command line output encoding.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.4', 'Verify that file and path handling is not susceptible to Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.5', 'Verify that XML parsing and queries are not susceptible to XPath injection or XML injection attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.6', 'Verify that where potentially untrusted data is copied one DOM context to another, the transfer uses safe JavaScript methods, such as using innerText or JQuery .val to ensure the application is not susceptible to DOM Cross-Site Scripting (XSS) attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.7', 'Verify that the application protects against SMTP or IMAP injection.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.8', 'Verify that the application protects against eval(), template injection, or remote code execution attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.9', 'Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.10', 'Verify that if the application uses a systems language or unmanaged code, it uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.11', 'Verify that if the application uses a systems language or unmanaged code, format strings do not take potentially hostile input, and are constant.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.12', 'Verify that if the application uses a systems language or unmanaged code, sign, range, and input validation techniques are used to prevent integer overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.3.13', 'Verify that if the application uses a systems language or unmanaged code, compiler flags are configured to enable all available buffer overflow protections and warnings, including stack randomization, data execution prevention, and to break the build if an unsafe pointer, memory, format string, integer, or string operations are found.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.4', 'Deserialization Prevention Requirements', '263');
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.4.1', 'Verify when parsing JSON in browsers or JavaScript-based backends, that JSON.parse is used to parse the JSON document. Do not use eval() to parse JSON.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.4.2', 'Verify that untrusted data, particularly filenames and URL input fields, use positive input validation and output encoding methods to protect against Server-Side Request Forgery (SSRF) vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.4.3', 'Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '5.4.4', 'Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.0', 'Cryptography at rest verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.2', 'Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable Padding Oracle attacks.', '149'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.6', 'Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module’s approved random number generator when these random values are intended to be not guessable by an attacker.', '118'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.7', 'Verify that cryptographic algorithms used by the application have been validated against FIPS 140-2 or an equivalent standard.', '119'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.11', 'Verify that consumers of cryptographic services do not have direct access to key material, such as by using key vaults or API based alternatives.', '196'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.12', 'Verify that Personally Identifiable Information (PII) and other sensitive data is stored encrypted while at rest.', '207'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.13', 'Verify that sensitive passwords or key material maintained in memory is overwritten with zeros as soon as it is no longer required, to mitigate memory dumping attacks.', '203'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.14', 'Verify that all keys and passwords are replaceable, and are generated or replaced at installation time.', '204'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.15', 'Verify that random numbers are created with proper entropy even when the application is under heavy load, or that the application degrades gracefully in such circumstances.', '205'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '7.16', 'Verify that industry proven cryptographic modules are used instead of custom coded cryptography.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.0', 'Error Handling and Logging Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.1', 'Verify that the application does not output error messages or stack traces containing sensitive data that could assist an attacker, including session id, software/framework versions and personal information.', '15'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.3', 'Verify that the application logs security relevant events including successful and failed authentication events, access control failures and input validation failures.', '83'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.4', 'Verify that each log event includes necessary information that would allow for a detailed investigation of the timeline when an event happens.', '99'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.5', 'Verify that all events that include untrusted data will not execute as code in the intended log viewing software.', '100'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.6', 'Verify that security logs are protected from unauthorized access and modification.', '257'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.7', 'Verify that the application does not log credentials, session tokens, payment instruments, or sensitive data, as defined under local privacy laws or relevant security policy.', '78'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.8', 'Verify the application appropriately encodes user supplied data to prevent log injection.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.12', 'Verify that logs are transmitted to a remote system for analysis, detection, alerting, and escalation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.13', 'Verify that time sources are synchronized to the correct time and time zone.', '210'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '8.14', 'Verify all authentication decisions are logged, without storing sensitive session identifiers or memorized secrets. This should include requests with relevant metadata needed for security investigations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.0', 'Data Protection Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.2', 'Identify all sensitive data created and processed by the application and ensure that a policy is in place on how to deal with sensitive data.', '261'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.3', 'Verify that sensitive data is sent to the server in the HTTP/S message body or headers and that all query string parameters from any HTTP verb does not contain sensitive data.', '72'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.4', 'Verify that the application sets sufficient anti-caching headers such that any sensitive and personal information displayed by the application or entered by the user should not be cached on disk by mainstream modern browsers (e.g. visit about:cache to review disk cache).', '19'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.5', 'Verify that on the server, all cached or temporary copies of sensitive data stored are protected from unauthorized access or purged/invalidated after the authorized user accesses the sensitive data.', '145'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.6', 'Verify that users have a method to remove or export their data on demand.', '135'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.7', 'Verify the application minimizes the number of parameters in a request, such as hidden fields, Ajax variables, cookies and header values.', '142'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.8', 'Verify the application has the ability to detect and alert on abnormal numbers of requests.', '125'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.9', 'Verify that data stored in client side storage (such as HTML5 local storage, session storage, IndexedDB, regular cookies or Flash cookies) does not contain sensitive data or PII.', '190'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.10', 'Verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required.', '235'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.11', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required, to mitigate memory dumping attacks.', '135'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.12', 'Verify that sensitive or private information that is required to be encrypted, is encrypted using approved algorithms that provides both confidentiality and integrity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.13', 'Verify that users are provided clear language regarding collection and use of supplied personal information and that users have provided opt in consent for the use of that data before it is used in any way.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '9.14', 'Verify that authenticated data is cleared from client storage, such as the browser DOM, after the client or session is terminated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.0', 'Communications security verification requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.1', 'Verify that a path can be built from a trusted CA to each Transport Layer Security (TLS) server certificate, and that each server certificate is valid.', '101'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.3', 'Verify that TLS is used for all connections (including for authentication, API or web service calls, backend, external, and partner connections), and does not fall back to insecure or unencrypted protocols.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.4', 'Verify that backend TLS connection failures are logged.', '103'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.5', 'Verify that certificate paths are built and verified for all client certificates using configured trust anchors and revocation information.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.6', 'Verify that all connections to external systems that involve sensitive information or functions are authenticated.', '84'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.11', 'Verify that HTTP Strict Transport Security headers are included on all requests and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains.', '192'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.12', 'Verify that the applications URL has been submitted to a preloaded list of Strict Transport Security domains maintained by web browser vendors.', '255'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.14', 'Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured.', '139'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.15', 'Verify that only strong algorithms, ciphers, and protocols are enabled, with the strongest algorithms and ciphers set as preferred, to provide both confidentiality and integrity.', '198'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '10.17', 'Verify that old versions of SSL and TLS protocols, algorithms, ciphers, and configuration are not used, such as SSLv2/3 or TLS 1.0. The latest version of TLS should be the preferred cipher suite.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.0', 'HTTP Security Configuration Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.1', 'Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.2', 'Verify that every HTTP response contains a content type header specifying a safe character set (e.g., UTF-8, ISO 8859-1).', '131'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.3', 'Verify that HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, are authenticated by the application.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.4', 'Verify that a suitable X-Frame-Options or Content-Security-Policy: frame-ancestors header is in use for sites where content should not be embedded in a 3rd party site.', '20'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.5', 'Verify that the HTTP headers or any part of the HTTP response do not expose detailed version information of system components.', '130'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.6', 'Verify that all API responses contain X-Content-Type-Options: nosniff and Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type).', '193'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.7', 'Verify that a content security policy (CSPv2) is in place that helps mitigate common DOM, XSS, JSON, and JavaScript injection vulnerabilities.', '178'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.8', 'Verify that the X-XSS-Protection: 1; mode=block header is in place to enable browser reflected XSS filters.', '21'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '11.9', 'Verify that the supplied Origin header is not used for authentication or access control decisions, as the Origin header can easily be changed by an attacker.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.0', 'Malicious Code Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.1', 'Verify all malicious activity is adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications.', '239'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.2', 'Verify that the application source code and third party libraries do not contain unauthorized phone home or data collection capabilities. Where such functionality exists, obtain the users permission for it to operate prior to collecting any data.', '105'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.3', 'Verify that the application does not execute external code from untrusted sources, such as loading code or libraries from the Internet post-installation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.4', 'Verify that if the application has an auto-update feature, updates should be obtained over secure channels and digitally signed. The update code must validate the digital signature of the update before installing or executing the update.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.5', 'Verify that the application source code and third party libraries do not contain back doors, such as hard-coded or additional undocumented accounts or keys, code obfuscation, undocumented binary blobs, root kits, or anti-debugging, insecure debugging features, or otherwise out of date, insecure, or hidden functionality that could be used maliciously if discovered.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.6', 'Verify that the application source code and third party libraries does not contain time bombs by searching for date and time related functions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.7', 'Verify that the application source code and third party libraries does not contain malicious code, such as salami attacks, logic bypasses, or logic bombs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '13.8', 'Verify that the application source code and third party libraries do not contain Easter eggs or any other potentially unwanted functionality.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.0', 'Business Logic Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.1', 'Verify the application will only process business logic flows for the same user in sequential step order and without skipping steps.', '110'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.2', 'Verify the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.', '125'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.3', 'Verify the application has appropriate limits for specific business actions or transactions which are correctly enforced on a per user basis.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.4', 'Verify the application monitors for unusual events or activity from a business logic perspective. For example, attempts to perform actions out of order or actions which a normal user would never attempt.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.5', 'Verify the application has configurable alerting when automated attacks or unusual activity is detected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.6', 'Verify the application has automated reactions when automated attacks or unusual activity is detected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '15.7', 'Verify the application has sufficient anti-automation controls to detect and protect against data exfiltration, excessive business logic requests, or denial of service attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.0', 'File and Resources Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.1', 'Verify that URL redirects and forwards only allow whitelisted destinations, or show a warning when redirecting to potentially untrusted content.', '67'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.2', 'Verify that untrusted file data submitted to the application is not used directly with file I/O commands, particularly to protect against vulnerabilities involving path traversal, local file include, file mime type, reflective file download, and OS command injection.', '225'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.3', 'Verify that files obtained from untrusted sources are validated to be of expected type and scanned by antivirus scanners to prevent upload of known malicious content.', '226'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.4', 'Verify that untrusted data is not used within inclusion, class loader, or reflection capabilities to prevent remote/local code execution vulnerabilities.', '250'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.5', 'Verify that untrusted data is not used within cross-domain resource sharing (CORS) to protect against arbitrary remote content.', '112'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.6', 'Verify that files obtained from untrusted sources are stored outside the web root, with limited permissions, preferably with strong validation.', '227'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.7', 'Verify that the web or application server is configured by default to deny access to remote resources or systems outside the web or application server.', '138'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.8', 'Verify that application code does not execute uploaded data obtained from untrusted sources.', '13'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.9', 'Verify that unsupported, insecure or deprecated client-side technologies are not used, such as NSAPI plugins, Flash, Shockwave, ActiveX, Silverlight, NACL, or client-side Java applets.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '16.10', 'Verify that the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header does not reflect the request origin header or support the "null" origin.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.0', 'API and Web Service Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.1', 'Verify that the same encoding is used between the client and the server.', '33'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.2', 'Verify that suitable generic error messages are returned when in production mode, so as to not leak sensitive debug information.', '187'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.3', 'Verify that access to administration and management functions within the Web Service Application is limited to web service administrators.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.4', 'Verify that XML or JSON schema is in place and verified before accepting input.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.5', 'Verify that all received input meets service type/length/range and format.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.6', 'Verify that all received input, before processed, is sanitised accordingly to ensure it is safe to handle.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.7', 'Verify that SOAP based web services are compliant with Web Services-Interoperability (WS-I) Basic Profile at minimum. This essentially means TLS encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.8', 'Verify that REST services are protected from Cross-Site Request Forgery via the use of at least one or more of the following: double submit cookie pattern, CSRF nonces, ORIGIN request header checks, and referrer request header checks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.9', 'Verify that REST services explicitly check the incoming Content-Type to be the expected one, such as application/xml or application/JSON.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.10', 'Verify that the message payload is signed to ensure reliable transport between client and service, using JSON Web Signing or WS-Security for SOAP requests.', '80'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.11', 'Verify that alternative and less secure access paths do not exist.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.12', 'If GraphQL is used, to prevent DoS as a result of expensive, nested queries, query whitelisting or a combination of depth limiting and amount limiting should be used. For more advanced scenarios, query cost analysis should be used.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.13', 'If GraphQL is used, authorization logic should be implemented at the business logic layer instead of the GraphQL layer.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.14', 'If no access control is present, verify that the REST service is not susceptible to excessive calls, which could lead to increased overhead or CPU/bandwidth bills. A potential solution could be API keys, or returning error code 429 "Too Many Requests" if requests are excessive.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.15', 'Verify that authorization decisions are made at both the URI and resource level, not just at the resource level.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.16', 'Verify that requests containing unexpected or missing content types are rejected with appropriate headers (HTTP response status 406 Unacceptable or 415 Unsupported Media Type).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '18.17', 'Verify that logging is performed for all security-related events.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.0', 'Configuration Verification Requirements', '263'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.1', 'Verify that all components are up to date with proper security configuration(s) and version(s). This should include removal of unneeded configurations and functionality, such as sample applications, platform documentation, and default or example users.', '14'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.2', 'Verify that communications between components, such as between the application server and the database server, are encrypted, particularly when the components are in different containers or on different systems.', '102'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.3', 'Verify that communications between components, such as between the application server and the database server, are authenticated using an account with the least necessary privileges.', '246'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.4', 'Verify application deployments are adequately sandboxed, containerized or isolated to delay and deter attackers from attacking other applications.', '106'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.5', 'Verify that the application build and deployment processes are performed in a secure and repeatable way, such as CI / CD automation and automated configuration management.', '199'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.6', 'Verify that authorized administrators have the capability to verify the integrity of all security-relevant configurations to detect tampering.', '237'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.7', 'Verify that all application components are signed with a suitable key (Digital Cert/CA).', '200'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.8', 'Verify that third party components come from pre-defined, trusted repositories.', '238'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.9', 'Verify that build processes for system-level languages have all security flags enabled, such as ASLR, DEP, and security checks.', '201'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.10', 'Verify that if application assets, such as JavaScript libraries, CSS stylesheets or web fonts, are hosted externally on a content delivery network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.11', 'Verify that all application components, services, and servers each use their own low-privilege service account, that is not shared between applications nor used by administrators.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.12', 'Verify that all parsers used by the application such as XML parsers are configured to prevent external entity attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (3, '19.13', 'Verify that the web tier is configured to serve only files with specific file extensions to prevent unintentional information and source code leakage. For example, .bak, .swp and and similar extensions commonly used by editors should not be served by the web tier.', '999'); 
---
--- MASVS lvl 1 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.1', 'All app components are identified and known to be needed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (4, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- MASVS lvl 2 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.6', 'Biometric authentication, if any, is not eventbound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.10', 'The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.9', 'Stepup authentication is required to enable actions that deal with sensitive data or transactions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.4', 'The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.8', 'A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '4.7', 'Sessions are terminated at the remote endpoint after a predefined period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.12', 'The app educates the user about the types of personally identifiable information processed, as well as security best practices the user should follow in using the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.10', 'All components that are not part of the application but that the application relies on to operate, are clearly identified and the security implications of using those components are known.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.7', 'A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.1', 'All app components are identified and known to be needed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.13', 'Security is addressed within all parts of the software development lifecycle.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.8', 'No sensitive data is included in backups generated by the mobile operating system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.9', 'All security controls have a centralized implementation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.11', 'The app enforces a minimum deviceaccesssecurity policy, such as requiring the user to set a device passcode.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.5', 'The app doesn''t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrolments and account recovery.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.10', 'The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.8', 'All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.9', 'The app removes sensitive data from views when backgrounded.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.12', 'Remote endpoints verify that connecting clients use an uptodate version of the mobile app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.11', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 80057.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (5, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- MASVS lvl 3 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.11', 'The app uses multiple functionally independent methods of emulator detection that, in context of the overall protection scheme, force adversaries to invest significant manual effort to run the app in an emulator (supersedes requirement 8.7).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.6', 'Biometric authentication, if any, is not eventbound (i.e. using an API that simply returns "true" or "false"). Instead, it is based on unlocking the keychain/keystore.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.7', 'The app implements multiple different responses to tampering, debugging and emulation, including stealthy responses that don''t simply terminate the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.0', 'Architecture, Design and Threat Modelling Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.3', 'The app uses cryptographic primitives that are appropriate for the particular usecase, configured with parameters that adhere to industry best practices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.0', 'Resiliency Against Reverse Engineering Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.1', 'The app implements two or more functionally independent methods of root detection and responds to the presence of a rooted device either by alerting the user or terminating the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.3', 'The remote endpoint terminates the existing session when the user logs out.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.3', 'The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a valid CA are accepted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.4', 'The app detects the presence of widely used reverse engineering tools, such as code injection tools, hooking frameworks and debugging servers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.8', 'Free security features offered by the toolchain, such as bytecode minification, stack protection, PIE support and automatic reference counting, are activated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.0', 'Platform Interaction Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.10', 'The app informs the user of all login activities with his or her account. Users are able view a list of devices used to access the account, and to block specific devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.5', 'The app detects, and response to, being run in an emulator using any method.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.9', 'Stepup authentication is required to enable actions that deal with sensitive data or transactions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.4', 'The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.10', 'The app implements a ''device binding'' functionality using a device fingerprint derived from multiple properties unique to the device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.5', 'The remote endpoint implements an exponential backoff, or temporarily locks the user account, when incorrect authentication credentials are submitted an excessive number of times .', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.6', 'All random values are generated using a sufficiently secure random number generator.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.0', 'Cryptography Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.1', 'Data is encrypted on the network using TLS. The secure channel is used consistently throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.5', 'The app doesn''t reuse the same cryptographic key for multiple purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.2', 'The TLS settings are in line with current best practices, or as close as possible if the mobile operating system does not support the recommended standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.4', 'A password policy exists and is enforced at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.9', 'Obfuscating transformations and functional defenses are interdependent and wellintegrated throughout the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.8', 'A second factor of authentication exists at the remote endpoint and the 2FA requirement is consistently enforced.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.1', 'If the app provides users with access to a remote service, an acceptable form of authentication such as username/password authentication is performed at the remote endpoint.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.0', 'Authentication and Session Management Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.6', 'The app detects, and responds to, modifications of process memory, such as relocation table patches and injected code.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.3', 'The app detects, and responds to, tampering with executable files and critical data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.0', 'Code Quality and Build Setting Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.2', 'The remote endpoint uses randomly generated access tokens toauthenticate client requests without sending the user''s credentials.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.13', 'If the architecture requires sensitive computations be performed on the clientside, these computations are isolated from the operating system by using a hardwarebased SE / TEE. Alternatively, the information is protected using obfuscation. Considering current published research, the obfuscation type and parameters are sufficient to cause significant manual effort for reverse engineers seeking to comprehend the sensitive portions of the code and/or data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.2', 'The app implements multiple functionally independent debugging defenses that, in context of the overall protection scheme, force adversaries to invest considerable manual effort to enable debugging. All available debugging protocols must be covered (e.g. JDWP and native).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.8', 'All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.4', 'The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '4.7', 'Sessions are terminated at the remote endpoint after a predefined period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.0', 'Data Storage and Privacy Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '8.12', 'If the architecture requires sensitive information be stored on the device, the app only runs on operating system versions and devices that offer hardwarebacked key storage. Alternatively, the information is protected using obfuscation. Considering current published research, the obfuscation type and parameters are sufficient to cause significant manual effort for reverse engineers seeking to comprehend or extract the sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.5', 'JavaScript is disabled in WebViews unless explicitly required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.5', 'Data considered sensitive in the context of the mobile app is clearly identified.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.2', 'The app uses proven implementations of cryptographic primitives.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.4', 'The keyboard cache is disabled on text inputs that process sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.5', 'The app catches and handles possible exceptions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.12', 'The app educates the user about the types of personally identifiable information processed, as well as security best practices the user should follow in using the app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.10', 'All components that are not part of the application but that the application relies on to operate, are clearly identified and the security implications of using those components are known.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.2', 'All third party components used by the mobile app, such as libraries and frameworks, are identified, and checked for known vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.7', 'A threat model for the mobile app and the associated remote services has been produced that identifies potential threats and countermeasures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.1', 'System credential storage facilities are used appropriately to store sensitive data, such as user credentials or cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.9', 'Object serialization, if any, is implemented using safe serialization APIs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.7', 'The app does not load usersupplied local resources into WebViews.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.1', 'All app components are identified and known to be needed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.1', 'The app only requests the minimum set of permissions necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.13', 'Security is addressed within all parts of the software development lifecycle.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.1', 'The app is signed and provisioned with valid certificate.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.8', 'No sensitive data is included in backups generated by the mobile operating system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.2', 'No sensitive data is written to application logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.7', 'In unmanaged code, memory is allocated, freed and used securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.6', 'All app components are defined in terms of the business functions and/or security functions they provide.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.10', 'The app detects whether it is being executed on a rooted or jailbroken device. Depending on the business requirement, users are warned, or the app is terminated if the device is rooted or jailbroken.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.6', 'No sensitive data is exposed via IPC mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.4', 'The app does not export sensitive functionality through IPC facilities, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.2', 'The app has been built in release mode, with settings appropriate for a release build (e.g. nondebuggable).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.9', 'All security controls have a centralized implementation.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.11', 'The app enforces a minimum deviceaccesssecurity policy, such as requiring the user to set a device passcode.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.5', 'The app doesn''t rely on a single insecure communication channel (email or SMS) for critical operations, such as enrolments and account recovery.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.10', 'The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.3', 'Debugging symbols have been removed from native binaries.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.8', 'All third party components have been assessed (associated risks) before being used or implemented. A process is in place to ensure that each time a security update for a third party component is published, the change is inspected and the risk evaluated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.7', 'No sensitive data, such as passwords and credit card numbers, is exposed through the user interface or leaks to screenshots.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.3', 'The app does not export sensitive functionality via custom URL schemes, unless these mechanisms are properly protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.6', 'Error handling logic in security controls denies access by default.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.9', 'The app removes sensitive data from views when backgrounded.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.3', 'No sensitive data is shared with third parties unless it is a necessary part of the architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.12', 'Remote endpoints verify that connecting clients use an uptodate version of the mobile app.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.2', 'All inputs from external sources and the user are validated and, if necessary, sanitized. This includes data received via the UI, IPC mechanisms such as intents, custom URLs, and network sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.8', 'If Java objects are exposed in a WebView, verify that the WebView only renders JavaScript contained within the app package.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.3', 'Security controls are never enforced only on the client side, but on the respective remote endpoints.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '5.0', 'Network Communication Requirements', '264'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.11', 'There is an explicit policy for how cryptographic keys (if any) are managed, and the lifecycle of cryptographic keys is enforced. Ideally, follow a key management standard such as NIST SP 80057.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '7.4', 'Debugging code has been removed, and the app does not log verbose errors or debugging messages.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '2.5', 'The clipboard is deactivated on text fields that may contain sensitive data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '3.1', 'The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '1.4', 'A highlevel architecture for the mobile app and all connected remote services has been defined and security has been addressed in that architecture.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (6, '6.6', 'WebViews are configured to allow only the minimum set of protocol handlers required (ideally, only https is supported). Potentially dangerous handlers, such as file, tel and appid, are disabled.', '999'); 
---
--- ASVS IoT lvl 1 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (7, '1.0', 'TBD', '92'); 
---
--- ASVS IoT lvl 2 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (8, '1.0', 'TBD', '92'); 
---
--- ASVS IoT lvl 3 ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.0', 'Internet of Things Verification Requirements', '92'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.1', 'Verify that application layer debugging interfaces such USB, UART, and other serial variants are disabled or protected by a complex password.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.2', 'Verify that cryptographic keys and certificats are unique to each individual device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.3', 'Verify that memory protection controls such as ASLR and DEP are enabled by the embedded/IoT operating system, if applicable.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.4', 'Verify that on-chip debugging interfaces such as JTAG or SWD are disabled or that available protection mechanism is enabled and configured appropriately.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.5', 'Verify that physical debug headers are not present on the device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.6', 'Verify that sensitive data is not stored unencrypted on the device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.7', 'Verify that ARM based processors make use of TrustZone and TEE (Trusted Execution Environment)', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.8', 'Verify that private keys and certificates are stored securely in a Secure Element, TPM, TEE (Trusted Execution Environment), or protected using strong cryptography.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.9', 'Verify that the firmware apps protect data-in-transit using transport layer security.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.10', 'Verify that the firmware apps validate the digital signature of server connections.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.11', 'Verify that wireless communications are mutually authenticated.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.12', 'Verify that wireless communications are sent over an encrypted channel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.13', 'Verify that any use of banned C functions are replaced with the appropriate safe equivalent functions.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.14', 'Verify that each firmware maintains a software bill of materials cataloging third-party components, versioning, and published vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.15', 'Verify all code including third-party binaries, libraries, frameworks are reviewed for hardcoded credentials (backdoors).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.16', 'Verify that the application and firmware components are not susceptible to OS Command Injection by invoking shell command wrappers, scripts, or that security controls prevent OS Command Injection.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.17', 'Verify that the firmware apps pin the digital signature to a trusted server(s).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.18', 'Verify the presence of physical tamper resistance and/or tamper detection features, including epoxy.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.19', 'Verify that identifying markings on chips have been removed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.20', 'Verify that any available Intellectual Property protection technologies provided by the chip manufacturer are enabled.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.21', 'Verify security controls are in place to hinder firmware reverse engineering (e.g., removal of verbose debugging symbols).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.22', 'Verify the device validates the boot image signature before loading.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.23', 'Verify that the firmware update process is not vulnerable to time-of-check vs time-of-use attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.24', 'Verify the device uses code signing and validates firmware upgrade files before installing.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.25', 'Verify that the device cannot be downgraded to old versions (anti-rollback) of valid firmware.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.26', 'Verify usage of cryptographically secure pseudo-random number generator on embedded device (e.g., using chip-provided random number generators).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.27', 'Verify that firmware has the abilityto perform automatic firmware updates upon a predefined schedule.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.28', 'Verify that the device wipes firmware and sensitive data upon detection of tampering or receipt of invalid message.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.29', 'Verify that only micro controllers that support disabling debugging interfaces (e.g. JTAG, SWD) are used.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.30', 'Verify that only micro controllers that provide substantial protection from de-capping and side channel attacks are used.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.31', 'Verify that sensitive traces are not exposed to outer layers of the printed circuit board.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.32', 'Verify that inter-chip communication is encrypted (e.g. Main board to daughter board commnucation).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.33', 'Verify the device uses code signing and validates code before execution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.34', 'Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.35', 'Verify that the firmware apps utilize kernel containers for isolation between apps.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.36', 'Verify that secure compiler flags such as -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap are configured for firmware builds.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (9, '20.37', 'Verify that micro controllers are configured with code protection (if applicable).', '999'); 
---
--- PCIDSS ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.0', 'Protect stored cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.5', 'Physically secure all media.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.1', 'Use strong cryptography and security protocols to safeguard sensitive cardholder data during transmission over open, public networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.2', 'Secure cryptographic key distribution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.7', 'Ensure that security policies and operational procedures for developing and maintaining secure systems and applications are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.5', 'Assign to an individual or team the information security management responsibilities: Monitor and control all access to data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.4', 'Configure system security parameters to prevent misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5', 'Documented change controls procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.4', 'Document and communicate authentication policies and procedures to all users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.3', 'Install perimeter firewalls between all wireless networks and the cardholder data environment, and configure these firewalls to deny or, if traffic is necessary for business purposes, permit only authorized traffic between the wireless environment and the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.3', 'Record the audit trail entry date and time for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.2', 'Maintain a written agreement that includes an acknowledgement that the service providers are responsible for the security of cardholder data the service providers possess or otherwise store, process or transmit on behalf of the customer, or to the extent that they could impact the security of the customers cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.5', 'Deploy a changedetection mechanism (for example, fileintegrity monitoring tools) to alert personnel to unauthorized modification (including changes, additions, and deletions) of critical system files, configuration files, or content files; and configure the software to perform critical file comparisons at least weekly.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.1.1', 'For wireless environments connected to the cardholder data environment or transmitting cardholder data, change ALL wireless vendor defaults at installation, including but not limited to default wireless encryption keys, passwords, and SNMP community strings.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.6', 'Upon completion of a significant change, all relevant PCI DSS requirements must be implemented on all new or changed systems and networks, and documentation updated as applicable.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.4', 'Remove/disable inactive user accounts within 90 days.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.2', 'Restrict access to cryptographic keys to the fewest number of custodians necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.1', 'Review security events at least daily.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2', 'Implement automated audit trails for all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.7', 'Implemented mitigation for crosssite scripting (XSS).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.3', 'Designate specific personnel to be available on a 24/7 basis to respond to alerts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.2', 'Develop procedures to easily distinguish between onsite personnel and visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.3', 'Perform internal and external scans, and rescans as needed, after any significant change. Scans must be performed by qualified personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.2', 'Ensure that all system components and software are protected from known vulnerabilities by installing applicable vendorsupplied security patches. Install critical security patches within one month of release.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.1', 'Do not store the full contents of any track (from the magnetic stripe located on the back of a card, equivalent data contained on a chip, or elsewhere) after authorization. This data is alternatively called full track, track, track 1, track 2, and magneticstripe data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.6', 'Documentation of business justification and approval for use of all services, protocols, and ports allowed, including documentation of security features implemented for those protocols considered to be insecure..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1', 'Define and implement policies and procedures to ensure proper user identification management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.0', 'Install and maintain a firewall configuration to protect cardholder data', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.4', 'Ensure that the security policy and procedures clearly define information security responsibilities for all personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.3', 'Passwords/passphrases are strong and not weak.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.1', 'Coverage of all system component.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.4.1', 'If disk encryption is used (rather than file or columnlevel database encryption), logical access must be managed separately and independently of native operating system authentication and access control mechanisms (for example, by not using local user account databases or general network login credentials). Decryption keys must not be associated with user accounts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.4', 'A method to accurately and readily determine owner, contact information, and purpose (for example, labeling, coding, and/or inventorying of devices).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.2', 'Review logs of all other system components periodically based on the organization?s policies and risk management strategy, as determined by the organization?s annual risk assessment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.2', 'Ensure that all antivirus mechanisms are maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2', 'Develop configuration standards for all system components. Assure that these standards address all known security vulnerabilities and are consistent with industryaccepted system hardening standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.4', 'If segmentation is used to isolate the CDE from other networks, perform penetration tests at least annually and after any changes to segmentation controls/methods to verify that the segmentation methods are operational and effective, and isolate all outofscope systems from systems in the CDE.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.5', 'Create audit logs for all use of and changes to identification and authentication mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3.2', 'Review custom code prior to release to production or customers in order to identify any potential coding vulnerability (using either manual or automated processes).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5', 'Secure audit trails so they cannot be altered.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.4.1', 'Additional requirement for service providers only: Executive management shall establish responsibility for the protection of cardholder data and a PCI DSS compliance program.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.2', 'Verify user identity before modifying any authentication credential for example, performing password resets, provisioning new tokens, or generating new keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.3', 'Current diagram that shows all cardholder data flows across systems and networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.3', 'Immediately revoke access for any terminated users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.6', 'All high risk vulnerabilities identified in the vulnerability identification process (as defined in PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.5', 'Include alerts from security monitoring systems, including but not limited to intrusiondetection, intrusionprevention, firewalls, and fileintegrity monitoring systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10', 'Implement an incident response plan. Be prepared to respond immediately to a system breach.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.1', 'Visitors are authorized before entering, and escorted at all times within, areas where cardholder data is processed or maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.5', 'Permit only established connections into the network.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.6', 'Record the audit trail entry identity or name of affected data, system component, or resource for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3', 'Secure all individual nonconsole administrative access and all remote access to the CDE using multifactor authentication.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.2', 'Secure and synchronize router configuration files.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.2', 'Separation of duties between development/test and production environments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.0', 'Regularly test security systems and processes.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.4', 'Assign to an individual or team the information security management responsibilities: Administer user accounts, including additions, deletions, and modifications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.4', 'Maintain an inventory of system components that are in scope for PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.1', 'Generation of strong cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.0', 'Maintain a policy that addresses information security for all personnel.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.2', 'Implement a riskassessment process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.1.1', 'Ensure wireless networks transmitting cardholder data or connected to the cardholder data environment, use industry best practices to implement strong encryption for authentication and transmission.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.9', 'Ensure that security policies and operational procedures for monitoring all access to network resources and cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.5.1', 'Store media backups in a secure location, preferably an offsite facility, such as an alternate or backup site, or a commercial storage facility. Review the location''s security at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8.2', 'Render cardholder data on electronic media unrecoverable so that cardholder data cannot be reconstructed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.3', 'Visitors are asked to surrender the badge or identification before leaving the facility or at the date of expiration.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1.1', 'Maintain an inventory of authorized wireless access points including a documented business justification.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.2', 'Periodically inspect device surfaces to detect tampering (for example, addition of card skimmers to devices), or substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.4', 'Cryptographic key changes for keys that have reached the end of their cryptoperiod (for example, after a defined period of time has passed and/or after a certain amount of ciphertext has been produced by a given key), as defined by the associated application vendor or key owner, and based on industry best practices and guidelines (for example, NIST Special Publication 80057).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.10', 'Implemented mitigation for broken authentication and session management.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.5.1', 'Implement a process to respond to any alerts generated by the changedetection solution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.2', 'Time data is protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.7', 'Ensure that security policies and operational procedures for protecting stored cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.2', 'Documented change approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.7', 'Maintain strict control over the storage and accessibility of media.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6.1', 'Educate personnel upon hire and at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.2', 'Enable only necessary services, protocols, daemons, etc., as required for the function of the system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1.1', 'Ensure that antivirus programs are capable of detecting, removing, and protecting against all known types of malicious software.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.1', 'Record the audit trail entry user identification for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.5.1', 'Additional requirement for service providers only: Service providers with remote access to customer premises (for example, for support of POS systems or servers) must use a unique authentication credential (such as a password/phrase) for each customer.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.2', 'Authentication for use of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.4', 'Require documented approval by authorized parties specifying required privileges.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.1', 'Implement a DMZ to limit inbound traffic to only system components that provide authorized publicly accessible services, protocols, and ports.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.1', 'Implemented mitigation for injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.4', 'Maintain a program to monitor service providers? PCI DSS compliance status at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.5', 'Use fileintegrity monitoring or changedetection software on logs to ensure that existing log data cannot be changed without generating alerts (although new data being added should not cause an alert).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.6', 'Limit repeated access attempts by locking out the user ID after not more than six attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1', 'Establish and implement firewall and router configuration standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.2', 'Implement physical and/or logical controls to restrict access to publicly accessible network jacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.1', 'Perform external penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.2', 'Create audit logs for all actions taken by any individual with root or administrative privilege.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.3', 'Do not store the personal identification number (PIN) or the encrypted PIN block after authorization.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.3', 'Ensure that security policies and operational procedures for restricting access to cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.9', 'Activation of remoteaccess technologies for vendors and business partners only when needed by vendors and business partners, with immediate deactivation after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.4', 'Ensure that security policies and operational procedures for protecting systems against malware are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.3', 'Default denyall setting.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.3', 'Mask PAN when displayed (the first six and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the first six/last four digits of the PAN.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.6', 'Acceptable network locations for the technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.3', 'Create audit logs for all access to all audit trails.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.2', 'Perform internal penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.1', 'Use either video cameras or access control mechanisms (or both) to monitor individual physical access to sensitive areas. Review collected data and correlate with other entries. Store for at least three months, unless otherwise restricted by law.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2', 'In addition to assigning a unique ID, ensure proper userauthentication management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.0', 'Protect all systems against malware and regularly update antivirus software or program.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.1', 'A formal process for approving and testing all network connections and changes to the firewall and router configurations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.2', 'Protect audit trail files from unauthorized modifications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.5', 'Maintain information about which PCI DSS requirements are managed by each service provider, and which are managed by the entity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.7', 'Do not disclose private IP addresses and routing information to unauthorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.4', 'Implemented mitigation for insecure communications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.11', 'Additional requirement for service providers only: Perform reviews at least quarterly to confirm personnel are following security policies and operational procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.0', 'Restrict physical access to cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.5', 'Do not allow an individual to submit a new password/passphrase that is the same as any of the last four passwords/passphrases he or she has used.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2', 'Build firewall and router configurations that restrict connections between untrusted networks and any system components in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.7', 'Prevention of unauthorized substitution of cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.1', 'Critical systems have the correct and consistent time.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.0', 'Develop and maintain secure systems and application.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.1', 'Perform quarterly internal vulnerability scans. Address vulnerabilities and perform rescans to verify all high risk vulnerabilities are resolved in accordance with the entity''s vulnerability ranking (per Requirement 6.1). Scans must be performed by qualified personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.2', 'Assign to an individual or team the information security management responsibilities: Monitor and analyze security alerts and information, and distribute to appropriate personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.6', 'Shared hosting providers must protect each entity?s hosted environment and cardholder data. These providers must meet specific requirements as detailed in Appendix A1: Additional PCI DSS Requirements for Shared Hosting Providers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4', 'Follow change control processes and procedures for all changes to system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.3', 'Ensure that security policies and operational procedures for encrypting transmissions of cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.1', 'Define access needs for each role.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.4', 'Do not allow unauthorized outbound traffic from the cardholder data environment to the Internet.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.4', 'Store cryptographic keys in the fewest possible locations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.6', 'Where other authentication mechanisms are used (for example, physical or logical security tokens, smart cards, certificates, etc.), use of these mechanisms must be assigned.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.1', 'Explicit approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8', 'Destroy media when it is no longer needed for business or legal reasons.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.3', 'Functionality testing to verify that the change does not adversely impact the security of the system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.8', 'Additional requirement for service providers only: Implement a process for the timely detection and reporting of failures of critical security control systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.1', 'Classify media so the sensitivity of the data can be determined.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8', 'Maintain and implement policies and procedures to manage service providers with whom cardholder data is shared, or that could affect the security of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.7', 'All access to any database containing cardholder data (including access by applications, administrators, and all other users) is restricted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3', 'Develop usage policies for critical technologies and define proper use of these technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.2', 'Restrict access to privileged user IDs to least privileges necessary to perform job responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.3', 'Implement antispoofing measures to detect and block forged source IP addresses from entering the network. (For example, block traffic originating from the Internet with an internal source address..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.3', 'Store secret and private keys used to encrypt/decrypt cardholder data in one (or more) of the following forms at all times.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.4', 'Backout procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.7.1', 'Properly maintain inventory logs of all media and conduct media inventories at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.7', 'Retain audit trail history for at least one year, with a minimum of three months immediately available for analysis (for example, online, archived, or restorable from backup).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.2', 'Send the media by secured courier or other delivery method that can be accurately tracked.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.7', 'Screen potential personnel prior to hire to minimize the risk of attacks from internal sources. (Examples of background checks include previous employment history, criminal record, credit history, and reference checks..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.7', 'Requirement to review firewall and router rule sets at least every six months.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.6', 'If manual cleartext cryptographic keymanagement operations are used, these operations must be managed using split knowledge and dual control.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.6', 'Set passwords/passphrases for firsttime use and upon reset to a unique value for each user, and change immediately after the first use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4', 'Using timesynchronization technology, synchronize all critical system clocks and times and ensure that the following is implemented for acquiring, distributing, and storing time.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.5', 'Ensure that security policies and operational procedures for managing vendor defaults and other security parameters are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2', 'Run internal and external network vulnerability scans at least quarterly and after any significant change in the network (such as new system component installations, changes in network topology, firewall rule modifications, product upgrades).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.1', 'Assign to an individual or team the following information security management responsibilities: * Establish, document, and distribute security policies and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.10', 'Ensure that security policies and operational procedures for restricting physical access to cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.1', 'Separate development/test environments from production environments, and enforce the separation with access controls.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.2', 'Current network diagram that identifies all connections between the cardholder data environment and other networks, including any wireless networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.8', 'If a session has been idle for more than 15 minutes, require the user to reauthenticate to reactivate the terminal or session.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.3', 'Promptly back up audit trail files to a centralized log server or media that is difficult to alter.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.4', 'Install personal firewall software or equivalent functionality on any portable computing devices (including company and/or employeeowned) that connect to the Internet when outside the network (for example, laptops used by employees), and which are also used to access the CDE.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.9', 'Additional requirement for service providers only: Service providers acknowledge in writing to customers that they are responsible for the security of cardholder data the service provider possesses.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.6', 'Develop a process to modify and evolve the incident response plan according to lessons learned and to incorporate industry developments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.3', 'Implemented mitigation for insecure cryptographic storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.3', 'Ensure that antivirus mechanisms are actively running and cannot be disabled or altered by users, unless specifically authorized by management on a casebycase basis for a limited time period.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.7', 'List of companyapproved products.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.2', 'Assignment of privileges to individuals based on job classification and function.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.4', 'Render PAN unreadable anywhere it is stored (including on portable digital media, backup media, and in logs)', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.4', 'Create audit logs for all invalid logical access attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.3', 'Exploitable vulnerabilities found during penetration testing are corrected and testing is repeated to verify the corrections.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1', 'Use appropriate facility entry controls to limit and monitor physical access to systems in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.3', 'Restrict physical access to wireless access points, gateways, handheld devices, networking/communications hardware, and telecommunication lines.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3', 'Implement a methodology for penetration testing.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.1', 'Create audit logs for all individual user accesses to cardholder dat.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.8', 'Automatic disconnect of sessions for remoteaccess technologies after a specific period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.2', 'Do not store the card verification code or value (threedigit or fourdigit number printed on the front or back of a payment card used to verify cardnotpresent transactions) after authorization.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.1', 'Establish a process to identify security vulnerabilities, using reputable outside sources for security vulnerability information, and assign a risk ranking (for example, as high, medium or low) to newly discovered security vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.2', 'Implemented mitigation for buffer overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.5', 'Ensure that security policies and operational procedures for managing firewalls are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.3', 'Ensure there is an established process for engaging service providers including proper due diligence prior to engagement.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.4', 'Write logs for externalfacing technologies onto a secure, centralized, internal log server or media device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.0', 'Do not use vendorsupplied defaults for system passwords and other security parameter.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.7', 'Set the lockout duration to a minimum of 30 minutes or until an administrator enables the user ID.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.1', 'Documentation of impact.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.3', 'Implement additional security features for any required services, protocols, or daemons that are considered to be insecure..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.3', 'Ensure management approves any and all media that is moved from a secured area (including when media is distributed to individuals).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6.2', 'Require personnel to acknowledge at least annually that they have read and understood the security policy and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.2', 'Record the audit trail entry type of event for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1', 'Deploy antivirus software on all systems commonly affected by malicious software (particularly personal computers and servers).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.3', 'Assign access based on individual personnel''s job classification and function.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.2', 'Limit inbound Internet traffic to IP addresses within the DMZ.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.5', 'Do not use group, shared, or generic IDs, passwords, or other authentication methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.3', 'A list of all such devices and personnel with access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.2', 'Visitors are identified and given a badge or other identification that expires and that visibly distinguishes the visitors from onsite personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1.2', 'Implement incident response procedures in the event unauthorized wireless access points are detected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.1', 'Keep cardholder data storage to a minimum by implementing data retention and disposal policies, procedures and processes that include at least the following for all cardholder data (CHD) storage: . Limiting data storage amount and retention time to that which is required for legal, regulatory, and/or business requirements . Specific retention requirements for cardholder data . Processes for secure deletion of data when no longer needed . A quarterly process for identifying and securely deleting stored cardholder data that exceeds defined retention.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.3', 'Provide training for personnel to be aware of attempted tampering or replacement of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.6', 'Ensure that security policies and operational procedures for security monitoring and testing are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.5', 'Retirement or replacement (for example, archiving, destruction, and/or revocation) of keys as deemed necessary when the integrity of the key has been weakened (for example, departure of an employee with knowledge of a cleartext key component), or keys are suspected of being compromised.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.9', 'Implemented mitigation for crosssite request forgery (CSRF).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.8', 'Requirement for cryptographic key custodians to formally acknowledge that they understand and accept their keycustodian responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.3', 'Time settings are received from industryaccepted time sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.1.1', 'Review the security policy at least annually and update the policy when the environment changes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1', 'Limit access to system components and cardholder data to only those individuals whose job requires such access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6', 'Fully document and implement all keymanagement processes and procedures for cryptographic keys used for encryption of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.2', 'Never send unprotected PANs by enduser messaging technologies (for example, email, instant messaging, SMS, chat, etc.).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.8.1', 'Additional requirement for service providers only: Respond to failures of any critical security controls in a timely manner.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6', 'Maintain strict control over the internal or external distribution of any kind of media, including the following.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8.1', 'Shred, incinerate, or pulp hardcopy materials so that cardholder data cannot be reconstructed. Secure storage containers used for materials that are to be destroyed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.5', 'Record the audit trail entry origination of event for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.1', 'Restrict inbound and outbound traffic to that which is necessary for the cardholder data environment, and specifically deny all other traffic.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3.1', 'Incorporate multifactor authentication for all nonconsole access into the CDE for personnel with administrative access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.3', 'Production data (live PANs) are not used for testing or development.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.3', 'Encrypt all nonconsole administrative access using strong cryptography.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.3', 'Assign to an individual or team the information security management responsibilities: Establish, document, and distribute security incident response and escalation procedures to ensure timely and effective handling of all situations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.1', 'Limit viewing of audit trails to those with a jobrelated need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.0', 'Identify and authenticate access to system component.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3.1', 'Remove development, test and/or custom application accounts, user IDs, and passwords before applications become active or are released to customers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.4', 'Requirements for a firewall at each Internet connection and between any demilitarized zone (DMZ) and the internal network zone.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.2', 'Control addition, deletion, and modification of user IDs, credentials, and other identifier objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.1', 'Using strong cryptography, render all authentication credentials (such as passwords/phrases) unreadable during transmission and storage on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.4', 'Provide appropriate training to staff with security breach response responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.5', 'Implemented mitigation for improper error handling.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.6', 'Place system components that store cardholder data (such as a database) in an internal network zone, segregated from the DMZ and other untrusted networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.1', 'Create the incident response plan to be implemented in the event of system breach.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4', 'Implement procedures to identify and authorize visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.5', 'Acceptable uses of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2', 'Establish an access control system(s) for systems components that restricts access based on a user''s need to know, and is set to deny all unless specifically allowed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5', 'Document and implement procedures to protect keys used to secure stored cardholder data against disclosure and misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1.2', 'For systems considered to be not commonly affected by malicious software, perform periodic evaluations to identify and evaluate evolving malware threats in order to confirm whether such systems continue to not require antivirus software.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.3', 'Follow up exceptions and anomalies identified during the review process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.4.1', 'Additional requirement for service providers only: If segmentation is used, confirm PCI DSS scope by performing penetration testing on segmentation controls at least every six months and after any changes to segmentation controls/methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.8', 'Ensure that security policies and operational procedures for identification and authentication are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.1', 'Implement only one primary function per server to prevent functions that require different security levels from coexisting on the same server. (For example, web servers, database servers, and DNS should be implemented on separate servers..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.6', 'Create audit logs for all initialization, stopping, or pausing of the audit logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.8', 'Implemented mitigation for improper access control (such as insecure direct object references, failure to restrict URL access, directory traversal, and failure to restrict user access to functions).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.1', 'Implement audit trails to link all access to system components to each individual user.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.2', 'Review and test the plan, including all elements listed in Requirement 12.10.1, at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.3', 'Control physical access for onsite personnel to sensitive areas.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.2', 'Perform quarterly external vulnerability scans, via an Approved Scanning Vendor (ASV) approved by the Payment Card Industry Security Standards Council (PCI SSC). Perform rescans as needed, until passing scans are achieved.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3', 'Develop internal and external software applications (including webbased administrative access to applications) securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.10', 'For personnel accessing cardholder data via remoteaccess technologies, prohibit the copying, moving, and storage of cardholder data onto local hard drives and removable electronic media, unless explicitly authorized for a defined business need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.4', 'Change user passwords/passphrases at least once every 90 days..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2', 'Do not store sensitive authentication data after authorization (even if encrypted). If sensitive authentication data is received, render all data unrecoverable upon completion of the authorization process. It is permissible for issuers and companies that support issuing services to store sensitive authentication data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.5', 'Description of groups, roles, and responsibilities for management of network components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.1', 'Assign all users a unique ID before allowing them to access system components or cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.1', 'Always change vendorsupplied defaults and remove or disable unnecessary default accounts before installing a system on the network. This applies to ALL default passwords, including but not limited to those used by operating systems, software that provides security services, application and system accounts, pointofsale (POS) terminals, payment applications, Simple Network Management Protocol (SNMP) community strings, etc.).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.1', 'Maintain a list of service providers including a description of the service provided.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.4', 'Use intrusiondetection and/or intrusionprevention techniques to detect and/or prevent intrusions into the network. Monitor all traffic at the perimeter of the cardholder data environment as well as at critical points in the cardholder data environment, and alert personnel to suspected compromises. Keep all intrusiondetection and prevention engines, baselines, and signatures up to date.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.7', 'Create audit logs for all creation and deletion of systemlevel objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5', 'Address common coding vulnerabilities in softwaredevelopment processes as follows: * Train developers at least annually in uptodate secure coding techniques, including how to avoid common coding vulnerabilities. * Develop applications based on secure coding guidelines.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.1', 'Additional requirement for service providers only: Maintain a documented description of the cryptographic architecture', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.5', 'Manage IDs used by third parties to access, support, or maintain system components via remote access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.0', 'Track and monitor all access to network resources and cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6', 'Review logs and security events for all system components to identify anomalies or suspicious activity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.5', 'Remove all unnecessary functionality, such as scripts, drivers, features, subsystems, file systems, and unnecessary web servers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6', 'Implement a formal security awareness program to make all personnel aware of the cardholder data security policy and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.4', 'Removal of test data and accounts from system components before the system becomes active / goes into production.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3', 'Prohibit direct public access between the Internet and any system component in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3.2', 'Incorporate multifactor authentication for all remote network access (both user and administrator, and including thirdparty access for support or maintenance) originating from outside the entity''s network.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.4', 'Record the audit trail entry success or failure indication for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.1', 'Maintain an uptodate list of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.4', 'A visitor log is used to maintain a physical audit trail of visitor activity to the facility as well as computer rooms and data centers where cardholder data is stored or transmitted. Document the visitors name, the firm represented, and the onsite personnel authorizing physical access on the log. Retain this log for a minimum of three months, unless otherwise restricted by law.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1', 'Implement processes to test for the presence of wireless access points (802.11), and detect and identify all authorized and unauthorized wireless access points on a quarterly basis.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.0', 'Encrypt transmission of cardholder data across open, public network.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.1', 'Establish, publish, maintain, and disseminate a security policy.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.3', 'Secure cryptographic key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.6', 'For publicfacing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.0', 'Restrict access to cardholder data by business need to kno.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9', 'Protect devices that capture payment card data via direct physical interaction with the card from tampering and substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.0', 'Protect stored cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.5', 'Physically secure all media.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.1', 'Use strong cryptography and security protocols to safeguard sensitive cardholder data during transmission over open, public networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.2', 'Secure cryptographic key distribution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.7', 'Ensure that security policies and operational procedures for developing and maintaining secure systems and applications are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.5', 'Assign to an individual or team the information security management responsibilities: Monitor and control all access to data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.4', 'Configure system security parameters to prevent misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5', 'Documented change controls procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.4', 'Document and communicate authentication policies and procedures to all users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.3', 'Install perimeter firewalls between all wireless networks and the cardholder data environment, and configure these firewalls to deny or, if traffic is necessary for business purposes, permit only authorized traffic between the wireless environment and the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.3', 'Record the audit trail entry date and time for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.2', 'Maintain a written agreement that includes an acknowledgement that the service providers are responsible for the security of cardholder data the service providers possess or otherwise store, process or transmit on behalf of the customer, or to the extent that they could impact the security of the customers cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.5', 'Deploy a changedetection mechanism (for example, fileintegrity monitoring tools) to alert personnel to unauthorized modification (including changes, additions, and deletions) of critical system files, configuration files, or content files; and configure the software to perform critical file comparisons at least weekly.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.1.1', 'For wireless environments connected to the cardholder data environment or transmitting cardholder data, change ALL wireless vendor defaults at installation, including but not limited to default wireless encryption keys, passwords, and SNMP community strings.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.6', 'Upon completion of a significant change, all relevant PCI DSS requirements must be implemented on all new or changed systems and networks, and documentation updated as applicable.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.4', 'Remove/disable inactive user accounts within 90 days.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.2', 'Restrict access to cryptographic keys to the fewest number of custodians necessary.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.1', 'Review security events at least daily.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2', 'Implement automated audit trails for all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.7', 'Implemented mitigation for crosssite scripting (XSS).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.3', 'Designate specific personnel to be available on a 24/7 basis to respond to alerts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.2', 'Develop procedures to easily distinguish between onsite personnel and visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.3', 'Perform internal and external scans, and rescans as needed, after any significant change. Scans must be performed by qualified personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.2', 'Ensure that all system components and software are protected from known vulnerabilities by installing applicable vendorsupplied security patches. Install critical security patches within one month of release.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.1', 'Do not store the full contents of any track (from the magnetic stripe located on the back of a card, equivalent data contained on a chip, or elsewhere) after authorization. This data is alternatively called full track, track, track 1, track 2, and magneticstripe data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.6', 'Documentation of business justification and approval for use of all services, protocols, and ports allowed, including documentation of security features implemented for those protocols considered to be insecure..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1', 'Define and implement policies and procedures to ensure proper user identification management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.0', 'Install and maintain a firewall configuration to protect cardholder data', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.4', 'Ensure that the security policy and procedures clearly define information security responsibilities for all personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.3', 'Passwords/passphrases are strong and not weak.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.1', 'Coverage of all system component.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.4.1', 'If disk encryption is used (rather than file or columnlevel database encryption), logical access must be managed separately and independently of native operating system authentication and access control mechanisms (for example, by not using local user account databases or general network login credentials). Decryption keys must not be associated with user accounts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.4', 'A method to accurately and readily determine owner, contact information, and purpose (for example, labeling, coding, and/or inventorying of devices).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.2', 'Review logs of all other system components periodically based on the organization?s policies and risk management strategy, as determined by the organization?s annual risk assessment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.2', 'Ensure that all antivirus mechanisms are maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2', 'Develop configuration standards for all system components. Assure that these standards address all known security vulnerabilities and are consistent with industryaccepted system hardening standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.4', 'If segmentation is used to isolate the CDE from other networks, perform penetration tests at least annually and after any changes to segmentation controls/methods to verify that the segmentation methods are operational and effective, and isolate all outofscope systems from systems in the CDE.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.5', 'Create audit logs for all use of and changes to identification and authentication mechanisms.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3.2', 'Review custom code prior to release to production or customers in order to identify any potential coding vulnerability (using either manual or automated processes).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5', 'Secure audit trails so they cannot be altered.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.4.1', 'Additional requirement for service providers only: Executive management shall establish responsibility for the protection of cardholder data and a PCI DSS compliance program.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.2', 'Verify user identity before modifying any authentication credential for example, performing password resets, provisioning new tokens, or generating new keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.3', 'Current diagram that shows all cardholder data flows across systems and networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.3', 'Immediately revoke access for any terminated users.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.6', 'All high risk vulnerabilities identified in the vulnerability identification process (as defined in PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.5', 'Include alerts from security monitoring systems, including but not limited to intrusiondetection, intrusionprevention, firewalls, and fileintegrity monitoring systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10', 'Implement an incident response plan. Be prepared to respond immediately to a system breach.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.1', 'Visitors are authorized before entering, and escorted at all times within, areas where cardholder data is processed or maintained.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.5', 'Permit only established connections into the network.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.6', 'Record the audit trail entry identity or name of affected data, system component, or resource for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3', 'Secure all individual nonconsole administrative access and all remote access to the CDE using multifactor authentication.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.2', 'Secure and synchronize router configuration files.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.2', 'Separation of duties between development/test and production environments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.0', 'Regularly test security systems and processes.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.4', 'Assign to an individual or team the information security management responsibilities: Administer user accounts, including additions, deletions, and modifications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.4', 'Maintain an inventory of system components that are in scope for PCI DSS.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.1', 'Generation of strong cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.0', 'Maintain a policy that addresses information security for all personnel.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.2', 'Implement a riskassessment process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.1.1', 'Ensure wireless networks transmitting cardholder data or connected to the cardholder data environment, use industry best practices to implement strong encryption for authentication and transmission.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.9', 'Ensure that security policies and operational procedures for monitoring all access to network resources and cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.5.1', 'Store media backups in a secure location, preferably an offsite facility, such as an alternate or backup site, or a commercial storage facility. Review the location''s security at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8.2', 'Render cardholder data on electronic media unrecoverable so that cardholder data cannot be reconstructed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.3', 'Visitors are asked to surrender the badge or identification before leaving the facility or at the date of expiration.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1.1', 'Maintain an inventory of authorized wireless access points including a documented business justification.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.2', 'Periodically inspect device surfaces to detect tampering (for example, addition of card skimmers to devices), or substitution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.4', 'Cryptographic key changes for keys that have reached the end of their cryptoperiod (for example, after a defined period of time has passed and/or after a certain amount of ciphertext has been produced by a given key), as defined by the associated application vendor or key owner, and based on industry best practices and guidelines (for example, NIST Special Publication 80057).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.10', 'Implemented mitigation for broken authentication and session management.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.5.1', 'Implement a process to respond to any alerts generated by the changedetection solution.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.2', 'Time data is protected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.7', 'Ensure that security policies and operational procedures for protecting stored cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.2', 'Documented change approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.7', 'Maintain strict control over the storage and accessibility of media.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6.1', 'Educate personnel upon hire and at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.2', 'Enable only necessary services, protocols, daemons, etc., as required for the function of the system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1.1', 'Ensure that antivirus programs are capable of detecting, removing, and protecting against all known types of malicious software.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.1', 'Record the audit trail entry user identification for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.5.1', 'Additional requirement for service providers only: Service providers with remote access to customer premises (for example, for support of POS systems or servers) must use a unique authentication credential (such as a password/phrase) for each customer.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.2', 'Authentication for use of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.4', 'Require documented approval by authorized parties specifying required privileges.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.1', 'Implement a DMZ to limit inbound traffic to only system components that provide authorized publicly accessible services, protocols, and ports.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.1', 'Implemented mitigation for injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.4', 'Maintain a program to monitor service providers? PCI DSS compliance status at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.5', 'Use fileintegrity monitoring or changedetection software on logs to ensure that existing log data cannot be changed without generating alerts (although new data being added should not cause an alert).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.6', 'Limit repeated access attempts by locking out the user ID after not more than six attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1', 'Establish and implement firewall and router configuration standards.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.2', 'Implement physical and/or logical controls to restrict access to publicly accessible network jacks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.1', 'Perform external penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.2', 'Create audit logs for all actions taken by any individual with root or administrative privilege.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.3', 'Do not store the personal identification number (PIN) or the encrypted PIN block after authorization.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.3', 'Ensure that security policies and operational procedures for restricting access to cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.9', 'Activation of remoteaccess technologies for vendors and business partners only when needed by vendors and business partners, with immediate deactivation after use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.4', 'Ensure that security policies and operational procedures for protecting systems against malware are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.3', 'Default denyall setting.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.3', 'Mask PAN when displayed (the first six and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the first six/last four digits of the PAN.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.6', 'Acceptable network locations for the technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.3', 'Create audit logs for all access to all audit trails.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.2', 'Perform internal penetration testing at least annually and after any significant infrastructure or application upgrade or modification (such as an operating system upgrade, a subnetwork added to the environment, or a web server added to the environment).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.1', 'Use either video cameras or access control mechanisms (or both) to monitor individual physical access to sensitive areas. Review collected data and correlate with other entries. Store for at least three months, unless otherwise restricted by law.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2', 'In addition to assigning a unique ID, ensure proper userauthentication management for nonconsumer users and administrators on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.0', 'Protect all systems against malware and regularly update antivirus software or program.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.1', 'A formal process for approving and testing all network connections and changes to the firewall and router configurations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.2', 'Protect audit trail files from unauthorized modifications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.5', 'Maintain information about which PCI DSS requirements are managed by each service provider, and which are managed by the entity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.7', 'Do not disclose private IP addresses and routing information to unauthorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.4', 'Implemented mitigation for insecure communications.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.11', 'Additional requirement for service providers only: Perform reviews at least quarterly to confirm personnel are following security policies and operational procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.0', 'Restrict physical access to cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.5', 'Do not allow an individual to submit a new password/passphrase that is the same as any of the last four passwords/passphrases he or she has used.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2', 'Build firewall and router configurations that restrict connections between untrusted networks and any system components in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.7', 'Prevention of unauthorized substitution of cryptographic keys.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.1', 'Critical systems have the correct and consistent time.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.0', 'Develop and maintain secure systems and application.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.1', 'Perform quarterly internal vulnerability scans. Address vulnerabilities and perform rescans to verify all high risk vulnerabilities are resolved in accordance with the entity''s vulnerability ranking (per Requirement 6.1). Scans must be performed by qualified personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.2', 'Assign to an individual or team the information security management responsibilities: Monitor and analyze security alerts and information, and distribute to appropriate personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.6', 'Shared hosting providers must protect each entity?s hosted environment and cardholder data. These providers must meet specific requirements as detailed in Appendix A1: Additional PCI DSS Requirements for Shared Hosting Providers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4', 'Follow change control processes and procedures for all changes to system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.3', 'Ensure that security policies and operational procedures for encrypting transmissions of cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.1', 'Define access needs for each role.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.4', 'Do not allow unauthorized outbound traffic from the cardholder data environment to the Internet.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.4', 'Store cryptographic keys in the fewest possible locations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.6', 'Where other authentication mechanisms are used (for example, physical or logical security tokens, smart cards, certificates, etc.), use of these mechanisms must be assigned.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.1', 'Explicit approval by authorized parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8', 'Destroy media when it is no longer needed for business or legal reasons.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.3', 'Functionality testing to verify that the change does not adversely impact the security of the system.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.8', 'Additional requirement for service providers only: Implement a process for the timely detection and reporting of failures of critical security control systems.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.1', 'Classify media so the sensitivity of the data can be determined.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8', 'Maintain and implement policies and procedures to manage service providers with whom cardholder data is shared, or that could affect the security of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.7', 'All access to any database containing cardholder data (including access by applications, administrators, and all other users) is restricted.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3', 'Develop usage policies for critical technologies and define proper use of these technologies.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.2', 'Restrict access to privileged user IDs to least privileges necessary to perform job responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.3', 'Implement antispoofing measures to detect and block forged source IP addresses from entering the network. (For example, block traffic originating from the Internet with an internal source address..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.3', 'Store secret and private keys used to encrypt/decrypt cardholder data in one (or more) of the following forms at all times.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.4', 'Backout procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.7.1', 'Properly maintain inventory logs of all media and conduct media inventories at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.7', 'Retain audit trail history for at least one year, with a minimum of three months immediately available for analysis (for example, online, archived, or restorable from backup).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.2', 'Send the media by secured courier or other delivery method that can be accurately tracked.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.7', 'Screen potential personnel prior to hire to minimize the risk of attacks from internal sources. (Examples of background checks include previous employment history, criminal record, credit history, and reference checks..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.7', 'Requirement to review firewall and router rule sets at least every six months.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.6', 'If manual cleartext cryptographic keymanagement operations are used, these operations must be managed using split knowledge and dual control.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.6', 'Set passwords/passphrases for firsttime use and upon reset to a unique value for each user, and change immediately after the first use.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4', 'Using timesynchronization technology, synchronize all critical system clocks and times and ensure that the following is implemented for acquiring, distributing, and storing time.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.5', 'Ensure that security policies and operational procedures for managing vendor defaults and other security parameters are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2', 'Run internal and external network vulnerability scans at least quarterly and after any significant change in the network (such as new system component installations, changes in network topology, firewall rule modifications, product upgrades).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.1', 'Assign to an individual or team the following information security management responsibilities: * Establish, document, and distribute security policies and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.10', 'Ensure that security policies and operational procedures for restricting physical access to cardholder data are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.1', 'Separate development/test environments from production environments, and enforce the separation with access controls.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.2', 'Current network diagram that identifies all connections between the cardholder data environment and other networks, including any wireless networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.8', 'If a session has been idle for more than 15 minutes, require the user to reauthenticate to reactivate the terminal or session.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.3', 'Promptly back up audit trail files to a centralized log server or media that is difficult to alter.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.4', 'Install personal firewall software or equivalent functionality on any portable computing devices (including company and/or employeeowned) that connect to the Internet when outside the network (for example, laptops used by employees), and which are also used to access the CDE.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.9', 'Additional requirement for service providers only: Service providers acknowledge in writing to customers that they are responsible for the security of cardholder data the service provider possesses.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.6', 'Develop a process to modify and evolve the incident response plan according to lessons learned and to incorporate industry developments.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.3', 'Implemented mitigation for insecure cryptographic storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.3', 'Ensure that antivirus mechanisms are actively running and cannot be disabled or altered by users, unless specifically authorized by management on a casebycase basis for a limited time period.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.7', 'List of companyapproved products.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2.2', 'Assignment of privileges to individuals based on job classification and function.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.4', 'Render PAN unreadable anywhere it is stored (including on portable digital media, backup media, and in logs)', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.4', 'Create audit logs for all invalid logical access attempts.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.3', 'Exploitable vulnerabilities found during penetration testing are corrected and testing is repeated to verify the corrections.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1', 'Use appropriate facility entry controls to limit and monitor physical access to systems in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.1.3', 'Restrict physical access to wireless access points, gateways, handheld devices, networking/communications hardware, and telecommunication lines.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3', 'Implement a methodology for penetration testing.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.1', 'Create audit logs for all individual user accesses to cardholder dat.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.8', 'Automatic disconnect of sessions for remoteaccess technologies after a specific period of inactivity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2.2', 'Do not store the card verification code or value (threedigit or fourdigit number printed on the front or back of a payment card used to verify cardnotpresent transactions) after authorization.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.1', 'Establish a process to identify security vulnerabilities, using reputable outside sources for security vulnerability information, and assign a risk ranking (for example, as high, medium or low) to newly discovered security vulnerabilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.2', 'Implemented mitigation for buffer overflows.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.5', 'Ensure that security policies and operational procedures for managing firewalls are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.3', 'Ensure there is an established process for engaging service providers including proper due diligence prior to engagement.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.4', 'Write logs for externalfacing technologies onto a secure, centralized, internal log server or media device.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.0', 'Do not use vendorsupplied defaults for system passwords and other security parameter.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.7', 'Set the lockout duration to a minimum of 30 minutes or until an administrator enables the user ID.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.5.1', 'Documentation of impact.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.3', 'Implement additional security features for any required services, protocols, or daemons that are considered to be insecure..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6.3', 'Ensure management approves any and all media that is moved from a secured area (including when media is distributed to individuals).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6.2', 'Require personnel to acknowledge at least annually that they have read and understood the security policy and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.2', 'Record the audit trail entry type of event for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1', 'Deploy antivirus software on all systems commonly affected by malicious software (particularly personal computers and servers).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1.3', 'Assign access based on individual personnel''s job classification and function.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.2', 'Limit inbound Internet traffic to IP addresses within the DMZ.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.5', 'Do not use group, shared, or generic IDs, passwords, or other authentication methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.3', 'A list of all such devices and personnel with access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.2', 'Visitors are identified and given a badge or other identification that expires and that visibly distinguishes the visitors from onsite personnel.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1.2', 'Implement incident response procedures in the event unauthorized wireless access points are detected.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.1', 'Keep cardholder data storage to a minimum by implementing data retention and disposal policies, procedures and processes that include at least the following for all cardholder data (CHD) storage: . Limiting data storage amount and retention time to that which is required for legal, regulatory, and/or business requirements . Specific retention requirements for cardholder data . Processes for secure deletion of data when no longer needed . A quarterly process for identifying and securely deleting stored cardholder data that exceeds defined retention.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.3', 'Provide training for personnel to be aware of attempted tampering or replacement of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.6', 'Ensure that security policies and operational procedures for security monitoring and testing are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.5', 'Retirement or replacement (for example, archiving, destruction, and/or revocation) of keys as deemed necessary when the integrity of the key has been weakened (for example, departure of an employee with knowledge of a cleartext key component), or keys are suspected of being compromised.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.9', 'Implemented mitigation for crosssite request forgery (CSRF).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.8', 'Requirement for cryptographic key custodians to formally acknowledge that they understand and accept their keycustodian responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.4.3', 'Time settings are received from industryaccepted time sources.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.1.1', 'Review the security policy at least annually and update the policy when the environment changes.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.1', 'Limit access to system components and cardholder data to only those individuals whose job requires such access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6', 'Fully document and implement all keymanagement processes and procedures for cryptographic keys used for encryption of cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.2', 'Never send unprotected PANs by enduser messaging technologies (for example, email, instant messaging, SMS, chat, etc.).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.8.1', 'Additional requirement for service providers only: Respond to failures of any critical security controls in a timely manner.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.6', 'Maintain strict control over the internal or external distribution of any kind of media, including the following.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.8.1', 'Shred, incinerate, or pulp hardcopy materials so that cardholder data cannot be reconstructed. Secure storage containers used for materials that are to be destroyed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.5', 'Record the audit trail entry origination of event for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.2.1', 'Restrict inbound and outbound traffic to that which is necessary for the cardholder data environment, and specifically deny all other traffic.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3.1', 'Incorporate multifactor authentication for all nonconsole access into the CDE for personnel with administrative access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.3', 'Production data (live PANs) are not used for testing or development.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.3', 'Encrypt all nonconsole administrative access using strong cryptography.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.5.3', 'Assign to an individual or team the information security management responsibilities: Establish, document, and distribute security incident response and escalation procedures to ensure timely and effective handling of all situations.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.5.1', 'Limit viewing of audit trails to those with a jobrelated need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.0', 'Identify and authenticate access to system component.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3.1', 'Remove development, test and/or custom application accounts, user IDs, and passwords before applications become active or are released to customers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.4', 'Requirements for a firewall at each Internet connection and between any demilitarized zone (DMZ) and the internal network zone.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.2', 'Control addition, deletion, and modification of user IDs, credentials, and other identifier objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.1', 'Using strong cryptography, render all authentication credentials (such as passwords/phrases) unreadable during transmission and storage on all system components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.4', 'Provide appropriate training to staff with security breach response responsibilities.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.5', 'Implemented mitigation for improper error handling.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3.6', 'Place system components that store cardholder data (such as a database) in an internal network zone, segregated from the DMZ and other untrusted networks.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.1', 'Create the incident response plan to be implemented in the event of system breach.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4', 'Implement procedures to identify and authorize visitors.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.5', 'Acceptable uses of the technology.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '7.2', 'Establish an access control system(s) for systems components that restricts access based on a user''s need to know, and is set to deny all unless specifically allowed.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5', 'Document and implement procedures to protect keys used to secure stored cardholder data against disclosure and misuse.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '5.1.2', 'For systems considered to be not commonly affected by malicious software, perform periodic evaluations to identify and evaluate evolving malware threats in order to confirm whether such systems continue to not require antivirus software.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6.3', 'Follow up exceptions and anomalies identified during the review process.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.3.4.1', 'Additional requirement for service providers only: If segmentation is used, confirm PCI DSS scope by performing penetration testing on segmentation controls at least every six months and after any changes to segmentation controls/methods.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.8', 'Ensure that security policies and operational procedures for identification and authentication are documented, in use, and known to all affected parties.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.1', 'Implement only one primary function per server to prevent functions that require different security levels from coexisting on the same server. (For example, web servers, database servers, and DNS should be implemented on separate servers..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.6', 'Create audit logs for all initialization, stopping, or pausing of the audit logs.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5.8', 'Implemented mitigation for improper access control (such as insecure direct object references, failure to restrict URL access, directory traversal, and failure to restrict user access to functions).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.1', 'Implement audit trails to link all access to system components to each individual user.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.10.2', 'Review and test the plan, including all elements listed in Requirement 12.10.1, at least annually.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.3', 'Control physical access for onsite personnel to sensitive areas.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.2.2', 'Perform quarterly external vulnerability scans, via an Approved Scanning Vendor (ASV) approved by the Payment Card Industry Security Standards Council (PCI SSC). Perform rescans as needed, until passing scans are achieved.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.3', 'Develop internal and external software applications (including webbased administrative access to applications) securely.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.3.10', 'For personnel accessing cardholder data via remoteaccess technologies, prohibit the copying, moving, and storage of cardholder data onto local hard drives and removable electronic media, unless explicitly authorized for a defined business need.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.2.4', 'Change user passwords/passphrases at least once every 90 days..', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.2', 'Do not store sensitive authentication data after authorization (even if encrypted). If sensitive authentication data is received, render all data unrecoverable upon completion of the authorization process. It is permissible for issuers and companies that support issuing services to store sensitive authentication data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.1.5', 'Description of groups, roles, and responsibilities for management of network components.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.1', 'Assign all users a unique ID before allowing them to access system components or cardholder data.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.1', 'Always change vendorsupplied defaults and remove or disable unnecessary default accounts before installing a system on the network. This applies to ALL default passwords, including but not limited to those used by operating systems, software that provides security services, application and system accounts, pointofsale (POS) terminals, payment applications, Simple Network Management Protocol (SNMP) community strings, etc.).', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.8.1', 'Maintain a list of service providers including a description of the service provided.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.4', 'Use intrusiondetection and/or intrusionprevention techniques to detect and/or prevent intrusions into the network. Monitor all traffic at the perimeter of the cardholder data environment as well as at critical points in the cardholder data environment, and alert personnel to suspected compromises. Keep all intrusiondetection and prevention engines, baselines, and signatures up to date.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.2.7', 'Create audit logs for all creation and deletion of systemlevel objects.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.5', 'Address common coding vulnerabilities in softwaredevelopment processes as follows: * Train developers at least annually in uptodate secure coding techniques, including how to avoid common coding vulnerabilities. * Develop applications based on secure coding guidelines.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.5.1', 'Additional requirement for service providers only: Maintain a documented description of the cryptographic architecture', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.1.5', 'Manage IDs used by third parties to access, support, or maintain system components via remote access.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.0', 'Track and monitor all access to network resources and cardholder dat.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.6', 'Review logs and security events for all system components to identify anomalies or suspicious activity.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '2.2.5', 'Remove all unnecessary functionality, such as scripts, drivers, features, subsystems, file systems, and unnecessary web servers.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.6', 'Implement a formal security awareness program to make all personnel aware of the cardholder data security policy and procedures.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.4.4', 'Removal of test data and accounts from system components before the system becomes active / goes into production.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '1.3', 'Prohibit direct public access between the Internet and any system component in the cardholder data environment.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '8.3.2', 'Incorporate multifactor authentication for all remote network access (both user and administrator, and including thirdparty access for support or maintenance) originating from outside the entity''s network.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '10.3.4', 'Record the audit trail entry success or failure indication for all system components for each event.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.9.1', 'Maintain an uptodate list of devices.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '9.4.4', 'A visitor log is used to maintain a physical audit trail of visitor activity to the facility as well as computer rooms and data centers where cardholder data is stored or transmitted. Document the visitors name, the firm represented, and the onsite personnel authorizing physical access on the log. Retain this log for a minimum of three months, unless otherwise restricted by law.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '11.1', 'Implement processes to test for the presence of wireless access points (802.11), and detect and identify all authorized and unauthorized wireless access points on a quarterly basis.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '4.0', 'Encrypt transmission of cardholder data across open, public network.', '265'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '12.1', 'Establish, publish, maintain, and disseminate a security policy.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '3.6.3', 'Secure cryptographic key storage.', '999'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (10, '6.6', 'For publicfacing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks.', '999'); 
---
--- Custom ---
---
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (11, '20.0', 'Custom checklist title example', '0'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID, question_pre_ID, question_sprint_ID) VALUES (11, '20.1', 'Custom checklist item example, lorum ipsum', '14', '2', '0'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID) VALUES (11, '20.0', 'Custom checklist title example', '0'); 
INSERT OR REPLACE INTO checklists_kb (checklist_type, checklistID, content, kbID, question_pre_ID, question_sprint_ID) VALUES (11, '20.2', 'Custom checklist item example, lorum ipsum', '15', '0', '22'); 

