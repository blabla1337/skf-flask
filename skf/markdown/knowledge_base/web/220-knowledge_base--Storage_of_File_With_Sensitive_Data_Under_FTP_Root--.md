## Description:

The application stores sensitive data under the FTP server root with insufficient access control, which might make it accessible to untrusted parties.



## Mitigation:


PHASE:Implementation System Configuration:
Avoid storing information under the FTP root directory.

PHASE:System Configuration:
Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the FTP directory.

