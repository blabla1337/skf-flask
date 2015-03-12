
Version management
-------

**Description:**

Whenever a programmer decides to use third party software, 
he should keep an eye implementing a proper version management methodology for this software. 
When hackers discover vulnerabilities they often publish these exploits online in order 
to push the developers of this software to fix their issues. As a result, 
when your software is not upgraded to the latest available version, 
script kiddies could easily compromise your application by following the 
exploit tutorials online, thus compromising your application.


**Solution:**

One option is not to use components that you did not write. 
But that is not very realistic.

Most component projects do not create vulnerability patches for old versions. 
Instead, most simply fix the problem in the next version. So upgrading to these new 
versions is critical. 
Software projects should have a process in place to:

-Identify all components and the versions you are using, including all dependencies. 
 (e.g., the versions plugin).

-Monitor the security of these components in public databases, 
 project mailing lists, and security mailing lists, and keep them up to date.
 
-Establish security policies governing component use, such as requiring certain software 
 development practices, passing security tests, and acceptable licenses.
 
-Where appropriate, consider adding security wrappers around components to disable unused 
 functionality and/ or secure weak or vulnerable aspects of the component.
	