## Description:

Whenever a user is changing credentials such as his password, the user should always be
challenged by the application to re-authenticate himself. This is in order to prevent an
attacker from changing credentials if ever an attacker could hijack another users session.

## Solution:

Verify that the changing password functionality includes the old password,
the new password, and a password confirmation, as well as a passphrase strength indication
to encourage the adoption of strong password phrases. This same principle applies for other operations
that are considered critical such as changing an email adress or phone number.
