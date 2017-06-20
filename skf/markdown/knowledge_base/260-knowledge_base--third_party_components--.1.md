# Third party components
-------

## Description: 

All third party components the application depends on to operate must be mapped in
terms of the functions, and/or security functions, they provide for several reasons.

1. Whenever one of these dependencies is down the application has to handle the missing of
   that dependency gracefully and not break down resulting in a DOS.

2. All security functions they provide must be mapped and backed up by a WAF or ModSecurity in case
   the dependency goes down for service.

## Solution:

Verify that all components that are not part of the application but that the application
relies on to operate are defined in terms of the functions, and/or security functions, they provide.
