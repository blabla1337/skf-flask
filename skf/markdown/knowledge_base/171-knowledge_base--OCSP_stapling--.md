## Description:

OCSP stapling, formally known as the TLS Certificate Status Request extension, is an
alternative approach to the Online Certificate Status Protocol (OCSP) for checking the
revocation status of X.509 digital certificates. It allows the presenter of a
certificate to bear the resource cost involved in providing OCSP responses by appending
("stapling") a time-stamped OCSP response signed by the CA to the initial TLS Handshake,
eliminating the need for clients to contact the CA

## Solution:

Stapling basically means that the certificate holder queries the OCSP server themselves at
regular intervals, obtaining a signed time-stamped OCSP response. When the site's visitors
attempt to connect to the site, this response is included ("stapled") with the TLS/SSL
Handshake via the Certificate Status Request extension response (note: the TLS client must
explicitly include a Certificate Status Request extension in its ClientHello TLS/SSL
handshake message). While it may appear that allowing the site operator to control
verification responses would allow a fraudulent site to issue false verification for a
revoked certificate, the stapled responses can't be forged as they need to be directly
signed by the certificate authority, not the server. If the client does not receive a
stapled response, it will just contact the OCSP server by itself. However, if the
client receives an invalid stapled response, it will abort the connection. The only
increased risk of OCSP stapling is that the notification of revocation for a certificate
may be delayed until the last-signed OCSP response expires.

For more detailed information about Specification, Deployment, and limitation visit:
https://en.wikipedia.org/wiki/OCSP_stapling
