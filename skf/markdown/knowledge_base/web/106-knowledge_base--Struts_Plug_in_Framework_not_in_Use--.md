## Description:

When an application does not use an input validation framework such as the Struts Validator, there is a greater risk of introducing weaknesses related to insufficient input validation.

Unchecked input is the leading cause of vulnerabilities in J2EE applications. Unchecked input leads to cross-site scripting, process control, and SQL injection vulnerabilities, among others. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Mitigation:


PHASE:Architecture and Design:STRATEGY:Input Validation:
Use an input validation framework such as Struts.

PHASE:Architecture and Design:STRATEGY:Libraries or Frameworks:
Use an input validation framework such as Struts.

PHASE:Implementation:STRATEGY:Input Validation:
Use the Struts Validator to validate all program input before it is processed by the application. Ensure that there are no holes in your configuration of the Struts Validator. Example uses of the validator include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only T or F Free-form strings are of a reasonable length and composition

PHASE:Implementation:STRATEGY:Libraries or Frameworks:
Use the Struts Validator to validate all program input before it is processed by the application. Ensure that there are no holes in your configuration of the Struts Validator. Example uses of the validator include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only T or F Free-form strings are of a reasonable length and composition

