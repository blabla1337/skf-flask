##Description:

When you process data you should always enforce policies for the transfer of sensitive data in order to enforce a higher level of security imposing structured thresholds to fend off attackers.

##Mitigation:

First, you have to create a list which contains locations of where all sensitive data is used and processed. Next, you create a policy that tells who is allowed and to what extent they have privileges to look into which data. When this data moves through the network it should always be encrypted (TLS) and also be stored encrypted. Thereafter you should establish monitoring and testing methods to verify that everything stays encrypted and your policies are properly enforced.
Also, determine whenever data storage is necessary or becomes a redundancy. Whenever sensitive data does not have to be stored don't store it. This reduces the quantity of data may your application ever be compromised.
Ultimately, verify accessing sensitive data is logged, if the data is collected under relevant data protection directives or where logging of accesses is required.
Sensitive data or primary keys, such as personally identifiable information or credit cards should also be anonymized, masked or truncated on the server before transmission to the client.

