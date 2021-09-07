## Description:

Endpoint Identify Verification

MSTG-NETWORK-3: The app verifies the X.509 certificate of the remote endpoint when the secure channel is established. Only certificates signed by a trusted CA are accepted.

Using TLS to transport sensitive information over the network is essential for security. However, encrypting communication between a mobile application and its backend API is not trivial. Developers often decide on simpler but less secure solutions (e.g., those that accept any certificate) to facilitate the development process, and sometimes these weak solutions [make it into the production version](https://saschafahl.de/static/paper/androidssl2012.pdf "Hunting Down Broken SSL in Android Apps"), potentially exposing users to [man-in-the-middle attacks](https://cwe.mitre.org/data/definitions/295.html "CWE-295: Improper Certificate Validation").


## Mitigation:

Two key issues should be addressed:
	- Verify that a certificate comes from a trusted source, i.e. a trusted CA (Certificate Authority).
	- Determine whether the endpoint server presents the right certificate.

Make sure that the hostname and the certificate itself are verified correctly.