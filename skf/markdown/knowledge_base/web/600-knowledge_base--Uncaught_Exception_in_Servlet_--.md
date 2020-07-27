##Description:

The Servlet does not catch all exceptions, which may reveal sensitive debugging information.

When a Servlet throws an exception, the default error response the Servlet container sends back to the user typically includes debugging information. This information is of great value to an attacker. For example, a stack trace might show the attacker a malformed SQL query string, the type of database being used, and the version of the application container. This information enables the attacker to target known vulnerabilities in these components.

##Mitigation:


PHASE:Implementation:
Implement Exception blocks to handle all types of Exceptions.

