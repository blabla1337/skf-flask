## Description:

When converting from one data type to another, such as long to integer, data can be omitted or translated in a way that produces unexpected values. If the resulting values are used in a sensitive context, then dangerous behaviors may occur.



## Mitigation:


PHASE:Implementation:
Avoid making conversion between numeric types. Always check for the allowed ranges.

