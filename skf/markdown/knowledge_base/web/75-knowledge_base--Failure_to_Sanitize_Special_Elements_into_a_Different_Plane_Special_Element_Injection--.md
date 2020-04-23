## Description:

The software does not adequately filter user-controlled input for special elements with control implications.



## Mitigation:


PHASE:Requirements:
Programming languages and supporting technologies might be chosen which are not subject to these issues.

PHASE:Implementation:
Utilize an appropriate mix of whitelist and blacklist parsing to filter special element syntax from all input.

