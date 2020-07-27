##Description:

Thread management in a Web application is forbidden in some circumstances and is always highly error prone.

Thread management in a web application is forbidden by the J2EE standard in some circumstances and is always highly error prone. Managing threads is difficult and is likely to interfere in unpredictable ways with the behavior of the application container. Even without interfering with the container, thread management usually leads to bugs that are hard to detect and diagnose like deadlock, race conditions, and other synchronization errors.

##Mitigation:


PHASE:Architecture and Design:
For EJB, use framework approaches for parallel execution, instead of using threads.

