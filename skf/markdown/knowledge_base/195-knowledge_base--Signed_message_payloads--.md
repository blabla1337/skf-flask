# Signed message payloads
-------

## Description:

In order to establish trust between two communicating party's such as servers and clients
there message payload should be signed by means of public/private key method. This builds trust
and makes it harder for attackers to impersonate different users.

## Solution:

Verify that the message payload is signed to ensure reliable transport between client and
service, using JSON Web Signing or WS-Security for SOAP requests.
