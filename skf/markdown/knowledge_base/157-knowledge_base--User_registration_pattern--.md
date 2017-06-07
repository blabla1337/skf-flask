# User registration - pattern
-------

## Description:

Whenever you allow users to register on your system there are a couple of things you need
to take into consideration in order to enforce a high level of security
For more detailed information about these items you should check the knowledge-base about:

1.	Column Truncation SQL injection(for MySQL databases)
2.	Single input validation controls
3.	Audit logs
4.	Prevent password leaking
5.	Predictable password and or token generation
6.	Are all passwords hashed, salted and stretched
7.	Does the application enforce the use of secure passwords?


## Solution:

The items as pointed out before should be looked into and taken into consideration
whenever you are letting users register on your system in order to enforce a
high level of security.

Here are the steps described briefly.
For more detailed information you should look into these items in the knowledge base.

First, You enforce limits on the length of the users submits on the server side in order
to prevent him from truncating his submits. These limits have to correlate with the limits
you set in your column in the database.

Second, you should create a single user input validation control class which should
validate the expected input values in order to verify if the user is not tampering data
or injecting malicious code into your application. All infringements should be logged
and repercussions should be taken whenever these infringements are frequent.

Third, never display the user’s password on a screen anywhere.

Fourth, Whenever you generate a password for your users, this password should always
be randomized sufficiently.

Fifth, encrypt your passwords by proven cryptographic standards when storing them.

Sixth, Enforce secure passwords by implementing good password policies.
