##Description:

The software uses OpenSSL and trusts or uses a certificate without using the SSL_get_verify_result() function to ensure that the certificate satisfies all necessary security requirements.

This could allow an attacker to use an invalid certificate to claim to be a trusted host, use expired certificates, or conduct other attacks that could be detected if the certificate is properly validated.

##Mitigation:


PHASE:Architecture and Design:
Ensure that proper authentication is included in the system design.

PHASE:Implementation:
Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

