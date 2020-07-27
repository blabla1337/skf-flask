##Description:

There are some kind of headers that uses tokens such as Bearer or JWT which are signed or calculated using a key, by the server that creates it.

## Solution:

Verify the integrity and authenticity of the HTTP headers added by a trusted proxy or SSO devices by checking the digital signature or by recalculating the hash or integrity method using a private key or passphrase.
