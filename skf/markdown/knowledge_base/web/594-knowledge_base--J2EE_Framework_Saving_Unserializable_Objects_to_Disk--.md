## Description:

When the J2EE container attempts to write unserializable objects to disk there is no guarantee that the process will complete successfully.

In heavy load conditions, most J2EE application frameworks flush objects to disk to manage memory requirements of incoming requests. For example, session scoped objects, and even application scoped objects, are written to disk when required. While these application frameworks do the real work of writing objects to disk, they do not enforce that those objects be serializable, thus leaving the web application vulnerable to crashes induced by serialization failure. An attacker may be able to mount a denial of service attack by sending enough requests to the server to force the web application to save objects to disk.

## Mitigation:


PHASE:Architecture and Design Implementation:
All objects that become part of session and application scope must implement the java.io.Serializable interface to ensure serializability of containing objects.

