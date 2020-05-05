## Description:

A parent class contains one or more child classes, but the parent class does not have a virtual destructor method.

This issue can prevent the software from running reliably due to undefined or unexpected behaviors. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Mitigation:
