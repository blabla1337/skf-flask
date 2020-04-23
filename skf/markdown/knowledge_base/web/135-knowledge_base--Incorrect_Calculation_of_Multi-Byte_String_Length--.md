## Description:

The software does not correctly calculate the length of strings that can contain wide or multi-byte characters.



## Mitigation:


PHASE:Implementation:STRATEGY:Input Validation:
Always verify the length of the string unit character.

PHASE:Implementation:STRATEGY:Libraries or Frameworks:
Use length computing functions (e.g. strlen, wcslen, etc.) appropriately with their equivalent type (e.g.: byte, wchar_t, etc.)

