## Description:

When a security-critical event occurs, the software either does not record the event or omits important details about the event when logging it.

When security-critical events are not logged properly, such as a failed login attempt, this can make malicious behavior more difficult to detect and may hinder forensic analysis after an attack succeeds.

## Mitigation:


PHASE:Architecture and Design:
Use a centralized logging mechanism that supports multiple levels of detail. Ensure that all security-related successes and failures can be logged.

PHASE:Operation:
Be sure to set the level of logging appropriately in a production environment. Sufficient data should be logged to enable system administrators to detect attacks, diagnose errors, and recover from attacks. At the same time, logging too much data (CWE-779) can cause the same problems.

