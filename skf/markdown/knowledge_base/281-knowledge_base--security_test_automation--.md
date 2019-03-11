Description:

Security tools can be easiliy integrated into CI/CD pipelines.
Generally the recommended way is to containerize your tooling to
have a CI environment agnostic approach so you can build and configure them
once and than run them everywhere you need. Especially with autonomous 
self steering developer teams this is a really important development.

There are a lot of security tools on the market both free
and premium. It is for you to decide which tools cover your technology
stacks most optimal.

There are different category tooling such as but not limited to,

- DAST tools
  Web Application Vulnerability Scanners are automated tools that scan
  web applications, normally from the outside, to look for security
  vulnerabilities such as Cross-site scripting, SQL Injection, 
  Command Injection, Path Traversal and insecure server configuration. 
  This category of tools is frequently referred to as Dynamic Application 
  ecurity Testing (DAST) Tools.  

- SAST tools
  Source code analysis tools, also referred to as Static 
  Application Security Testing (SAST) Tools, are designed to 
  analyze source code and/or compiled versions of code to help 
  find security flaws.  

- Dependency checker tools
   up to 90 percent of an application typically consists of third-party components.
   A depdendenct checker builds up the applications dependency tree and correlates
   all the third party components to known vulnerabilities to see if
   by using these libraries, you are introducing vulnerable components in your 
   application. Some Source code repositories provide dependency checking out
   of the box these days.

Solution:

Examples for SAST tooling are found here, allong with more in depth
information.

    https://www.owasp.org/index.php/Source_Code_Analysis_Tools

Examples for DAST tooling are found here,

    https://www.owasp.org/index.php/Category:Vulnerability_Scanning_Tools


Examples for tools that can scan your containers for vulnerbilities are,

    https://coreos.com/clair/docs/latest/
    https://anchore.com/

Examples for Dependency checkers are found here,
    https://www.owasp.org/index.php/OWASP_Dependency_Check
