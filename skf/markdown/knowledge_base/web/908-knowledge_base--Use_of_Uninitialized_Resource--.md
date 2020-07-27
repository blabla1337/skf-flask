##Description:

The software uses or accesses a resource that has not been initialized.

When a resource has not been properly initialized, the software may behave unexpectedly. This may lead to a crash or invalid memory access, but the consequences vary depending on the type of resource and how it is used within the software.

##Mitigation:


PHASE:Implementation:
Explicitly initialize the resource before use. If this is performed through an API function or standard procedure, follow all required steps.

PHASE:Implementation:
Pay close attention to complex conditionals that affect initialization, since some branches might not perform the initialization.

PHASE:Implementation:
Avoid race conditions (CWE-362) during initialization routines.

PHASE:Build and Compilation:
Run or compile the software with settings that generate warnings about uninitialized variables or data.

