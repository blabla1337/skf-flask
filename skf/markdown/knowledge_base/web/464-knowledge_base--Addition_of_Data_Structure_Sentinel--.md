##Description:

The accidental addition of a data-structure sentinel can cause serious programming logic problems.

Data-structure sentinels are often used to mark the structure of data. A common example of this is the null character at the end of strings or a special sentinel to mark the end of a linked list. It is dangerous to allow this type of control data to be easily accessible. Therefore, it is important to protect from the addition or modification of sentinels.

##Mitigation:


PHASE:Implementation Architecture and Design:
Encapsulate the user from interacting with data sentinels. Validate user input to verify that sentinels are not present.

PHASE:Implementation:
Proper error checking can reduce the risk of inadvertently introducing sentinel values into data. For example, if a parsing function fails or encounters an error, it might return a value that is the same as the sentinel.

PHASE:Architecture and Design:
Use an abstraction library to abstract away risky APIs. This is not a complete solution.

PHASE:Operation:
Use OS-level preventative functionality. This is not a complete solution.

