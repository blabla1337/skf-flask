## Description:

Passwords stored locally are often vulnerable to offline attacks like dictionary attacks(list of commonly known passwords), bruteforce(permutation of all possible combinations) and rainbow tables(generate hashes upfront and do a look up for each hash). Since we belong to a generation of high speed computers performing these attacks is quite a trivial task for the attackers.


## Solution:

The most effective solution to eliminate offline attacks on password is to enforce the use of strong passwords and very prominently use industry recognized hashing algorithms with a salting mechanism. We hash passwords because in the event an attacker gets read access to our database, we do not want him to retrieve the passwords plain text. A salt is a non-secret, unique value in the database which is appended (depending on the used algorithm) to the password before it gets hashed.

Some of the well known hashing algorithms are as follows:

MD5 (Crytographically Broken),
SHA1 (Crytographically Broken),
SHA2,
SHA3,
PBKDF2,
bcrypt (defacto standard)
and scrypt.
