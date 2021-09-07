## Description:

Identify components

MSTG-ARCH-1: All app components are identified and known to be needed.

It's important to review all the application components as we want to remove the unused components in the release of the application. The more code and components in here increases the risk of the application and the possibity that it can be abused by an attacker, the goal is to minimize the attack surface.

## Mitigation:

Review the application on the components that are being important and the usage of those and if necerry remove unused components.

Follow every entry points and check:

	- Is there any data retrieved by the app which should require privacy protection of that data? If so, are all required controls in place?	
	- Are all communications secured?
	- When you need more functionalities, are the right security controls downloaded as well?
