##Description:

The system's authorization functionality does not prevent one user from gaining access to another user's data or record by modifying the key value identifying the data.

Retrieval of a user record occurs in the system based on some key value that is under user control. The key would typically identify a user-related record stored in the system and would be used to lookup that record for presentation to the user. It is likely that an attacker would have to be an authenticated user in the system. However, the authorization process would not properly check the data access operation to ensure that the authenticated user performing the operation has sufficient entitlements to perform the requested data access, hence bypassing any other authorization checks present in the system. For example, attackers can look at places where user specific data is retrieved (e.g. search screens) and determine whether the key for the item being looked up is controllable externally. The key may be a hidden field in the HTML form field, might be passed as a URL parameter or as an unencrypted cookie variable, then in each of these cases it will be possible to tamper with the key value. One manifestation of this weakness is when a system uses sequential or otherwise easily-guessable session IDs that would allow one user to easily switch to another user's session and read/modify their data.

##Mitigation:


PHASE:Architecture and Design:
For each and every data access, ensure that the user has sufficient privilege to access the record that is being requested.

PHASE:Architecture and Design Implementation:
Make sure that the key that is used in the lookup of a specific user's record is not controllable externally by the user or that any tampering can be detected.

PHASE:Architecture and Design:
Use encryption in order to make it more difficult to guess other legitimate values of the key or associate a digital signature with the key so that the server can verify that there has been no tampering.

