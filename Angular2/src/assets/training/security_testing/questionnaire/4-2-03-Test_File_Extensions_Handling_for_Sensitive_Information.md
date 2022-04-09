# Question

Decide if the given statmen is true or false.

"The following file extensions should never returned by a web server: .asa .inc .config"

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


Explanation: They are related to files which may contain sensitive information or to files for which there is no reason to be served.

-----SPLIT-----


# Question

Decide if the given statmen is true or false.

"Using legacy file handling libraries could result in defeating file upload filters."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False


Explanation: Windows 8.3 legacy file handling can sometimes be used to defeat file upload filters. For example;
1- file.phtml gets processed as PHP code.
2- FILE~1.PHT is served, but not processed by the PHP ISAPI handler.
3- shell.phPWND can be uploaded.
4- SHELL~1.PHP will be expanded and returned by the OS shell, then processed by the PHP ISAPI handler.

-----SPLIT-----

# Question

Decide if the given statmen is true or false.

"Performing white-box testing against file extensions handling amounts to checking the configurations of web servers or application servers taking part in the web application architecture, and verifying how they are instructed to serve different file extensions."

* ( ) True
* ( ) False

-----SPLIT-----

# Answer

* (x) True
* ( ) False

-----SPLIT-----