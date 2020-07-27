##Description:

The program invokes a potentially dangerous function that could introduce a vulnerability if it is used incorrectly, but the function can also be used safely.



##Mitigation:


PHASE:Build and Compilation Implementation:
Identify a list of prohibited API functions and prohibit developers from using these functions, providing safer alternatives. In some cases, automatic code analysis tools or the compiler can be instructed to spot use of prohibited functions, such as the banned.h include file from Microsoft's SDL. [REF-554] [REF-7]

