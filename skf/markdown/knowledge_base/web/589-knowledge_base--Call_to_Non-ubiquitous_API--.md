## Description:

The software uses an API function that does not exist on all versions of the target platform. This could cause portability problems or inconsistencies that allow denial of service or other consequences.

Some functions that offer security features supported by the OS are not available on all versions of the OS in common use. Likewise, functions are often deprecated or made obsolete for security reasons and should not be used.

## Mitigation:


PHASE:Implementation:
Always test your code on any platform on which it is targeted to run on.

PHASE:Testing:
Test your code on the newest and oldest platform on which it is targeted to run on.

PHASE:Testing:
Develop a system to test for API functions that are not portable.

