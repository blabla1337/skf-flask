## Description:

Sensitive data on local device

MSTG-STORAGE-13: No sensitive data should be stored locally on the mobile device. Instead, data should be retrieved from a remote endpoint when needed and only be kept in memory.

MSTG-STORAGE-14: If sensitive data is still required to be stored locally, it should be encrypted using a key derived from hardware backed storage which requires authentication.


## Mitigation:

In general sensitive data stored locally on the device should always be at least encrypted, and any keys used for encryption methods should be securely stored within KeyChain (iOS) or KeyStore (Android). These files should also be stored within the application sandbox. If achievable for the application, sensitive data should be stored off device or, even better, not stored at all.