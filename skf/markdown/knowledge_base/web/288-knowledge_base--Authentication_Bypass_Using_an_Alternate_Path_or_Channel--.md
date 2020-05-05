## Description:

A product requires authentication, but the product has an alternate path or channel that does not require authentication.



## Mitigation:


PHASE:Architecture and Design:
Funnel all access through a single choke point to simplify how users can access a resource. For every access, perform a check to determine if the user has permissions to access the resource.

