
Filename Injection / Path Traversel 
-------


**Description:**

A Path Traversal attack aims to access files and directories that are stored outside the web root folder. 
By browsing the application, the attacker looks for absolute links to files stored on the web server. 
By manipulating variables that reference files with dot-dot-slash (../); sequences and its variations, 
it may be possible to access arbitrary files and directories stored on file system, including application source code, 
configuration and critical system files, limited by system operational access control. 

The attacker uses ../../
sequences to move up to root directory, thus permitting navigation through the file system.
This attack can be executed with an external malicious code injected on the path, like the Resource Injection attack. 

**Solution:**

The most effective solution to eliminate file inclusion vulnerabilities is to avoid passing user-submitted input to any
filesystem/framework API. If this is not possible the application can maintain a white list of files, 
that may be included by the page, and then use an identifier (for example the index number) to access to the selected file. 
Any request containing an invalid identifier has to be rejected, in this way there is
no attack surface for malicious users to manipulate the path. 

	