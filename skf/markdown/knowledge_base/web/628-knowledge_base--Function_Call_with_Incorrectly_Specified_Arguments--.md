##Description:

The product calls a function, procedure, or routine with arguments that are not correctly specified, leading to always-incorrect behavior and resultant weaknesses.

There are multiple ways in which this weakness can be introduced, including: the wrong variable or reference; an incorrect number of arguments; incorrect order of arguments; wrong type of arguments; or wrong value.

##Mitigation:


PHASE:Build and Compilation:
Once found, these issues are easy to fix. Use code inspection tools and relevant compiler features to identify potential violations. Pay special attention to code that is not likely to be exercised heavily during QA.

PHASE:Architecture and Design:
Make sure your API's are stable before you use them in production code.

