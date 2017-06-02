# Insecure internal communication
-------

## Description:

Whenever organizations communicate by means of unencrypted connections, an attacker
could easily sniff insecure communications and access sensitive information.

## Solution:

Use TLS encrypted data lines for all internal communication channels.
Also, your infrastructure should not traverse unencrypted or weakly encrypted links. Because
if so, all your data's integrity and confidentiality will be lost.
