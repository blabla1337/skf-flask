##Description:

HTTP Strict-Transport-Security (HSTS) allows sites to specify that they should be accessed
via a secure connection only. The problem is, a user's first request to a site employing
HSTS may not be over HTTPS. A preload list will allow us to ship Firefox with some
pre-set HSTS sites that, from the first time they're accessed in the browser, will require
a secure connection.

##Mitigation:

In order to be included on the HSTS preload list, your site must:

1. Have a valid certificate (which must expire before 2016 if it uses SHA-1).
2. Redirect all HTTP traffic to HTTPS—i.e. be HTTPS only.
3. Serve all subdomains over HTTPS, specifically including the www subdomain if a DNS
record for that subdomain exists.
4. Serve an HSTS header on the base domain:
* Expiry must be at least eighteen weeks (10886400 seconds).
* The includeSubdomains token must be specified.
* The preload token must be specified.
* If you are serving a redirect, that redirect must have the HSTS header, not the page it
  redirects to.

For more details on HSTS, please see RFC 6797. Note that the preload flag in the HSTS
header is required to confirm and authenticate your submission to the preload list.
An example valid HSTS header:

    Strict-Transport-Security: max-age=10886400; includeSubDomains; preload

Adding your website to the list:
https://www.chromium.org/hsts     


Source:
https://wiki.mozilla.org/Privacy/Features/HSTS_Preload_List
