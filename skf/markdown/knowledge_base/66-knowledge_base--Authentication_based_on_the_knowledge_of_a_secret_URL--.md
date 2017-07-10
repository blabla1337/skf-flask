## Description:

This is a form of security by obscurity. Whenever an attacker manages to fuzz or spider
this URL the application could compromise whatever is behind this URL.

## Solution:

Always implement proper authentication mechanisms that are not using a static authentication URL.
