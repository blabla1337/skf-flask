
Session cookies (Domain)
-------

**Description:**

The Domain option allows you to specify whether or not to send the cookie to subdomains. 


**Solution:**

Setting www.example.com will mean only the exact domain www.example.com will 
be matched, while .example.com (wildcard) will also match again any 
subdomain (forums.example.com, blog.example.com).

The use of a wildcard is not recommended at all and should be avoided.

There are a lot of different mitigations in order to harden your session management.
These mitigations are amongst others the setting of the "HttpOnly and secure" flags on
your sessions. Follow the "Sessions pattern" list to make sure your session management is
secure.

Recommended knowledge base items:

- Cross subdomain cookie attacks
- Sessions pattern
