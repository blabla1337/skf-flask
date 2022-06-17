# C2: Leverage Security Frameworks and Libraries

## Description
Secure coding libraries and software frameworks with embedded security help software developers guard against security-related design and implementation flaws. A developer writing an application from scratch might not have sufficient knowledge, time, or budget to properly implement or maintain security features. Leveraging security frameworks helps accomplish security goals more efficiently and accurately.

## Implementation Best Practices
When incorporating third party libraries or frameworks into your software, it is important to consider the following best practices:

1. Use libraries and frameworks from trusted sources that are actively maintained and widely used by many applications.
2. Create and maintain an inventory catalog of all the third party libraries.
3. Proactively keep libraries and components up to date. Use a tool like [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/) and [Retire.JS](https://retirejs.github.io/retire.js/) to identify project dependencies and check if there are any known, publicly disclosed vulnerabilities for all third party code.
4. Reduce the attack surface by encapsulating the library and expose only the required behaviour into your software.

## Vulnerabilities Prevented
Secure frameworks and libraries can help to prevent a wide range of web application vulnerabilities. It is critical to keep these frameworks and libraries up to date as described in the [using components with known vulnerabilities [Top Ten 2017 risks](https://owasp.org/www-project-top-ten/).

## Tools
* [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/) - identifies project dependencies and checks for publicly disclosed vulnerabilities
* [Retire.JS](http://retirejs.github.io/retire.js/) scanner for JavaScript libraries
