##Description:

There are some techniques attackers use to decrease the entropy pool of the system so it will
create weak and predictable 'random' numbers that should not be used in crypto functions.

## Solution:

Enforce in your application that random numbers are created with proper entropy even when the
application is under heavy load, or that the application degrades gracefully in such circumstances.
