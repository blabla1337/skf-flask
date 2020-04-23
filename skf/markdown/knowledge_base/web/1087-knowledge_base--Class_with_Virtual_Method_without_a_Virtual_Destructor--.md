## Description:

A class contains a virtual method, but the method does not have an associated virtual destructor.

This issue can prevent the software from running reliably, e.g. due to undefined behavior. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Mitigation:
