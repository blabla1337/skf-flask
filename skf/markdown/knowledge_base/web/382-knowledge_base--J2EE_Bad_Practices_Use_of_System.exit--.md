## Description:

A J2EE application uses System.exit(), which also shuts down its container.

It is never a good idea for a web application to attempt to shut down the application container. Access to a function that can shut down the application is an avenue for Denial of Service (DoS) attacks.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Separation of Privilege:
The shutdown function should be a privileged function available only to a properly authorized administrative user

PHASE:Implementation:
Web applications should not call methods that cause the virtual machine to exit, such as System.exit()

PHASE:Implementation:
Web applications should also not throw any Throwables to the application server as this may adversely affect the container.

PHASE:Implementation:
Non-web applications may have a main() method that contains a System.exit(), but generally should not call System.exit() from other locations in the code

