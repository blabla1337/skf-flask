## Description:

The ASP.NET application does not use an input validation framework.



## Mitigation:


PHASE:Architecture and Design:
Use the ASP.NET validation framework to check all program input before it is processed by the application. Example uses of the validation framework include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only T or F Free-form strings are of a reasonable length and composition

