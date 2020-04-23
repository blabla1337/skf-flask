## Description:

A Pseudo-Random Number Generator (PRNG) uses the same seed each time the product is initialized.

If an attacker can guess (or knows) the seed, then the attacker may be able to determine the random numbers that will be produced from the PRNG.

## Mitigation:


PHASE:Architecture and Design:
Do not reuse PRNG seeds. Consider a PRNG that periodically re-seeds itself as needed from a high quality pseudo-random output, such as hardware devices.

PHASE:Architecture and Design Requirements:STRATEGY:Libraries or Frameworks:
Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C (Approved Random Number Generators).

