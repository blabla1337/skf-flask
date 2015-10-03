
Certificate paths/revocation information
-------

**Description:**

Whenever your certificate authority is not trusted anymore you should always be able to 
recall these certificates asap.


**Solution:**

The trust anchor for given zone is found in the keyset-<zone name> file on the secure 
signing computer in the same location where the signed and unsigned copies of the zone reside. 
This file is created automatically as part of the signing process. 
A certificate revocation list (CRL) is a list, created and signed by a 
certificate authority (CA), which contains serial numbers of certificates that have been 
issued by that CA and are currently revoked. In addition to the serial number for the 
revoked certifications, the CRL also contains the reason for revocation for each certificate 
and the time the certificate was revoked. The serial number for each revoked certificate is 
kept in the CAs database and published in the CRL until the certificate expires. 

After the revoked certificate is expired, the certificates entry in the CRL is removed and 
the CA may remove the certificate from its database. Typically, the revoked certificate 
will remain in the CRL for one publication period after the certificate expires. By all 
times you should have this information in reach in order to take quick actions.

	