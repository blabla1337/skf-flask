##Description:

All time sources must be synchronized throughout. For example, different API servers or 
microservices. to prevent logs to be tainted and become unusable for forensics.

##Mitigation:

Time sources should be synchronized to ensure logs have the correct time. If these
time sources are not synchronized, the logs lose integrity and can become untrusted for
investigators.
