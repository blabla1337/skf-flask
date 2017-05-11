# HTTP strict transport security
-------

## Description:

HTTP Strict Transport Security (HSTS) is an opt-in security enhancement that is specified
by a web application through the use of a special response header. Once a supported browser
receives this header that browser will prevent any communications from being sent over
HTTP to the specified domain and will instead send all communications over HTTPS. It also
prevents HTTPS click through prompts on browsers. 

HSTS addresses the following threats:

1. User bookmarks or manually types http://example.com and is subject to a man-in-the-middle attacker
   HSTS automatically redirects HTTP requests to HTTPS for the target domain
2. Web application that is intended to be purely HTTPS inadvertently contains HTTP links or serves content over HTTP
   HSTS automatically redirects HTTP requests to HTTPS for the target domain
3. A man-in-the-middle attacker attempts to intercept traffic from a victim user using an invalid certificate and 
   hopes the user will accept the bad certificate
4. HSTS does not allow a user to override the invalid certificate message

## Solution:

When users are visiting the application it should set the following header:
These headers should be set in a base class which always sets the header no mather what
page the users initially visit.

Simple example, using a long (1 year) max-age:
    Strict-Transport-Security: max-age=31536000

If all present and future subdomains will be HTTPS:
    Strict-Transport-Security: max-age=31536000; includeSubDomains

## CAUTION: 
Site owners can use HSTS to identify users without cookies. This can lead to a significant
privacy leak.

Cookies can be manipulated from sub-domains, so omitting the include "includeSubDomains"
option permits a broad range of cookie-related attacks that HSTS would otherwise prevent
by requiring a valid certificate for a subdomain. Ensuring the "Secure Flag" is set on all
cookies will also prevent, some, but not all, of the same attacks.

