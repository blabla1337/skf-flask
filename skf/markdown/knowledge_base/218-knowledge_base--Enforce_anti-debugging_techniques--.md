# Enforce anti-debugging techniques
-------

## Description:

An attacker can use debug tooling to find out how the application is working and determain the 
possible attack surface by using tooling like GDB or running the application in an emulator. Using
these type of tooling the attacker can learn a lot about the tool and succesfully attack the application
and have a higher change of succeeding.

## Solution:

The application has to make use of anti-debugging techniques that are sufficient enough to deter or 
delay likely attackers from injecting debuggers into the application. Also the application has to be
able to notice if it's runned on an emulator or a specially designed hardware device that was not 
intended to be used and to prevent the attacker from gaining knowledge about the application.
