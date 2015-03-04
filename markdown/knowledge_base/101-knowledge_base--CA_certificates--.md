
CA certificates
-------

**Description:**

In cryptography, a certificate authority or certification authority (CA) is an entity that issues digital certificates. A digital certificate certifies the ownership of a public key by the named subject of the certificate. Sometimes it happens that a CA goes bad and is revoked from the browser. This will lead to untrusted TLS connections if your application uses an issued certificate from this CA.

**Solution:**

It&#39;s always a good idea to let multiple CA you trust create a certificate, best way is that you create yourself the key pair (pub &amp; priv) and let the CA sign it. This way you don&#39;t need to &#39;leak&#39; your priv key and you have backup trusted certificates you can use as a backup when one goes &#39;bad&#39;.

	