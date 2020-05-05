## Description:

The web application does not adequately enforce appropriate authorization on all restricted URLs, scripts, or files.

Web applications susceptible to direct request attacks often make the false assumption that such resources can only be reached through a given navigation path and so only apply authorization at certain points in the path.

## Mitigation:


PHASE:Architecture and Design Operation:
Apply appropriate access control authorizations for each access to all restricted URLs, scripts or files.

PHASE:Architecture and Design:
Consider using MVC based frameworks such as Struts.

