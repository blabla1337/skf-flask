##Description:

The software contains functionality that is not documented, not part of the specification, and not accessible through an interface or command sequence that is obvious to the software's users or administrators.

Hidden functionality can take many forms, such as intentionally malicious code, Easter Eggs that contain extraneous functionality such as games, developer-friendly shortcuts that reduce maintece or support costs such as hard-coded accounts, etc. From a security perspective, even when the functionality is not intentionally malicious or damaging, it can increase the software's attack surface and expose additional weaknesses beyond what is already exposed by the intended functionality. Even if it is not easily accessible, the hidden functionality could be useful for attacks that modify the control flow of the application.

##Mitigation:


PHASE:Installation:
Always verify the integrity of the software that is being installed.

PHASE:Testing:
Conduct a code coverage analysis using live testing, then closely inspect any code that is not covered.

