## Description:

The software uses a dedicated, central data manager component as required by design, but it contains code that performs data-access operations that do not use this data manager.

This issue can make the software perform more slowly than intended, since the intended central data manager may have been explicitly optimized for performance or other quality characteristics. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

## Mitigation:
