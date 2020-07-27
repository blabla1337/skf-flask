##Description:

The software does not initialize a critical resource.

Many resources require initialization before they can be properly used. If a resource is not initialized, it could contain unpredictable or expired data, or it could be initialized to defaults that are invalid. This can have security implications when the resource is expected to have certain properties or values.

##Mitigation:


PHASE:Implementation:
Explicitly initialize the resource before use. If this is performed through an API function or standard procedure, follow all specified steps.

PHASE:Implementation:
Pay close attention to complex conditionals that affect initialization, since some branches might not perform the initialization.

PHASE:Implementation:
Avoid race conditions (CWE-362) during initialization routines.

PHASE:Build and Compilation:
Run or compile your software with settings that generate warnings about uninitialized variables or data.

