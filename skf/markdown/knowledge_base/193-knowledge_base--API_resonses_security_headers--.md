## Description:

There are some security headers which should be properly configured in order to protect some API callbacks against Reflective File Download and other type of injections.

Also check that the API response is not dynamic, if so use input validation and encoding in order to prevent XSS and Same origin method execution attacks.

## Solution:

Verify that all API responses contain X-Content-Type-Options: nosniff and Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type).

