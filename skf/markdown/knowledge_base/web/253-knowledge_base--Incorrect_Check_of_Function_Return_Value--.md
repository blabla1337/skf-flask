##Description:

The software incorrectly checks a return value from a function, which prevents the software from detecting errors or exceptional conditions.

Important and common functions will return some value about the success of its actions. This will alert the program whether or not to handle any errors caused by that function.

##Mitigation:


PHASE:Architecture and Design:STRATEGY:Language Selection:
Use a language or compiler that uses exceptions and requires the catching of those exceptions.

PHASE:Implementation:
Properly check all functions which return a value.

PHASE:Implementation:
When designing any function make sure you return a value or throw an exception in case of an error.

