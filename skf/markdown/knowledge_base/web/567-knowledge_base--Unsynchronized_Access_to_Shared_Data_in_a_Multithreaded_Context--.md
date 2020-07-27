##Description:

The product does not properly synchronize shared data, such as static variables across threads, which can lead to undefined behavior and unpredictable data changes.

Within servlets, shared static variables are not protected from concurrent access, but servlets are multithreaded. This is a typical programming mistake in J2EE applications, since the multithreading is handled by the framework. When a shared variable can be influenced by an attacker, one thread could wind up modifying the variable to contain data that is not valid for a different thread that is also using the data within the variable. Note that this weakness is not unique to servlets.

##Mitigation:


PHASE:Implementation:
Remove the use of static variables used between servlets. If this cannot be avoided, use synchronized access for these variables.

