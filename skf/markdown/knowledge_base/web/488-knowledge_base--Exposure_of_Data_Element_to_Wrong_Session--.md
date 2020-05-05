## Description:

The product does not sufficiently enforce boundaries between the states of different sessions, causing data to be provided to, or used by, the wrong session.

Data can bleed from one session to another through member variables of singleton objects, such as Servlets, and objects from a shared pool. In the case of Servlets, developers sometimes do not understand that, unless a Servlet implements the SingleThreadModel interface, the Servlet is a singleton; there is only one instance of the Servlet, and that single instance is used and re-used to handle multiple requests that are processed simultaneously by different threads. A common result is that developers use Servlet member fields in such a way that one user may inadvertently see another user's data. In other words, storing user data in Servlet member fields introduces a data access race condition.

## Mitigation:


PHASE:Architecture and Design:
Protect the application's sessions from information leakage. Make sure that a session's data is not used or visible by other sessions.

PHASE:Testing:
Use a static analysis tool to scan the code for information leakage vulnerabilities (e.g. Singleton Member Field).

PHASE:Architecture and Design:
In a multithreading environment, storing user data in Servlet member fields introduces a data access race condition. Do not use member fields to store information in the Servlet.

