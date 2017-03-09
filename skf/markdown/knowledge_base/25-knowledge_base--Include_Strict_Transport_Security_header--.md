# Include Strict-Transport-Security header
-------

## Description:

HTTP Strict-Transport-Security (HSTS) enforces secure (HTTP over SSL/TLS) connections to
the server. This reduces impact of bugs in web applications leaking session data through
cookies and external links and defends against Man-in-the-middle attacks. HSTS also
disables the ability for user's to ignore SSL negotiation warnings


## Solution:

These headers are also known as the: Strict-Transport-Security: max-age=16070400:
includeSubDomains and provide protection against SSL Strip attacks when implemented in the
application or webserver.

When connecting to an HSTS host for the first time, the browser won't know whether or not
to use a secure connection, because it has never received an HSTS header from that host.
Consequently, an active network attacker could prevent the browser from ever connecting
securely (and even worse, the user may never realize something is amiss). To mitigate
this attack, you can add your application to a preload list which makes HSTS enforced by default.
When a user connects to one of these hosts for the first time, the browser will know that
it must use a secure connection. If a network attacker prevents secure connections to the
server, the browser will not attempt to connect over an insecure protocol, thus
maintaining the user's security.

Visit:
    https://hstspreload.appspot.com/
Here you can find how to add your application to HSTS preload
