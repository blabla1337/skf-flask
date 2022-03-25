### Other Topics in Cryptography

#### Getting Cryptographic Advice

In this course, we have tried to give some basics and enough information to apply them in various circumstances. Perhaps most important, however, are the key pieces of advice: do not create your own cryptographic algorithms or protocols, and do not create your own implementations. Instead, reuse well-respected algorithms, protocols, and implementations. When configuring cryptography, look for current well-respected advice. Examples of such sources include Mozilla’s [Security/Server Side TLS site](https://wiki.mozilla.org/Security/Server_Side_TLS), NIST (especially NIST’s [*Recommendation for Key Management: Part 1 - General*](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf)), and CISCO’s [*Next Generation Cryptography*](https://tools.cisco.com/security/center/resources/next_generation_cryptography). Cryptographers won’t always agree on what is “best” (as with any other field), but experts will be able to point out what is clearly broken and what is widely agreed to be much safer.

#### Constant Time Algorithms

There is an important topic that we have not mentioned yet: constant-time algorithms, especially constant-time comparisons. Many algorithms take a variable amount of time depending on their data. For example, if you want to determine if two arrays are equal, usually that comparison would stop on the first unequal value.

Those who develop cryptographic libraries must implement their algorithms so that the time they take does not vary based on their input data (this is non-trivial, though possible, with AES). Most developers are never taught how to do this, so this is one of many reasons you should not write your own cryptographic library. However, there is a variation that can often happen outside of these libraries: sometimes you have to handle array comparisons specially.

The normal comparison operations (such as **is-equal**) try to minimize execution time, and this can sometimes leak timing information about the values to attackers. If an attacker could repeatedly send in data and notice that a comparison of a value beginning with “0” takes longer than one that does not, then the first value it is compared to must be “0”. The attacker can then repeatedly guess the second digit, then the third, and so on. Many developers incorrectly believe that it is not possible for attackers to exploit timing variations over a network; this is a false belief attackers love to exploit. Modern statistics turns out to be remarkably powerful for removing latency variances; attackers really *can* exploit these latencies.

*Constant-time comparisons* are comparisons (usually equality) that take the same time no matter what data is provided to them. These are not the same as O(1) operations in computer science. Examples of these constant-time comparison functions are:

* Node.js: **crypto.timingSafeEqual**

* Ruby on Rails: **ActiveSupport::SecurityUtils secure_compare** and **fixed_length_secure_compare**

* Java: **MessageDigest.equal** (assuming you are not using an ancient version of Java)

Whenever you compare secret values or cryptographic values (such as session keys), use a *constant-time comparison* instead of a normal comparison unless an attacker cannot exploit the normal comparison timing. You don’t need to do this with an iterated salted hash computed in a trusted environment (such as your server), because it will take an attacker too much time to create the matching values. You *do* need to do this if you are directly comparing session keys to a stored value, since attackers *can* sometimes iterate this to figure out each digit in the session key.

#### Minimizing the Time Keys/Decrypted Data Exists

Remember that per least privilege, we want to minimize the time a privilege is active. In cryptography, you often want to minimize the time a private key or password is available, or at least minimize the time that the decrypted data is available. This can be harder that you might think. At the operating system level you can probably lock it into memory with **mlock()** or **VirtualLock()**; this will at least prevent the data from being copied into storage. Ideally, you would erase it from memory after use, though that is often surprisingly difficult. Compilers may turn overwrite code into a no-op, because they detect that nothing reads the overwritten values. Languages with built-in garbage collection often quietly make extra copies and/or do not provide a mechanism for erasure. That said, some languages or infrastructure do make this easy. For example, those using the .NET framework (e.g., C#) can use SecureString.

#### Quantum Computing

One of the large future unknowns in cryptography is the potential impact of general-purpose quantum computers. At the time of this writing, so-called *general-purpose* quantum computers exist, but they are not powerful enough to threaten current cryptographic algorithms. It is not known if such more powerful general-purpose quantum computers can be built, and if so, when that will happen. If strong general-purpose quantum computers are built, they have the potential to break all the public-key algorithms that are popular in 2020 by using an algorithm called *Shor’s algorithm*. As a result, researchers are developing new public-key algorithms that resist attacks from such quantum computers, an area called *post-quantum cryptography*. At the time of this writing, many such algorithms have been developed and are being evaluated.

In contrast, current symmetric cryptographic algorithms and hash functions are less affected by quantum computers. Grover’s algorithm speeds up attacks against symmetric ciphers, halving their effective length. That means that 128-bit AES could be broken by a quantum computer (it would then be equivalent to a 64-bit key today), but 256-bit AES would still be secure (it would be equivalent to a 128-bit key today). So simply using longer keys and hashes is expected to be adequate in a post-quantum world for symmetric cryptographic algorithms and hash functions.

#### Humility Is Important in Cryptography

Perhaps the most important lesson here is to be humble when using cryptography. Many cryptographic algorithms have been developed in the past, only to be broken later. It is hubris to think that our current algorithms and protocols cannot be broken.

You should instead have a plan for handling when (not if) your cryptographic algorithms and protocols are broken. Make sure all your co-developers learn of this plan so that they will not ruin it (e.g., if you run an OSS project, put this in the **CONTRIBUTING.md** or equivalent file). In short, plan for change.

Similarly, seek advice from experts, and weigh that advice carefully. Errors in cryptographic systems can be devastating, and can last for many years because they are not obvious. Getting others’ review and constructive feedback is generally a good idea, but it is especially important when using cryptography.