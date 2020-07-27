##Description:

When setting a new password for a user, the product does not require knowledge of the original password, or using another form of authentication.

This could be used by an attacker to change passwords for another user, thus gaining the privileges associated with that user.

##Mitigation:


PHASE:Architecture and Design:
When prompting for a password change, force the user to provide the original password in addition to the new password.

PHASE:Architecture and Design:
Do not use forgotten password functionality. But if you must, ensure that you are only providing information to the actual user, e.g. by using an email address or challenge question that the legitimate user already provided in the past; do not allow the current user to change this identity information until the correct password has been provided.

