## Description:

The lack of entropy available for, or used by, a Pseudo-Random Number Generator (PRNG) can be a stability and security threat.



## Mitigation:


PHASE:Architecture and Design Requirements:STRATEGY:Libraries or Frameworks:
Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C (Approved Random Number Generators).

PHASE:Implementation:
Consider a PRNG that re-seeds itself as needed from high-quality pseudo-random output, such as hardware devices.

PHASE:Architecture and Design:
When deciding which PRNG to use, look at its sources of entropy. Depending on what your security needs are, you may need to use a random number generator that always uses strong random data -- i.e., a random number generator that attempts to be strong but will fail in a weak way or will always provide some middle ground of protection through techniques like re-seeding. Generally, something that always provides a predictable amount of strength is preferable.

