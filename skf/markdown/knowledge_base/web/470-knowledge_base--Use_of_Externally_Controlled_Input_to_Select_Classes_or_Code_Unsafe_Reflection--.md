##Description:

The application uses external input with reflection to select which classes or code to use, but it does not sufficiently prevent the input from selecting improper classes or code.

If the application uses external inputs to determine which class to instantiate or which method to invoke, then an attacker could supply values to select unexpected classes or methods. If this occurs, then the attacker could create control flow paths that were not intended by the developer. These paths could bypass authentication or access control checks, or otherwise cause the application to behave in an unexpected manner. This situation becomes a doomsday scenario if the attacker can upload files into a location that appears on the application's classpath (CWE-427) or add new entries to the application's classpath (CWE-426). Under either of these conditions, the attacker can use reflection to introduce new, malicious behavior into the application.

##Mitigation:


PHASE:Architecture and Design:
Refactor your code to avoid using reflection.

PHASE:Architecture and Design:
Do not use user-controlled inputs to select and load classes or code.

PHASE:Implementation:
Apply strict input validation by using whitelists or indirect selection to ensure that the user is only selecting allowable classes or code.

