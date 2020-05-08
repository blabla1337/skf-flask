## Description:

The software initializes data using hard-coded values that act as network resource identifiers.

This issue can prevent the software from running reliably, e.g. if it runs in an environment does not use the hard-coded network resource identifiers. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.

## Mitigation:
