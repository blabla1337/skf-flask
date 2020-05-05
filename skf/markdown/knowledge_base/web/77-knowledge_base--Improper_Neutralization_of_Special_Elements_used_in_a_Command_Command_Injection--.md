## Description:

The software constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.

Command injection vulnerabilities typically occur when: 1. Data enters the application from an untrusted source. 2. The data is part of a string that is executed as a command by the application. 3. By executing the command, the application gives an attacker a privilege or capability that the attacker would not otherwise have. Command injection is a common problem with wrapper programs.

## Mitigation:


PHASE:Architecture and Design:
If at all possible, use library calls rather than external processes to recreate the desired functionality.

PHASE:Implementation:
If possible, ensure that all external commands called from the program are statically created.

PHASE:Implementation:STRATEGY:Input Validation:
Assume all input is malicious. Use an accept known good input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, boat may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as red or blue. Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, blacklists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

PHASE:Operation:
Run time: Run time policy enforcement may be used in a whitelist fashion to prevent use of any non-sanctioned commands.

PHASE:System Configuration:
Assign permissions to the software system that prevents the user from accessing/opening privileged files.

