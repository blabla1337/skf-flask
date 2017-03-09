# Signed application components
-------

## Description:

When an application don't use signed application components an attacker can easily modify parts
of the application and load inject a backdoor into the application. Also the attacker could
modify business logic in the application without the application notice. Signed application
components can help harden your application and make it noticeable when an attacker tries to
modify the code in the application.


## Solution:

Create for the different components in the application signed signatures and verify these in
the application at starting of the application and at run-time level.
