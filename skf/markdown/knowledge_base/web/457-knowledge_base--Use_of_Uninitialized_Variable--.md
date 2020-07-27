##Description:

The code uses a variable that has not been initialized, leading to unpredictable or unintended results.

In some languages such as C and C++, stack variables are not initialized by default. They generally contain junk data with the contents of stack memory before the function was invoked. An attacker can sometimes control or read these contents. In other languages or conditions, a variable that is not explicitly initialized can be given a default value that has security implications, depending on the logic of the program. The presence of an uninitialized variable can sometimes indicate a typographic error in the code.

##Mitigation:


PHASE:Implementation:STRATEGY:Attack Surface Reduction:
Assign all variables to an initial value.

PHASE:Build and Compilation:STRATEGY:Compilation or Build Hardening:
Most compilers will complain about the use of uninitialized variables if warnings are turned on.

PHASE:Implementation Operation:
When using a language that does not require explicit declaration of variables, run or compile the software in a mode that reports undeclared or unknown variables. This may indicate the presence of a typographic error in the variable's name.

PHASE:Requirements:
The choice could be made to use a language that is not susceptible to these issues.

PHASE:Architecture and Design:
Mitigating technologies such as safe string libraries and container abstractions could be introduced.

