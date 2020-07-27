##Description:

Automatic filtering via a Struts bean has been turned off, which disables the Struts Validator and custom validation logic. This exposes the application to other weaknesses related to insufficient input validation.



##Mitigation:


PHASE:Implementation:
Ensure that an action form mapping enables validation. Set the validate field to true.

