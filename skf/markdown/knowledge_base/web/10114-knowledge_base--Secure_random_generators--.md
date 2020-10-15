##Description:
A cryptographically secure pseudo-random number generator (CSPRNG) or cryptographic pseudo-random
number generator (CPRNG) is a pseudo-random number generator (PRNG) with properties that make it 
suitable for use in cryptography.

Most  applications require random numbers, for example:

- key generation
- nonces
- salts 

##Mitigation:
Ideally, the generation of random numbers in CSPRNGs uses entropy obtained from a high-quality source. Most of the development frameworks have excellent functions for generating true secure random values.

To test the effective entropy of the generated token we can utilize the extensive analysis tool
of "Burpsuite community version". more information in how to test your tokens effective entropy is found here:

https://portswigger.net/burp/documentation/desktop/tools/sequencer
