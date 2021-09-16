## Description:

Enforcing updates

MSTG-ARCH-9: A mechanism for enforcing updates of the mobile app exists.

Enforced updating can be really helpful when it comes to public key pinning (see the Testing Network communication for more details) when a pin has to be refreshed due to a certificate/public key rotation. Next, vulnerabilities are easily patched by means of forced updates.

Please note that newer versions of an application will not fix security issues that are living in the backends to which the app communicates. Allowing an app not to communicate with it might not be enough. Having proper API-lifecycle management is key here. Similarly, when a user is not forced to update, do not forget to test older versions of your app against your API and/or use proper API versioning.


## Mitigation:

Implement a proper update mechanism for application maintenance and fixing security issues.
