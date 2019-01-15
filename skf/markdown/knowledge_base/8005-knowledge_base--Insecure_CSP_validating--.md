## Description:

The Content Security Policy (CSP) is a computer security standard introduced to prevent cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content.
If the CSP and the validator are separate, an attacker might be able to intercept the data transmitted between the two endpoints. That could lead the attacker in performing code injection attacks mentioned before.

## Solution:

Ensure that in cases where a verifier and CSP are separate, mutually authenticated TLS is in place between the two endpoints.


