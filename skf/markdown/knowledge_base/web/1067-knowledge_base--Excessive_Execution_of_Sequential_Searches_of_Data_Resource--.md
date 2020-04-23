## Description:

The software contains a data query against an SQL table or view that is configured in a way that does not utilize an index and may cause sequential searches to be performed.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

## Mitigation:
