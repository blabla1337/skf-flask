
Enforce policys for sensitive data processing
-------

**Description:**

When you proces data you should always enforce policies for the transfer of sensitive data 
in order to enforce higher level of security imposing structured thresholds to 
fend of attackers.


**Solution:**

First you have to create a list which contains locations of where all sensitive data is 
used and processed. Next, you create a policy that tells who is allowed and to what extend 
they have privileges to look into which data. When this data moves through the network it 
should always be encrypted (TLS) and also be stored encrypted. Thereafter you should 
establish monitoring and testing methods to verify that everything stays encrypted and 
your policy's are properly enforced.

	