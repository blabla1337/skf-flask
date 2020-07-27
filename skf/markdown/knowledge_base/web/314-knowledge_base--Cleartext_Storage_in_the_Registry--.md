##Description:

The application stores sensitive information in cleartext in the registry.

Attackers can read the information by accessing the registry key. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

##Mitigation:
