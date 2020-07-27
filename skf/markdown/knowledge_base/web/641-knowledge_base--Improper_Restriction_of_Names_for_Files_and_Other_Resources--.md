##Description:

The application constructs the name of a file or other resource using input from an upstream component, but it does not restrict or incorrectly restricts the resulting name.

This may produce resultant weaknesses. For instance, if the names of these resources contain scripting characters, it is possible that a script may get executed in the client's browser if the application ever displays the name of the resource on a dynamically generated web page. Alternately, if the resources are consumed by some application parser, a specially crafted name can exploit some vulnerability internal to the parser, potentially resulting in execution of arbitrary code on the server machine. The problems will vary based on the context of usage of such malformed resource names and whether vulnerabilities are present in or assumptions are made by the targeted technology that would make code execution possible.

##Mitigation:


PHASE:Architecture and Design:
Do not allow users to control names of resources used on the server side.

PHASE:Architecture and Design:
Perform whitelist input validation at entry points and also before consuming the resources. Reject bad file names rather than trying to cleanse them.

PHASE:Architecture and Design:
Make sure that technologies consuming the resources are not vulnerable (e.g. buffer overflow, format string, etc.) in a way that would allow code execution if the name of the resource is malformed.

