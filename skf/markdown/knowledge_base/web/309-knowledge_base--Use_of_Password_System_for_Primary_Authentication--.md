##Description:

The use of password systems as the primary means of authentication may be subject to several flaws or shortcomings, each reducing the effectiveness of the mechanism.



##Mitigation:


PHASE:Architecture and Design:
In order to protect password systems from compromise, the following should be noted: Passwords should be stored safely to prevent insider attack and to ensure that -- if a system is compromised -- the passwords are not retrievable. Due to password reuse, this information may be useful in the compromise of other systems these users work with. In order to protect these passwords, they should be stored encrypted, in a non-reversible state, such that the original text password cannot be extracted from the stored value. Password aging should be strictly enforced to ensure that passwords do not remain unchanged for long periods of time. The longer a password remains in use, the higher the probability that it has been compromised. For this reason, passwords should require refreshing periodically, and users should be informed of the risk of passwords which remain in use for too long. Password strength should be enforced intelligently. Rather than restrict passwords to specific content, or specific length, users should be encouraged to use upper and lower case letters, numbers, and symbols in their passwords. The system should also ensure that no passwords are derived from dictionary words.

PHASE:Architecture and Design:
Use a zero-knowledge password protocol, such as SRP.

PHASE:Architecture and Design:
Ensure that passwords are stored safely and are not reversible.

PHASE:Architecture and Design:
Implement password aging functionality that requires passwords be changed after a certain point.

PHASE:Architecture and Design:
Use a mechanism for determining the strength of a password and notify the user of weak password use.

PHASE:Architecture and Design:
Inform the user of why password protections are in place, how they work to protect data integrity, and why it is important to heed their warnings.

