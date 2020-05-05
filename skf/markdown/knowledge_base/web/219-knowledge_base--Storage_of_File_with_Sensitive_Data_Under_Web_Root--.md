## Description:

The application stores sensitive data under the web document root with insufficient access control, which might make it accessible to untrusted parties.

Besides public-facing web pages and code, applications may store sensitive data, code that is not directly invoked, or other files under the web document root of the web server. If the server is not configured or otherwise used to prevent direct access to those files, then attackers may obtain this sensitive data.

## Mitigation:


PHASE:Implementation System Configuration:
Avoid storing information under the web root directory.

PHASE:System Configuration:
Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the web directory.

