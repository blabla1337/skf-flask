##Description:

Sometimes it is possible through an "enabling debug parameter" to display technical
information/secrets within the application. As a result, the attacker learns more about the
operation of the application, increasing his attack surface. Sometimes having a debug flag 
enabled could even lead to code execution attacks (older versions of werkzeug) 

## Solution:

Disable the possibility to enable debug information on a live environment.
