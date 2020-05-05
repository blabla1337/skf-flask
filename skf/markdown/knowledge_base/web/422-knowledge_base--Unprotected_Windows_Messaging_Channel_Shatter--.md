## Description:

The software does not properly verify the source of a message in the Windows Messaging System while running at elevated privileges, creating an alternate channel through which an attacker can directly send a message to the product.



## Mitigation:


PHASE:Architecture and Design:
Always verify and authenticate the source of the message.

