## Description:

Certain conditions, such as network failure, will cause a server error message to be displayed.

While error messages in and of themselves are not dangerous, per se, it is what an attacker can glean from them that might cause eventual problems.

## Mitigation:


PHASE:Architecture and Design System Configuration:
Recommendations include designing and adding consistent error handling mechanisms which are capable of handling any user input to your web application, providing meaningful detail to end-users, and preventing error messages that might provide information useful to an attacker from being displayed.

