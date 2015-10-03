
Unproven cryptographic algorithms
-------

**Description:**

The encryption techniques used in the application must be known and proven methods. 
When there is a self-made hashing algorithm developed it is very likely to contain 
vulnerabilities due to math-flaws resulting in encryption which can be broken.


**Solution:**

Never implement your own designed Crypto functions.
Verify that cryptographic modules used by the application have been validated against 
FIPS 140-2 or an equivalent standard.
