## Description:

The web application does not use an appropriate caching policy that specifies the extent to which each web page and associated form fields should be cached.



## Mitigation:


PHASE:Architecture and Design:
Protect information stored in cache.

PHASE:Architecture and Design Implementation:
Use a restrictive caching policy for forms and web pages that potentially contain sensitive information.

PHASE:Architecture and Design:
Do not store unnecessarily sensitive information in the cache.

PHASE:Architecture and Design:
Consider using encryption in the cache.

