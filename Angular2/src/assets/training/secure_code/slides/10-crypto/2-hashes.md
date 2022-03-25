### Cryptographic Hashes (Digital Fingerprints)

Some programs need a one-way cryptographic hash algorithm, that is, a function that takes an *arbitrary* amount of data and generates a fixed-length number with special properties. The special properties are that it must be infeasible for an attacker to create:

1. Another message with a given hash value (*preimage resistance*)

2. Another (modified) message with same hash as the first message (*second preimage resistance*)

3. Any two messages with the same hash (*collision resistance*).

The idea is that you can represent an arbitrary amount of data with a smaller value of fixed length. They are “*one-way*” in the sense that you cannot generally recreate the original data given only the hash value. Cryptographic hashes are useful by themselves, and they are also often used as part of larger cryptographic systems.

You should avoid the algorithms MD4, MD5, and SHA-0, as these are known to be broken.

The SHA-2 family (including SHA-256 and SHA-512) and the SHA-3 algorithm are widely used and generally considered secure at the time of this writing. There have been concerns about the SHA-2 family, leading to the development of SHA-3, but as of this writing no full break of SHA-2 has been publicly reported.

The SHA-1 algorithm is a slightly more complicated case. You should not use it in new systems, and should be moving away from it immediately if you are currently using it. NIST deprecated SHA-1 in 2011 because it is basically broken, in the sense that SHA-1 no longer meets the definition of a cryptographic hash. In most cases, it is no problem to switch from SHA-1 to SHA-2 or SHA-3.

However, one annoying problem is that the widely-used git tool (as originally developed) fundamentally depends on SHA-1. The currently-known breaks in SHA-1 don’t matter for common situations. In addition, as of 2020, git uses a hardened variant of SHA-1 that counters the main problems with SHA-1 as it is used within git. However, attacks only get stronger, not weaker, leading to many concerns about the use of SHA-1 in git.

As of this writing, there is an effort to update git so it will support a different cryptographic hash algorithm, specifically SHA-256. This has been complicated because git was not originally designed to support another cryptographic hash algorithm ([A new hash algorithm for Git](https://lwn.net/Articles/811068/), by Jonathan Corbet, 2020). As noted in LWN.net, *“one of the reasons this transition has been so hard is that the original Git implementation was not designed to swap out hashing algorithms. Much of the work to [implement SHA-256 in git] has been walking back this initial design flaw [to make] Git fundamentally indifferent to the hashing algorithm used. This [work] should make Git more adaptable in the future should the need to replace SHA-256 with something stronger arise”* ([Updating the Git protocol for SHA-256](https://lwn.net/Articles/823352/), by John Coggeshall, 2020).

This may be resolved in git by the time you read this. However, the main point is to learn from this mistake. As noted earlier, cryptographic systems (such as algorithms and protocols) *are* occasionally broken, so you must be prepared to replace them.