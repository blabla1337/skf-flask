## Description:

Custom Certificate Stores and Certificate Pinning

MSTG-NETWORK-4: The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.

Certificate Authorities are an integral part of a secure client server communication and they are predefined in the trust store of each operating system.

CAs can be added to the trust store, either manually through the user, by an MDM that manages your enterprise device or through malware. The question is then can I trust all of those CAs and should my app rely on the trust store?

In order to address this risk you can use certificate pinning. Certificate pinning is the process of associating the mobile app with a particular X.509 certificate of a server, instead of accepting any certificate signed by a trusted certificate authority. A mobile app that stores the server certificate or public key will subsequently only establish connections to the known server, thereby "pinning" the server. By removing trust in external certificate authorities (CAs), the attack surface is reduced. After all, there are many known cases where certificate authorities have been compromised or tricked into issuing certificates to impostors. 

The certificate can be pinned and hardcoded into the app or retrieved at the time the app first connects to the backend. In the latter case, the certificate is associated with ("pinned" to) the host when the host is seen for the first time. This alternative is less secure because attackers intercepting the initial connection can inject their own certificates.


## Mitigation:

Verify that the server certificate is pinned. Pinning can be implemented on various levels in terms of the certificate tree presented by the server:
	1. Including server's certificate in the application bundle and performing verification on each connection. This requires an update mechanisms whenever the certificate on the server is updated.
	2. Limiting certificate issuer to e.g. one entity and bundling the intermediate CA's public key into the application. In this way we limit the attack surface and have a valid certificate.
	3. Owning and managing your own PKI. The application would contain the intermediate CA's public key. This avoids updating the application every time you change the certificate on the server, due to e.g. expiration. Note that using your own CA would cause the certificate to be self-singed.