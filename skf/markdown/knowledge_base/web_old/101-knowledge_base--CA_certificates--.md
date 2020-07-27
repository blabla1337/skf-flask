##Description:

In cryptography, a certificate authority or certification authority (CA) is an entity that
issues digital certificates. A digital certificate certifies the ownership of a public key
by the named subject of the certificate. Sometimes it happens that a CA goes bad and is
revoked from the browser. This will lead to untrusted TLS connections if your application
uses an issued certificate from this CA.

A self-signed certificate is an identity certificate that is signed by the same entity whose identity it certifies. This term has nothing to do with the identity of the person or organization that actually performed the signing procedure. In technical terms a self-signed certificate is one signed with its own private key.

In typical public key infrastructure (PKI) arrangements, a digital signature from a certificate authority (CA) attests that a particular public key certificate is valid. Each CA has one or more root keys; and the certificates associated with those public keys are "trust anchors" that use a special type of self-signed certificates. Establishing trust of the CA root certificate is dependent upon procedures beyond checking its digital signature.

## Solution:

In a CA based PKI system, the CA must be trusted by both parties. This is usually accomplished by placing the CA certificates in a whitelist of trusted certificates. For example, web browsers developers may use procedures specified by the CA/Browser Forum, or a private CA's certificate may be placed in the firmware of an embedded system. The trust issues of an entity accepting a new self-signed certificate, is similar to the issues of an entity trusting the addition of a new CA certificate. The parties in a self-signed PKI must establish trust with each other (using procedures outside the PKI), and confirm the accurate transfer of public keys (e.g. compare the hash out of band).

There are many subtle differences between CA signed and self-signed certificates, especially in the amount of trust that can be placed in the security assertions of the certificate. Some CAs can verify the identity of the person to whom they issue a certificate; for example the US military issues their Common Access Cards in person, with multiple forms of other ID. The CA can attest identity values like these by including them in the signed certificate. The entity that validates the certificate can trust the information in that certificate, to the same extent that they trust the CA that signed it (and by implication, the security procedures the CA used to verify the attested information).

With a self-signed certificate by contrast, trust of the values in the certificate are more complicated because the entity possesses the signing key, and can always generate a new certificate with different values. For example, the validity dates of a self-signed certificate might not be trusted because the entity could always create and sign a new certificate that contained a valid date range. The values in a self-signed certificate can be trusted when the following conditions are true: the values were (out-of-band) verified when the self-signed was formally trusted, and there is a method to verify the self-signed certificate has not changed after it was trusted. For example, the procedure of trusting a self-signed certificate includes a manual verification of validity dates, and a hash of the certificate is incorporated into the white list. When the certificate is presented for an entity to validate, they first verify the hash of the certificate matches the reference hash in the white-list, and if they match (indicating the self-signed certificate is the same as the one that was formally trusted) then the certificate's validity dates can be trusted. Special treatment of X.509 certificate fields for self-signed certificate can be found in RFC 3280.

Verify that connections to and from the server use trusted TLS certificates. Where internally generated or self-signed certificates are used, the server must be configured to only trust specific internal CAs and specific self-signed certificates. All others should be rejected.
