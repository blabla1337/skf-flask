##Description:

PBKDF2, is a function for creating a cryptographic key from a password. The aim of the function is to create a key in such a way that dictionary attacks (where the attacker just tries a range of possible passwords) are unfeasible. To do this, PBKDF2 applies a pseudorandom function (PRF) to the password many times. Additionally, the function can be given a “salt” parameter to make each key derivation operation unique. A developer using PBKDF2 must carefully choose parameter values for the salt, the PRF, and the number of iterations, i.e. the number of times the PRF will be applied to the password when deriving the key.


## Solution:

A application developer using PBKDF2 should ensure the iteration count SHOULD be as large as verification server performance will allow, typically at least 100,000 iterations.
