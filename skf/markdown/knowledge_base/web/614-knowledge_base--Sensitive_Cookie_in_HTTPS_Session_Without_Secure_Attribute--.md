##Description:

The Secure attribute for sensitive cookies in HTTPS sessions is not set, which could cause the user agent to send those cookies in plaintext over an HTTP session.



##Mitigation:


PHASE:Implementation:
Always set the secure attribute when the cookie should sent via HTTPS only.

