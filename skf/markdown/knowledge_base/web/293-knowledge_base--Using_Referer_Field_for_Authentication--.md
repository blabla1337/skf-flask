## Description:

The referer field in HTTP requests can be easily modified and, as such, is not a valid means of message integrity checking.



## Mitigation:


PHASE:Architecture and Design:
In order to usefully check if a given action is authorized, some means of strong authentication and method protection must be used. Use other means of authorization that cannot be simply spoofed. Possibilities include a username/password or certificate.

