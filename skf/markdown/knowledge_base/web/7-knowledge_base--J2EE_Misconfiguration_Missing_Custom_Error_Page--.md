## Description:

The default error page of a web application should not display sensitive information about the software system.

A Web application must define a default error page for 4xx errors (e.g. 404), 5xx (e.g. 500) errors and catch java.lang.Throwable exceptions to prevent attackers from mining information from the application container's built-in error response. When an attacker explores a web site looking for vulnerabilities, the amount of information that the site provides is crucial to the eventual success or failure of any attempted attacks.

## Mitigation:


PHASE:Implementation:
Handle exceptions appropriately in source code.

PHASE:Implementation System Configuration:
Always define appropriate error pages. The application configuration should specify a default error page in order to guarantee that the application will never leak error messages to an attacker. Handling standard HTTP error codes is useful and user-friendly in addition to being a good security practice, and a good configuration will also define a last-chance error handler that catches any exception that could possibly be thrown by the application.

PHASE:Implementation:
Do not attempt to process an error or attempt to mask it.

PHASE:Implementation:
Verify return values are correct and do not supply sensitive information about the system.

