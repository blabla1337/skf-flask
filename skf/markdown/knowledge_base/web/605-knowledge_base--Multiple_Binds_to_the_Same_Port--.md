## Description:

When multiple sockets are allowed to bind to the same port, other services on that port may be stolen or spoofed.

On most systems, a combination of setting the SO_REUSEADDR socket option, and a call to bind() allows any process to bind to a port to which a previous process has bound with INADDR_ANY. This allows a user to bind to the specific address of a server bound to INADDR_ANY on an unprivileged port, and steal its UDP packets/TCP connection.

## Mitigation:


PHASE:Policy:
Restrict server socket address to known local addresses.

