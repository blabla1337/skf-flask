##Description:

The software declares a critical variable, field, or member to be public when intended security policy requires it to be private.

This issue makes it more difficult to maintain the software, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

##Mitigation:


PHASE:Implementation:
Data should be private, static, and final whenever possible. This will assure that your code is protected by instantiating early, preventing access, and preventing tampering.

