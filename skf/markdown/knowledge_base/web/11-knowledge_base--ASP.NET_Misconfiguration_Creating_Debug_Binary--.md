## Description:

Debugging messages help attackers learn about the system and plan a form of attack.

ASP .NET applications can be configured to produce debug binaries. These binaries give detailed debugging messages and should not be used in production environments. Debug binaries are meant to be used in a development or testing environment and can pose a security risk if they are deployed to production.

## Mitigation:


PHASE:System Configuration:
Avoid releasing debug binaries into the production environment. Change the debug mode to false when the application is deployed into production.

