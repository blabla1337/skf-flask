##Description:

The application stores a non-serializable object as an HttpSession attribute, which can hurt reliability.

A J2EE application can make use of multiple JVMs in order to improve application reliability and performance. In order to make the multiple JVMs appear as a single application to the end user, the J2EE container can replicate an HttpSession object across multiple JVMs so that if one JVM becomes unavailable another can step in and take its place without disrupting the flow of the application. This is only possible if all session data is serializable, allowing the session to be duplicated between the JVMs.

##Mitigation:


PHASE:Implementation:
In order for session replication to work, the values the application stores as attributes in the session must implement the Serializable interface.

