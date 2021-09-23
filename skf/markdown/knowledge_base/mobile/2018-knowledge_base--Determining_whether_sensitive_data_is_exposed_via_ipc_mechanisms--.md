## Description:

Determining whether sensitive data is exposed via IPC mechanisms

MSTG-STORAGE-6: No sensitive data is exposed via IPC mechanisms.

Inter Process Communication (IPC) allows processes to send each other messages and data. If not properly configured, these mechanisms may leak sensitive data.


## Mitigation:

Make sure the application shares only necessary data with other apps.
