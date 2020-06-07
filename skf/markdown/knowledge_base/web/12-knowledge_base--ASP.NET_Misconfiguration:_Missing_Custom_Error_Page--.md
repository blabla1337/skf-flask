## Description:

An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses.



## Mitigation:


PHASE:System Configuration:
Handle exceptions appropriately in source code. ASP .NET applications should be configured to use custom error pages instead of the framework default page.

PHASE:Architecture and Design:
Do not attempt to process an error or attempt to mask it.

PHASE:Implementation:
Verify return values are correct and do not supply sensitive information about the system.

