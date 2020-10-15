##Description:

The software uses a one-way cryptographic hash against an input that should not be reversible, such as a password, but the software does not also use a salt as part of the input.

This makes it easier for attackers to pre-compute the hash value using dictionary attack techniques such as rainbow tables. It should be noted that, despite common perceptions, the use of a good salt with a hash does not sufficiently increase the effort for an attacker who is targeting an individual password, or who has a large amount of computing resources available, such as with cloud-based services or specialized, inexpensive hardware. Offline password cracking can still be effective if the hash function is not expensive to compute; many cryptographic functions are designed to be efficient and can be vulnerable to attacks using massive computing resources, even if the hash is cryptographically strong. The use of a salt only slightly increases the computing requirements for an attacker compared to other strategies such as adaptive hash functions. See CWE-916 for more details.

##Mitigation:


PHASE:Architecture and Design:
Use an adaptive hash function that can be configured to change the amount of computational effort needed to compute the hash, such as the number of iterations (stretching) or the amount of memory required. Some hash functions perform salting automatically. These functions can significantly increase the overhead for a brute force attack compared to intentionally-fast functions such as MD5. For example, rainbow table attacks can become infeasible due to the high computing overhead. Finally, since computing power gets faster and cheaper over time, the technique can be reconfigured to increase the workload without forcing an entire replacement of the algorithm in use.

Some hash functions that have one or more of these desired properties include Argon2id, bcrypt [REF-291], PBKDF2 [REF-293], and scrypt [REF-292]. Many prefer Argon2id; it is the winner of the 2015 Password Hashing Competition (PHC), and the Argon2id hybrid algorithm has strong countermeasures against software-based attacks, direct hardware attacks (including GPU-based attacks), and side-channel attacks. Bcrypt counters software-based attacks; it is weaker against hardware-based attacks compared to Argon2id, but it is stronger against hardware-based attacks than PBDKF2. PBKDF2 counters software-based attacks, but it is the most vulnerable of these widely-used algorithms to hardware-based attacks such as from specialized circuits or GPUs (because it can be implemented with a small circuit and little RAM). The scrypt algorithm is expected to be strong against hardware attacks, but has not received as much review as Argon2id.

All of these algorithms are stronger than using salts with hash functions with very little computing overhead. Note that using these functions can have an impact on performance, so they require special consideration to avoid denial-of-service attacks. However, their configurability provides finer control over how much CPU and memory is used, so it could be adjusted to suit the environment's needs.:EFFECTIVENESS:High

PHASE:Architecture and Design:
If a technique that requires extra computational effort can not be implemented, then for each password that is processed, generate a new random salt using a strong random number generator with unpredictable seeds. Add the salt to the plaintext password before hashing it. When storing the hash, also store the salt. Do not use the same salt for every password.:EFFECTIVENESS:Limited

PHASE:Implementation Architecture and Design:
When using industry-approved techniques, use them correctly. Don't cut corners by skipping resource-intensive steps (CWE-325). These steps are often essential for preventing common attacks.

