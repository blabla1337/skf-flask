## Description:

When malformed or abnormal HTTP requests are interpreted by one or more entities in the data flow between the user and the web server, such as a proxy or firewall, they can be interpreted inconsistently, allowing the attacker to smuggle a request to one device without the other device being aware of it.



## Mitigation:


PHASE:Implementation:
Use a web server that employs a strict HTTP parsing procedure, such as Apache [REF-433].

PHASE:Implementation:
Use only SSL communication.

PHASE:Implementation:
Terminate the client session after each request.

PHASE:System Configuration:
Turn all pages to non-cacheable.

