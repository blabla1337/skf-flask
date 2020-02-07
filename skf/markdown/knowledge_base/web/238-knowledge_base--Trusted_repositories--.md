## Description:

Whenever the components are loaded from untrusted repositories this could imply the 
components are backdoored, outdated and cannot be trusted.

## Solution:

When checking if a repository can be trusted look to see if the source is stil maintained, 
security bugs are being reported and mitigated, if the component is not at the end of life or deprecated.

You can also scan the component in your SDLC through OWASP dependency checker to see if there are any
known CVEs for this component.
