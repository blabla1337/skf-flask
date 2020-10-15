##Description:

The primairy authentication mechanism is most often a good hardened functionality
because it gets a lot of attention during development. However, this is mostly not the
case for secondary authentication mechanisms such as password forget functions, or 
other alternative paths that could lead to authenticating to the target application.

##Mitigation:

Verify all account identity authentication functions (such as update profile, forgot password, 
disabled / lost token, help desk or IVR) that might regain access to the account are 
at least as resistant to attack as the primary authentication mechanism.
