##Description:

If too few arguments are sent to a function, the function will still pop the expected number of arguments from the stack. Potentially, a variable number of arguments could be exhausted in a function as well.



##Mitigation:


PHASE:Build and Compilation:
This issue can be simply combated with the use of proper build process.

PHASE:Implementation:
Forward declare all functions. This is the recommended solution. Properly forward declaration of all used functions will result in a compiler error if too few arguments are sent to a function.

