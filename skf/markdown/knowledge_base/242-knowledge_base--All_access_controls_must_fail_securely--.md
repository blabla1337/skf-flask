# All Access controls must fail securely
-------

## Description:

Handling errors securely is a key aspect of secure coding.
There are two types of errors that deserve special attention. The first is exceptions
that occur in the processing of a security control itself. It's important that these
exceptions do not enable behavior that the countermeasure would normally not allow.
As a developer, you should consider that there are generally three possible outcomes
from a security mechanism:

1. allow the operation
2. disallow the operation
3. exception

In general, you should design your security mechanism so that a failure will follow the same execution path
as disabling the operation

## Solution:

Make sure all the access control systems are thoroughly tested for failing securely before
using it in your application. It is common that complete unit-test are created especially
for this purpose.
