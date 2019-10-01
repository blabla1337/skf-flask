Description:
A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. 
The term globally unique identifier (GUID) is also used, typically in software created by Microsoft.

Solution:
A version 4 UUID is randomly generated. As in other UUIDs, 
4 bits are used to indicate version 4, and 2 or 3 bits to indicate the variant 
(102 or 1102 for variants 1 and 2 respectively). Thus, for variant 1 (that is, most UUIDs) a 
random version-4 UUID will have 6 predetermined variant and version bits, leaving 122 bits for 
the randomly generated part, for a total of 2122, or 5.3×1036 (5.3 undecillion) possible version-4 
variant-1 UUIDs. There are half as many possible version-4 variant-2 UUIDs (legacy GUIDs) because 
there is one less random bit available, 3 bits being consumed for the variant.
