
Re-authentication
-------

**Description:**

Whenever a user is changing credentials such as his password, the user should always be 
challenged by the application to re-authenticate himself. This is in order to prevent an 
attacker to change credentials if ever an attacker could hijack another users session.

Verify that the changing password functionality includes the old password, 
the new password, and a password confirmation, as well as a passphrase strength indication
to encourage the adoption of strong passphrases.  

**Solution:**

A user should always be challenged by the application to re-authenticate themselves after 
changing their credentials, e-mail or doing other important data exchanges such as 
transferring money. You could also consider using step up, adaptive authentication or
two factor authentication, or transaction signing depending on how critical your 
application is.

Recommended knowledge base item:

- Step up or adaptive authentication

