## High value transactions

## Description:

Whenever there are high value transactions a normal username / password static authentication method does
not suffice to ensure a high level of security. Whenever the application digests high level of transactions ensure that
risk based re-authentication, two factor or transaction signing is in place.

## Solution:

#1 risk based authentication:
In Authentication, risk-based authentication is a non-static authentication 
system which takes into account the profile of the agent requesting access to 
the system to determine the risk profile associated with that transaction. 

The risk profile is then used to determine the complexity of the challenge.
Higher risk profiles leads to stronger challenges, whereas a static username/password may suffice for 
lower-risk profiles. Risk-based implementation allows the application to challenge the user for additional 
credentials only when the risk level is appropriate.

#2 two factor authentication:
Multi-factor authentication (MFA) is a method of computer access control in which a user is 
granted access only after successfully presenting several separate pieces of evidence to an 
authentication mechanism – typically at least two of the following categories: knowledge (something they know), 
possession (something they have), and inherence (something they are)

#3 Transaction signing:
Transaction signing (or digital transaction signing) is the process of calculating a keyed hash function 
to generate a unique string which can be used to verify both the authenticity and integrity of an online transaction.

A keyed hash is a function of the user's private or secret key and the transaction details, 
such as the transfer to account number and the transfer amount.

To provide a high level of assurance of the authenticity and integrity of 
the hash it is essential to calculate the hash on a trusted device, such as a separate smart card reader.
Calculating a hash on an Internet-connected PC or mobile device such as a mobile telephone/PDA would be
counter-productive as malware and attackers can attack these platforms and potentially subvert the signing process itself.
