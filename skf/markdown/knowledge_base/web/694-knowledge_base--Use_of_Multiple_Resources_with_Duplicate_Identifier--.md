##Description:

The software uses multiple resources that can have the same identifier, in a context in which unique identifiers are required.

If the software assumes that each resource has a unique identifier, the software could operate on the wrong resource if attackers can cause multiple resources to be associated with the same identifier.

##Mitigation:


PHASE:Architecture and Design:
Where possible, use unique identifiers. If non-unique identifiers are detected, then do not operate any resource with a non-unique identifier and report the error appropriately.

