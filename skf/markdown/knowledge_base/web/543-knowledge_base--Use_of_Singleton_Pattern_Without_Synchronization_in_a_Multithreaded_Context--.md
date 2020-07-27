##Description:

The software uses the singleton pattern when creating a resource within a multithreaded environment.

The use of a singleton pattern may not be thread-safe.

##Mitigation:


PHASE:Architecture and Design:
Use the Thread-Specific Storage Pattern. See References.

PHASE:Implementation:
Do not use member fields to store information in the Servlet. In multithreading environments, storing user data in Servlet member fields introduces a data access race condition.

PHASE:Implementation:
Avoid using the double-checked locking pattern in language versions that cannot guarantee thread safety. This pattern may be used to avoid the overhead of a synchronized call, but in certain versions of Java (for example), this has been shown to be unsafe because it still introduces a race condition (CWE-209).:EFFECTIVENESS:Limited

