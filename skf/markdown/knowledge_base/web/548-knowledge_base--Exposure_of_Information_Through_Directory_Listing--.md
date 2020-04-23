## Description:

A directory listing is inappropriately exposed, yielding potentially sensitive information to attackers.

A directory listing provides an attacker with the complete index of all the resources located inside of the directory. The specific risks and consequences vary depending on which files are listed and accessible.

## Mitigation:


PHASE:Architecture and Design System Configuration:
Recommendations include restricting access to important directories or files by adopting a need to know requirement for both the document and server root, and turning off features such as Automatic Directory Listings that could expose private files and provide information that could be utilized by an attacker when formulating or conducting an attack.

