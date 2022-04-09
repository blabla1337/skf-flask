### Storing Passwords

A common need is that you are implementing a service and/or server application, and you need the user to authenticate and/or prove that they are authorized to make a request. This is called *inbound authentication*. Here are three common approaches for doing this:

1. Delegate this determination to some other service. You need to trust that other service, and you need a specification for communicating this. OAUTH and OpenID are two common specifications for making the request to the other service. Generally, you would call on a routine to implement this; make sure you apply its security guidance. This can be convenient to users, but remember that this reveals every login to that external service (a privacy concern), and make sure you can trust that service.

2. Require the requestor to have a private key that proves their identity. SSH and HTTPS both support this. A great advantage of this approach is that at the server end only a public key needs to be recorded, so while integrity is important, the confidentiality of the keys is not as critical. However, this requires that the user set up this private key.

3. Support a password-based login (at least in part).

If you implement option 3, supporting a password-based login (at least in part), you have a lot of company. Passwords have many known problems, but they are known problems. If you are going to use passwords, at least in part, you need to do it correctly.

**Beware** of storing passwords in an insecure way. A database full of password information is a tempting target for attackers. In practice, many attackers have managed to gain databases of password-related information (e.g., by breaking into the service or acquiring a backup). A secure system *must* be designed so that attackers cannot easily exploit server-side password databases, even when attackers manage to retrieve a copy. Here are some approaches that do **NOT** work:

* Storing passwords “in the clear” (unencrypted). Obviously, if an attacker gets this data, the attacker can use all the passwords. **_Don’t do this!_**

* Hashing the passwords (e.g., with SHA-256). Attackers have tools that can brute-force guess billions of passwords, hash them all, and compare them with the hashed values, so this does not protect the passwords. **_Don’t do this!_**

* Per-user salted hashes. This combines the password with a random per-user value called a “salt”, then hashes the combination. The problem is that modern hash algorithms are so fast that attackers can still guess billions of passwords and often find a user’s password. Again, **_don’t do this!_**

If you are using passwords for inbound authentication, for security you **_must_** use a special kind of algorithm for this purpose called an *iterated per-user salted cryptographic hash* algorithm. The term “iterated” is also called key derivation. Three algorithms are commonly used as an iterated per-user salted cryptographic hash algorithm:

* **Argon2id**
Unless you have a strong reason to use something else, this is the algorithm to use today. It is relatively strong against both software and hardware-based attacks.

* **Bcrypt**
This is a decent algorithm against software-based attacks. It is not as easy to attack with hardware compared to PBKDF2 (because bcrypt requires more RAM), but it is weaker against hardware-based attacks compared to Argon2id.

* **PBKDF2**
This is a decent algorithm against software-based attacks, but it is the most vulnerable of these widely-used algorithms to hardware-based attacks from specialized circuits or GPUs. That is because it can be implemented with a small circuit and little RAM. You may not need to replace it (depending on the kinds of attackers that concern you), but it is probably best to avoid this for new systems today.

Another algorithm that is in use is scrypt. This should also be strong against hardware attacks, but it has not gotten as much review compared to Argon2id, so Argon2id is more commonly recommended. That said, at the time of this writing, it has no known serious problems.

You should allow users to require the use of two-factor authentication (2FA), either directly or by delegating to a service that does.

Also, beware of implementing these algorithms only on the client side. It is fine to implement them on the client side (because that prevents the server from ever discovering the password the user enters), as long as they are *also* implemented on the server. The danger is doing them *only* on the client; if that happens, then what is stored in the server is no different from storing passwords in the clear. Once attackers get the password database, they can simply create or modify their own client to log into anyone’s account.