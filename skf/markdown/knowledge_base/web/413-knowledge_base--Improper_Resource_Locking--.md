##Description:

The software does not lock or does not correctly lock a resource when the software must have exclusive access to the resource.

When a resource is not properly locked, an attacker could modify the resource while it is being operated on by the software. This might violate the software's assumption that the resource will not change, potentially leading to unexpected behaviors.

##Mitigation:


PHASE:Architecture and Design:
Use a non-conflicting privilege scheme.

PHASE:Architecture and Design Implementation:
Use synchronization when locking a resource.

