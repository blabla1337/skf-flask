# HSTS preload
-------

## Description:

HTTP Strict Transport Security (HSTS) is an opt-in security enhancement that is specified by a 
web application through the use of a special response header. Once a supported browser receives 
this header that browser will prevent any communications from being sent over HTTP to the specified 
domain and will instead send all communications over HTTPS. It also prevents HTTPS click through prompts on browsers.

However, there is still a window where a user who has a fresh install, or who wipes out their local state,
is vulnerable. This is due to the fact that the browser is not yet aware of the fact if the application is trying to connect to supports HSTS. Whenever you are added to the preload list,
the application its preference is hard-coded into the browser and all first initial connections will
always be made by HTTPS.

## Solution:

In order to request for HSTS preloading, there are some requirements the application has to 
be complient with. The submission for the HSTS preloading can be performed on the following url:

    https://hstspreload.org/

Submission Requirements

If a site sends the preload directive in an HSTS header, it is considered to be requesting 
inclusion in the preload list and may be submitted via the form on this site.

In order to be accepted to the HSTS preload list the site must satisfy the following set of requirements:

1. Serve a valid certificate.
2. Redirect from HTTP to HTTPS on the same host, if you are listening on port 80.
3. Serve all subdomains over HTTPS.
   - In particular, you must support HTTPS for the www subdomain if a DNS record for that subdomain exists.
5. Serve an HSTS header on the base domain for HTTPS requests:
   - The max-age must be at least eighteen weeks (10886400 seconds).
   - The includeSubDomains directive must be specified.
   - The preload directive must be specified.
   - If you are serving an additional redirect from your HTTPS site, that redirect must still have the HSTS
     header (rather than the page it redirects to).

Now the following parameter can be added to the HSTS header,

maintained by Chrome (and used by Firefox and Safari), then use:
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

The 'preload' flag indicates the site owner's consent to have their domain preloaded. The site owner
still needs to then go and submit the domain to the list.

## CAUTION:

Make sure to have a perfectly smooth certification management. Whenever there is no
valid certificate, the application can not be downgraded temporarily over HTTP. The failing of
the TLS certificate will lead to a DOS since HSTS does not allow the application to be visited over HTTP
