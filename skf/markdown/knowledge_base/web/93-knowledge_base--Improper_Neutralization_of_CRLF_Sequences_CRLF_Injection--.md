##Description:

The software uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.



##Mitigation:


PHASE:Implementation:
Avoid using CRLF as a special sequence.

PHASE:Implementation:
Appropriately filter or quote CRLF sequences in user-controlled input.

