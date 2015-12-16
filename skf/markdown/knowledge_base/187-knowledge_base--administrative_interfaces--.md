Administrative interfaces are not accessible to untrusted parties
-------

**Description:**

Whenever it is not necessary for administrative pages to be publicly accessible these
pages should have restriced access for users. Whenever these pages are secluded from the rest
of the application in terms of accessability this could reduce the attack vector of malicious users.

**Solution:**

The first solution is to grant access only from a certain source IP range to the 
administrative interface. If that solution would not be possible than it is always recommended
to enforce a step-up or adaptive authentication for logging in into the administrative interface.

Recommended knowledgebase item:

- Step up or adaptive authentication