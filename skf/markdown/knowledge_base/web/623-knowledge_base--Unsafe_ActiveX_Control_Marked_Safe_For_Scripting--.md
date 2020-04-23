## Description:

An ActiveX control is intended for restricted use, but it has been marked as safe-for-scripting.

This might allow attackers to use dangerous functionality via a web page that accesses the control, which can lead to different resultant vulnerabilities, depending on the control's behavior.

## Mitigation:


PHASE:Architecture and Design:
During development, do not mark it as safe for scripting.

PHASE:System Configuration:
After distribution, you can set the kill bit for the control so that it is not accessible from Internet Explorer.

