

# Question

Which of the IMAP commands can be used for command injection?
	
* ( ) CAPABILITY
* ( ) NOOP
* ( ) AUTHENTICATE
* ( ) LOGIN
* ( ) LOGOUT
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) CAPABILITY
* (x) NOOP
* (x) AUTHENTICATE
* (x) LOGIN
* (x) LOGOUT
* ( ) None of the above

-----SPLIT-----

# Question

What does a typical structure of an IMAP/SMTP Injection contains?
	
* ( ) Header: ending of the expected command
* ( ) Body: injection of the new command
* ( ) Footer: beginning of the expected command
* ( ) None of the above

-----SPLIT-----

# Answer

* (x) Header: ending of the expected command
* (x) Body: injection of the new command
* (x) Footer: beginning of the expected command
* ( ) None of the above

Explanation:  The following command injection payload can be seperated into header, body and footer parts.
Payload:
???? FETCH 4791 BODY[HEADER]
V100 CAPABILITY
V101 FETCH 4791 BODY[HEADER]

Structure:
Header = 4791 BODY[HEADER]
Body   = %0d%0aV100 CAPABILITY%0d%0a
Footer = V101 FETCH 4791

-----SPLIT-----
