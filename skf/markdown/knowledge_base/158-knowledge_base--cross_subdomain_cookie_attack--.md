# Cross subdomain cookie attacks
-------

## Description:

A quick overview of how it works:

1. A web site www.example.com hands out subdomains to untrusted third parties
2. One such party, Mallory, who now controls evil.example.com, lures Alice to her site
3. A visit to evil.example.com sets a session cookie with the domain .example.com on Alice's browser
4. When Alice visits www.example.com, this cookie will be sent with the request, as the specs for cookies states, and Alice will have the session specified by Mallory's cookie.
5. Mallory can now use Alice her account.

## Solution:

In this scenario changing the sessionID on login does not make any difference since
Alice is already logged in when she visits Mallory's evil webpage.

It is good practice to use a completely different domain for all trusted activity.

For example Google uses google.com for trusted activities and *.googleusercontent.com
for untrusted sites.

Also when setting your cookies to specify which domains they are allowed to
be send to. Especially on your trusted domain you do not want to leak cookies to unintended
subdomains. highly recommended is to not use wildcards when setting this option.
