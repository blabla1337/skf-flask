##Description:

In order to establish trust between two communicating party's such as servers and clients
there message payload should be signed by means of public/private key method. This builds trust
and makes it harder for attackers to impersonate different users.

Web Services Security (WS-Security, WSS) is an extension to SOAP to apply security to 
Web services. It is a member of the Web service specifications and was published by OASIS.

The protocol specifies how integrity and confidentiality can be enforced on messages and allows 
the communication of various security token formats, such as Security Assertion Markup Language (SAML), 
Kerberos, and X.509. Its main focus is the use of XML Signature and XML Encryption to provide end-to-end security.

##Mitigation:

WS-Security describes three main mechanisms:

How to sign SOAP messages to assure integrity. Signed messages also provide non-repudiation.
How to encrypt SOAP messages to assure confidentiality.
How to attach security tokens to ascertain the sender's identity.
The specification allows a variety of signature formats, encryption algorithms and multiple trust domains, and is open to various security token models, such as:

X.509 certificates,
Kerberos tickets,
User ID/Password credentials,
SAML Assertions, and
custom-defined tokens.
The token formats and semantics are defined in the associated profile documents.

WS-Security incorporates security features in the header of a SOAP message, working in the application layer.

These mechanisms by themselves do not provide a complete security solution for Web services. Instead, this specification is a building block that can be used in conjunction with other Web service extensions and higher-level application-specific protocols to accommodate a wide variety of security models and security technologies. In general, WSS by itself does not provide any guarantee of security. When implementing and using the framework and syntax, it is up to the implementor to ensure that the result is not vulnerable.

Key management, trust bootstrapping, federation and agreement on the technical details (ciphers, formats, algorithms) is outside the scope of WS-Security.

### Use cases:

End-to-end security
If a SOAP intermediary is required, and the intermediary is not more or less trusted, messages need to be signed and optionally encrypted. This might be the case of an application-level proxy at a network perimeter that will terminate TCP (transmission control protocol) connections.

Non-repudiation
One method for non-repudiation is to write transactions to an audit trail that is subject to specific security safeguards. Digital signatures, which WS-Security supports, provide a more direct and verifiable non-repudiation proof.

Alternative transport bindings
Although almost all SOAP services implement HTTP bindings, in theory other bindings such as JMS or SMTP could be used; in this case end-to-end security would be required.

Reverse proxy/common security token
Even if the web service relies upon transport layer security, it might be required for the service to know about the end user, if the service is relayed by a (HTTP-) reverse proxy. A WSS header could be used to convey the end user's token, vouched for by the reverse proxy.


