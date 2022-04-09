### Transport Layer Security (TLS)

Transport Layer Security (TLS) is a widely-used cryptographic protocol to provide security over a network between two parties. It provides privacy and integrity between those parties. TLS version 1.3 was released in 2018. An older and insecure version of this protocol was named Secure Sockets Layer (SSL), and sometimes the terms are used interchangeably. When you use **https://** in a web browser or server today, you are normally using TLS (in rare cases, you might be using its insecure predecessor, SSL). TLS is also used in other applications, for example, to protect exchanges of email between different Mail Transport Agents (MTAs).

#### Certificate Validation

To use TLS properly, the server side at least needs a certificate (so it can prove to potential clients that it is the system it claims to be). You can create a certificate yourself and install its public key on each client (e.g., web browser) who will connect to that server. That is fine for testing, but in most other situations, that is too complicated. In most cases (other than testing) you should get a certificate assigned by a certificate authority. You can get free certificates from [Let’s Encrypt](https://letsencrypt.org/). If the requirements of Let’s Encrypt don’t suit your needs, other certificate authorities may be useful to you.

When clients connect to a server using TLS, the client normally needs to check that the certificate is valid. Web browsers have long worked this out; web browsers come with a configurable set of certificate authority public keys (directly or via the operating system) and automatically verify each new TLS connection.

*Beware*: If you are using your own client, instead of using a web browser, double-check that you are using the TLS library API *correctly*. Many TLS library APIs do *not* fully verify the server’s TLS certificate automatically. For example, they may allow connections to a server when there is no server certificate, they may allow any certificate (instead of a certificate for the site you are trying to connect to), or allow expired certificates. This is an extremely common mistake ([*The Most Dangerous Code in the World: Validating SSL Certificates in Non-Browser Software*](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf), by Martin Georgiev, Subodh Iyengar, Suman Jana, Rishita Anubhai, Dan Boneh, and Vitaly Shmatikov, 2012). If this is the case, you may be using a low-level TLS API instead of the API you should be using.

🔔 Improper certificate validation is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #25. It is identified as [CWE-295](https://cwe.mitre.org/data/definitions/295.html), *Improper Certificate Validation*.

#### Ciphersuites

TLS, as a protocol, combines many of the pieces we have discussed. At the beginning of communication, the two sides must negotiate to determine the set of algorithms (including key lengths) that will be used for its connection. This set of algorithms is called the *ciphersuite*. That means that, for security, it is important to have good default configurations and to have the software configured correctly when deploying it.

If you are configuring an HTTPS site, a great place to get currently-recommended settings is [Mozilla’s ](https://wiki.mozilla.org/Security/Server_Side_TLS) [*Security/Server Side TLS*](https://wiki.mozilla.org/Security/Server_Side_TLS)[ site](https://wiki.mozilla.org/Security/Server_Side_TLS). A key decision for you to make is if you want the modern, intermediate, or old configuration:

* Modern: Most secure, but a non-trivial number of clients might not be able to connect to it.

* Intermediate: A compromise setting that allows slightly older clients to connect while providing reasonably good security.

* Old: A setting that provides the best possible security that supports much older clients and libraries. Its security is much weaker than intermediate.

At the time of this writing, the *intermediate setting* is recommended in most cases, but check that website for updates.

You will notice that any configuration has a list of TLS ciphersuites in order of preference. For example, the `TLS_AES_128_GCM_SHA256` means that TLS is to use the Advanced Encryption Standard (AES) with 128-bit key in Galois/Counter mode (GCM) combined with the secure hash algorithm with 256 bits (SHA-256).

Once you have deployed your system, you should test it. If the site is publicly visible, it is a great idea to use the free Qualys test called the [SSL Server Test](https://www.ssllabs.com/ssltest/). It is called the SSL Server Test because that is the old name for TLS, but don’t be fooled, it works well with TLS (and will complain if you allow the vulnerable SSL protocols).