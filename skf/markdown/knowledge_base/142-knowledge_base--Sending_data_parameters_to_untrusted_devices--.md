# Sending data/parameters to untrusted devices
-------

## Description:

Whenever an application sends data/parameters to untrusted devices this data could be
compromised if the device has malicious intents.


## Solution:

Verify the application minimizes the number of parameters sent to untrusted systems,
such as hidden fields, Ajax variables, cookies and header values.

These untrusted devices should also be documented if possible and should be taken into
account when developing your application to minimize the possibility you send
unintended sensitive data towards these devices.

Recommended knowledge base items:

- High level architecture should be defined
- Identify all application components
