## Description:

In cryptography, forward secrecy (FS; also known as perfect forward secrecy, or PFS) is a property of key-agreement protocols ensuring that a session key derived from a set of long-term keys cannot be compromised if one of the long-term keys is compromised in the future. The key used to protect the transmission of data must not be used to derive any additional keys, and if the key used to protect the transmission of data is derived from some other keying material, then that material must not be used to derive any more keys. In this way, compromise of a single key permits access only to data protected by that single key.

## Solution:

In the beginning SSL handshake, the client sends a list of supported cipher suites (among other things). The server then picks one of the cipher suites, based on a ranking, and tells the client which one they will be using.

This step is the one that determines whether or not the future connection will have perfect forward secrecy. Note that, at this point, certificates have not entered the picture at all. This is because whether or not a connection has perfect forward secrecy is determined by how the session key is derived. And how the session key is derived is determined by the cipher suite in use. So, the cipher suites that use ephemeral Diffie-Hellman (DHE) or the elliptic curve variant (ECDHE) will have perfect forward secrecy while the other options will not.
