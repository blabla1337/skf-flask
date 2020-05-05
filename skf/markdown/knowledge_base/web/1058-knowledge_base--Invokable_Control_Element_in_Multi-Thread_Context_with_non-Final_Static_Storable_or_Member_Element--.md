## Description:

The code contains a function or method that operates in a multi-threaded environment but owns an unsafe non-final static storable or member data element.

This issue can prevent the software from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Mitigation:
