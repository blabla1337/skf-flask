## User and Account Management
User management is also another important part of secure design. All users should have minimum roles, a proper passwords policy and all service accounts should have least privileges. 

Some common example of bad practices: 

* Running services with administrative accounts, for example running database or web service with admin privilege. Any code injection will double the damage if the service runs with a high privilege account. Security best practices recommend to use minimum roles with a restricted environment. 
* Using same accounts/credentials for other services is also not part of security best practices. For example, using same password for database and operating system increase the attack surface. That means, somehow if attacker find a way to obtain the credentials, then she/he will be able to login both systems.
* Using default/guessable credentials are another security bad practice example. Each account should be unique, have a proper password policy and management cycle. 
