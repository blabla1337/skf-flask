## Description:

Memory for Sensitive Data

MSTG-STORAGE-10: The app does not hold sensitive data in memory longer than necessary, and memory is cleared explicitly after use.

Analyzing memory can help developers to identify the root causes of problems such as application crashes. However, it can also be used to access to sensitive data. We need to make sure that this info is exposed as briefly as possible.


## Mitigation:

The app should not hold sensitive data in memory longer than necessary, and memory should be cleared explicitly after use.