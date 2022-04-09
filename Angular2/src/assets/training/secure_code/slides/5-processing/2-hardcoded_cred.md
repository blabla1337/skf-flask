### Avoid Default & Hardcoded Credentials

Many programs have to use some secret information. An especially common kind of secret is a *credential* (e.g., a password or secret key).  How you protect them depends on how they are used, and there are two common uses for credentials:

* **Inbound**
The software receives some credentials as input and checks if it matches to authenticate something else.

* **Outbound**
The software sends the credentials to something else to authenticate itself to something else.

#### Avoid Default Credentials

Software should never be delivered with default credentials. There are endless web pages that track default credentials like **admin/admin**. Once anyone finds the credentials, they are likely to eventually end up on these listings. This will enable attackers to break into your software (if it is an inbound credential) or others’ software (if it is an outbound credential). If the software has many installations, then they may all be vulnerable at the same time. **Remember:** Users generally accept whatever is the default, and if the default is insecure, then the software will be insecure. Obfuscating the code is not enough; many attackers are quite adept at extracting and analyzing executables.

The usual solution for this is to have a “first login” mode that detects that there is no credential (password or key) yet, and then lets the user create a unique one. That is assuming it needs to be stored at all; in some cases, you can simply ask the user to provide it each time.

#### Avoid Hardcoded Credentials, Store Them Safely Instead

Hardcoded credentials are credentials stored within the source code, compiled code, or any other location that cannot be quickly changed by someone authorized to do so.

Hardcoded credentials are mistakes. Credentials should be changed whenever the software is first installed for use and should be easy and quick to change. Storing credentials in source code is a particularly bad idea. Source code is typically managed by version control systems, so any credentials in the code will become available to anyone with access to that source code … and that is often far more people than need to know. Encoding this information in a way that can be undone (e.g., using Base64 or ROT13) doesn’t help.

So: don’t hardcode credentials (e.g., within source code or compiled code). Instead, store credentials separately in a way that makes them easy to change. Public key certificates usually don’t need to be kept secret, but they may need to be updated. Other credentials often need to be kept secret, and should be protected at least as much as necessary. As we will briefly discuss later, there are tools that may help you identify hardcoded credentials in source code.

For inbound authentication using passwords, store credentials separately and use a secure algorithm specifically designed for encoding them. We will discuss this in more detail later in the section on Cryptography, but for now, just know that you need to use an *iterated per-user salted cryptographic hash* algorithm such as Argon2id.

For outbound authentication, credentials should be stored outside the code in a storage system that is protected from all outsiders (including local users on the same system/cloud host). Ideally, all credentials would be stored in an encrypted file or database, but in many environments, this is difficult to do (where do you store the key to access the key?). At the very least, store credentials in something like a file or database table with permissions that are as restrictive as you can practically make them. Environment variables are generally a weaker way to store credentials, since their values are available to the entire process that loads them, but in some circumstances this is acceptable… and it is generally much better than hardcoding credentials.

Hardcoded credentials are such a common cause of security vulnerabilities that they are 2019 CWE Top 25 #19. This weakness is [CWE-798](https://cwe.mitre.org/data/definitions/798.html), *Use of Hard-coded Credentials*. *Insufficiently Protected Credentials* are 2019 CWE Top 25 #27 as [CWE-522](https://cwe.mitre.org/data/definitions/522.html).