##Description:

A Credential Service Provider (or Identity Provider) is an Identity Access Management entity that releases security tokens to users of specific services (called Relying Parties or Service Providers). An Identity Provider makes possible to authenticate the user to registered services without actually requiring them to login again for every application.

When deploying a Credential Service Provider it is necessary to verify that the Credential Service Provider and Relying Parties handle the session management mechanisms in a secure way. 

##Mitigation:

To ensure a properly implemented connection between the Identity Provider and the Relying Parties, it is necessary to validate the session management in both sides. In particular, the Relying Parties have to specify to the IdP the maximum authentication timeframe for inactive sessions. After this period, the IdP has to reauthenticate the subscriber (i.e. the user) again.
On the other hand, is up to the IdP to inform the Relying Parties of the last authentication event of a user. With this information, the Relying Parties can determine if they need to force the user to authenticate again.
