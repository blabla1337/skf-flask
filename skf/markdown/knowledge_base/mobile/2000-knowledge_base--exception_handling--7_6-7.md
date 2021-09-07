## Description:

Exception Handling

MSTG-CODE-6: The app catches and handles possible exceptions.

MSTG-CODE-7: Error handling logic in security controls denies access by default.

Exceptions often occur after an application enters an abnormal or erroneous state. Testing exception handling is about making sure that the application will handle the exception and get into a safe state without exposing any sensitive information via its logging mechanisms or the UI.


## Mitigation:

Review the source code to understand how the application handles various types of errors (IPC communications, remote services invocation, etc.).

Make sure that the application uses a well-designed and unified scheme to handle exceptions.

Make sure that the application doesn't expose sensitive information while handling exceptions in its UI or log-statements. Ensure that exceptions are still verbose enough to explain the issue to the user.

