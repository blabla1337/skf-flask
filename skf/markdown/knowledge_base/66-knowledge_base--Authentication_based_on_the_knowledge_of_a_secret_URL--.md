# Authentication based on the knowledge of a secret URL
-------

## Description:

This is a form of security by obscurity. Whenever an attacker manages to fuzz or spider
this url the application could compromise whatever is behind this url.

## Solution:

Always implement proper authentication mechanisms that is not using a static authentication URL.
