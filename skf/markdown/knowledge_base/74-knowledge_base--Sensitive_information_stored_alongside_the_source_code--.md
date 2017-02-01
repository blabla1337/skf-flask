Sensitive information stored alongside the source code
-------

**Description:**

Sometimes when developing an application a programmer stores a password or other
credentials into the source-code as a comment for other developers to
login into the application. When these comments still exist in a live environment,
an attacker could use these credentials to gain access to the system.


**Solution:**

Search your source code for comments which contains possible user-credentials.
You should also verify that there are no secrets and API keys are included in the
source code, or end up within the resulting binary.

This also goes for providing information about business logic and other critical sensitive
information. Verify that there is no sensitive business logic, secret keys or other
proprietary information in client side code.
