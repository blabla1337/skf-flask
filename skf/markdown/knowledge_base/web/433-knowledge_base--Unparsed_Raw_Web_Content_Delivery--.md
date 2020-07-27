##Description:

The software stores raw content or supporting code under the web document root with an extension that is not specifically handled by the server.

If code is stored in a file with an extension such as .inc or .pl, and the web server does not have a handler for that extension, then the server will likely send the contents of the file directly to the requester without the pre-processing that was expected. When that file contains sensitive information such as database credentials, this may allow the attacker to compromise the application or associated components.

##Mitigation:


PHASE:Architecture and Design:
Perform a type check before interpreting files.

PHASE:Architecture and Design:
Do not store sensitive information in files which may be misinterpreted.

