### Minimize Feedback / Information Exposure

Avoid giving security or sensitive information to untrusted users. If a request is privileged, simply succeed or fail, and if it fails just say that it failed and minimize information on why it failed. In short, minimize feedback to untrusted users if it might compromise security, and instead send the detailed information to audit trail logs. For example:

* If your program requires some sort of user authentication (e.g., you are writing a network service or login program), give the user as little information as possible before they authenticate. In particular, avoid giving away the version number of your program before authentication. Otherwise, if a particular version of your program is found to have a vulnerability, then users who don’t upgrade from that version advertise to attackers that they are vulnerable.

* If your program accepts a password, don’t echo the exact characters back; this creates another way passwords can be seen by others. In HTML forms, set the input type to password, which intentionally limits the feedback.

* On a failed login, just say “*username or password failed*” or similar - don’t expose whether it was the username or the password that failed. That could tell the attacker that the username is valid, and makes further attacks easier.

* In general, don’t display sensitive/private data unless necessary at that point.

Implement audit logging early in development. Then, if you need to record more detailed information to aid debugging, report that information in the logs instead of displaying it to the user. Audit logs are really convenient for debugging (because they are designed to record useful information without interfering with normal operations), and you are more likely to include useful status information in the logs if they are developed in parallel with the rest of the program. They will also reduce the temptation to reveal too much to untrusted users.

Also, ensure that users cannot receive unauthorized information. Permissions and namespaces should be clearly set to prevent this.

Improper information exposure is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #4. It is also identified as [CWE-200](https://cwe.mitre.org/data/definitions/200.html), *Information Exposure*.