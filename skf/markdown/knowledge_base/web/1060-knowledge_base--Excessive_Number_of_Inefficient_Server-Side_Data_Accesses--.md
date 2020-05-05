## Description:

The software performs too many data queries without using efficient data processing functionality such as stored procedures.

This issue can make the software perform more slowly due to computational expense. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of too many data queries may vary for each product or developer, CISQ recommends a default maximum of 5 data queries for an inefficient function/procedure.

## Mitigation:
