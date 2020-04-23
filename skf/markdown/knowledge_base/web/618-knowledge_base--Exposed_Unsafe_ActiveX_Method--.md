## Description:

An ActiveX control is intended for use in a web browser, but it exposes dangerous methods that perform actions that are outside of the browser's security model (e.g. the zone or domain).

ActiveX controls can exercise far greater control over the operating system than typical Java or javascript. Exposed methods can be subject to various vulnerabilities, depending on the implemented behaviors of those methods, and whether input validation is performed on the provided arguments. If there is no integrity checking or origin validation, this method could be invoked by attackers.

## Mitigation:


PHASE:Implementation:
If you must expose a method, make sure to perform input validation on all arguments, and protect against all possible vulnerabilities.

PHASE:Architecture and Design:
Use code signing, although this does not protect against any weaknesses that are already in the control.

PHASE:Architecture and Design System Configuration:
Where possible, avoid marking the control as safe for scripting.

