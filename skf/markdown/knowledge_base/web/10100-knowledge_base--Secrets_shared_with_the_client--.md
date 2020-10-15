##Description:

symmetric keys, passwords, or API secrets that are shared with the client should
not be used for functions that are classified critical.

Whenever a client is sucessfully targeted by a malicious attacker the integrety
of these keys is no longer guaranteed. 

##Mitigation:

Verify that symmetric keys, passwords, or API secrets generated
by or shared with clients are used only in protecting low risk secrets, 
such as encrypting local storage, or temporary ephemeral uses such as parameter obfuscation.
Sharing secrets with clients is clear-text equivalent and architecturally should be treated as such.
