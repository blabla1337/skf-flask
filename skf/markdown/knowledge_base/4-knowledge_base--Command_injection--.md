
Command injection
-------

**Description:**

Command injection is an attack in which the goal is execution of arbitrary commands on
the host operating system via a vulnerable application. Command injection attacks are 
possible when an application passes unsafe user supplied data 
(forms, cookies, HTTP headers etc.) to a system shell. In this attack, 
the attacker-supplied operating system commands are usually executed with the privileges 
of the vulnerable application. Command injection attacks are possible largely due to 
insufficient input validation. This attack differs from Code Injection, in that code 
injection allows the attacker to adds his own code that is then executed by the application. 
In Code Injection, the attacker extends the default functionality of the application 
without the necessity of executing system commands. 


**Solution:**

User-input that is used in a shell command should not contain dangerous characters. 
A blacklist of characters is not a good option because it may be difficult to think of 
all of the characters to validate against. A white list containing only allowable 
characters should be created to validate the user-input.


	