##Description:

Whenever security researchers find a vulnerability in a library, modules, frameworks, platforms or 
operating system, these vulnerabilities are reported and saved in the CVE list. 

CVE is a list of information security vulnerabilities and exposures that aims to provide 
common names for  publicly known cyber security issues. The goal of CVE is to make it easier 
to share data  across separate vulnerability capabilities (tools, repositories, and services) 
with this "common enumeration."

Attackers can use these lists to find publicly known exploits which might exists in the target application. 
A lot of popular CVE exploits also have exploits available in Metasploit
or the Exploit database. This enables script kiddies to easily exploit the target applications
services, libraries and operating systems.

## Solution:

Verify that all application components, libraries, modules,
frameworks, platform, and operating systems are free from known vulnerabilities.

This could be achieved with for example, strict patch management and periodic scanning of
the environment for new issued CVEs'. 

It is also highly recommended to run the applications libraries and modules in the SDLC 
through tools like OWASP dependency check. This tool checks imported modules and libraries
for known CVEs'

    https://www.owasp.org/index.php/OWASP_Dependency_Check
