##Description:

The product does not sufficiently compartmentalize functionality or processes that require different privilege levels, rights, or permissions.

When a weakness occurs in functionality that is accessible by lower-privileged users, then without strong boundaries, an attack might extend the scope of the damage to higher-privileged users.

##Mitigation:


PHASE:Architecture and Design:
Break up privileges between different modules, objects or entities. Minimize the interfaces between modules and require strong access control between them.

