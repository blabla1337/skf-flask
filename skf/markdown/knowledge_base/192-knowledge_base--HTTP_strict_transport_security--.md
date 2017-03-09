# HTTP strict transport security
-------

## Description:

HTTP Strict Transport Security (HSTS) is an opt-in security enhancement that is specified
by a web application through the use of a special response header. Once a supported browser
receives this header that browser will prevent any communications from being sent over
HTTP to the specified domain and will instead send all communications over HTTPS. It also
prevents HTTPS click through prompts on browsers.


## Solution:

Simple example, using a long (1 year) max-age:
    Strict-Transport-Security: max-age=31536000

If all present and future subdomains will be HTTPS:
    Strict-Transport-Security: max-age=31536000; includeSubDomains

Recommended: If the site owner would like their domain to be included in the HSTS preload list
maintained by Chrome (and used by Firefox and Safari), then use:
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

The 'preload' flag indicates the site owner's consent to have their domain preloaded. The site owner
still needs to then go and submit the domain to the list.

There is still a window where a user who has a fresh install, or who wipes out their local state,
is vulnerable. This is due to the fact that the browser is not yet aware of the fact if the application
the it is trying to connect to supports HSTS. Whenever you are added to the preload list,
the application its preference is hard-coded into the browser and all first initial connections will
always be made by HTTPS.

## CAUTION: 
Site owners can use HSTS to identify users without cookies. This can lead to a significant
privacy leak.

Cookies can be manipulated from sub-domains, so omitting the include "includeSubDomains"
option permits a broad range of cookie-related attacks that HSTS would otherwise prevent
by requiring a valid certificate for a subdomain. Ensuring the "Secure Flag" is set on all
cookies will also prevent, some, but not all, of the same attacks.
