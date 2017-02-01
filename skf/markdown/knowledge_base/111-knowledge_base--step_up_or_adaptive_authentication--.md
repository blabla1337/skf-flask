Step up or adaptive authentication
-------

**Description:**

Whenever a user browses a section of a web based application that contains sensitive
information the user should be challenged authenticate again using a higher assurance
credential to be granted access to this information.


**Solution:**

Verify the application has additional authorization
(such as step up or adaptive authentication) so the user is challenged before being
granted access to sensitive information. This rule also applies for making critical
changes to an account or action.

This also means that the adaptation of authentication has
to be implemented in such a manner that the application correctly enforces context-sensitive
authorization so as to not allow unauthorized manipulation by means of in example, parameter tampering.
