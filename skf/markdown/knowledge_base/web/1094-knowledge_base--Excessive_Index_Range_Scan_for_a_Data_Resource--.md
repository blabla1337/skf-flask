## Description:

The software contains an index range scan for a large data table, but the scan can cover a large number of rows.

This issue can make the software perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability. While the interpretation of large data table and excessive index range may vary for each product or developer, CISQ recommends a threshold of 1000000 table rows and a threshold of 10 for the index range.

## Mitigation:
