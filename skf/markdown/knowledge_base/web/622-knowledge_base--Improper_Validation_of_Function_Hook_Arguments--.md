##Description:

A product adds hooks to user-accessible API functions, but does not properly validate the arguments. This could lead to resultant vulnerabilities.

Such hooks can be used in defensive software that runs with privileges, such as anti-virus or firewall, which hooks kernel calls. When the arguments are not validated, they could be used to bypass the protection scheme or attack the product itself.

##Mitigation:


PHASE:Architecture and Design:
Ensure that all arguments are verified, as defined by the API you are protecting.

PHASE:Architecture and Design:
Drop privileges before invoking such functions, if possible.

