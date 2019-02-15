## Description:

A Credential Service Provider (or Federation) is an Identity Access Management entity that releases security tokens to users of specific services (called Relying Parties). As Single Sign On (SSO) do, it makes possible to authenticate the user to registered services without actually requiring them to login again for every application. However, a Federation is a broader concept because it links multiple Identity Providers (IdP) of different organizations or security domains through trust boundary connections (established via digital signature and encryption). 

When deploying a Federation it is necessary to verify that the Credential Service Provider and Relying Parties handle the session management mechanisms in a secure way. 

## Solution:

To ensure a properly implemented connection between the Credential Service Provider and the Relying Parties, it is necessary to validate the session management in both sides. In particular, the Relying Parties have to specify to the CSP the maximum authentication timeframe for inactive sessions. After this period, the CSP has to reauthenticate the subscriber (i.e. the user) again.
On the other hand, is up to the CSP to inform the Relying Parties of the last authentication event of a user. With this information, the Relying Parties can determine if they need to force the user to authenticate again.
