# C10: Handle all Errors and Exceptions

## Description
Exception handling is a programming concept that allows an application to respond to different error states (like network down, or database connection failed, etc) in various ways. Handling exceptions and errors correctly is critical to making your code reliable and secure.

Error and exception handling occurs in all areas of an application including critical business logic as well as security features and framework code.

Error handling is also important from an intrusion detection perspective. Certain attacks against your application may trigger errors which can help detect attacks in progress.

## Error Handling Mistakes
Researchers at the University of Toronto have found that even small mistakes in error handling or forgetting to handle errors can lead to [catastrophic failures in distributed systems](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf).

Mistakes in error handling can lead to different kinds of security vulnerabilities.

* **Information leakage**: Leaking sensitive information in error messages can unintentionally help attackers. For example, an error that returns a stack trace or other internal error details can provide an attacker with information about your environment. Even small differences in handling different error conditions (e.g., returning "invalid user" or "invalid password" on authentication errors) can provide valuable clues to attackers. As described above, be sure to log error details for forensics and debugging purposes, but don’t expose this information, especially to an external client.
* **TLS bypass**:  The [Apple goto "fail bug"](https://www.dwheeler.com/essays/apple-goto-fail.html) was a control-flow error in error handling code that lead to a complete compromise of TLS connections on apple systems.
* **DOS**: A lack of basic error handling can lead to system shutdown. This is usually a fairly easy vulnerability for attackers to exploit. Other error handling problems could lead to increased usage of CPU or disk in ways that could degrade the system.


## Positive Advice
* Manage exceptions in a [centralized manner](https://www.owasp.org/index.php/Error_Handling#Centralised_exception_handling_.28Struts_Example.29) to avoid duplicated try/catch blocks in the code. Ensure that all unexpected behavior is correctly handled inside the application.
* Ensure that error messages displayed to users do not leak critical data, but are still verbose enough to enable the proper user response.
* Ensure that exceptions are logged in a way that gives enough information for support, QA, forensics or incident response teams to understand the problem.
* Carefully test and verify error handling code.

## References
* [OWASP Code Review Guide: Error Handling](https://www.owasp.org/index.php/Error_Handling)
* [OWASP Testing Guide: Testing for Error Handling](https://www.owasp.org/index.php/Testing_for_Error_Handling)
* [OWASP Improper Error Handling](https://www.owasp.org/index.php/Improper_Error_Handling)
* [CWE 209: Information Exposure Through an Error Message](https://cwe.mitre.org/data/definitions/209.html)
* [CWE 391: Unchecked Error Condition](https://cwe.mitre.org/data/definitions/391.html)

## Tools
* [Error Prone](http://errorprone.info/)  - A static analysis tool from Google to catch common mistakes in error handling for Java developers
* One of the most famous automated tools for finding errors at runtime is [Netflix's Chaos Monkey](https://github.com/Netflix/SimianArmy), which intentionally disables system instances to ensure that the overall service will recover correctly.
