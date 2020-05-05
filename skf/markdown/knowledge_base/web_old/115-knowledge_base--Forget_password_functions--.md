## Description:

Whenever the application provides a password forget functionality or another 
type of recovery methods there are several implementations of hardened proven ways to make
the user recover his password.

## Solution:

The recommended solutions are to use TOTP (Time-based One-Time Password algorithm). This 
method is an example of a hash-based message authentication code (HMAC). It combines a 
secret key with the current timestamp using a cryptographic hash function to generate 
a one-time password. Because network latency and out-of-sync clocks can result in the password 
recipient having to try a range of possible times to authenticate against, the timestamp typically 
increases in 30-second intervals, which thus cuts the potential search space.

Or the other option is to use a Mathematical-algorithm-based one-time password method. This other 
type of one-time password uses a complex mathematical algorithm, such as a hash chain, to generate 
a series of one-time passwords from a secret shared key. Each password cannot be guessed even when 
previous passwords are known. The open source OAuth algorithm is standardized; other algorithms are 
covered by U.S. patents. Each password is observably unpredictable and independent on previous ones. 
Therefore, an adversary would be unable to guess what the next password may be, even with the 
knowledge of all previous passwords.

Example of a hard token mathimatical algorithm would be a yubikey
Example of a soft token TOTP would be google authenticator

The last resort would be to send a new password by email. This mail should contain a reset link with 
a token which is valid for a limited amount of time. Additional authentication based on soft-tokens 
(e.g. SMS token, native mobile applications, etc.) can be required as well before the link is 
sent over. Also, make sure whenever such a recovery cycle is started, the application does not 
reveal the user’s current password in any way.
