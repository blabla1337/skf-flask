## Description:

The program violates the Enterprise JavaBeans (EJB) specification by using the class loader.

The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the program violates the following EJB guideline: The enterprise bean must not attempt to create a class loader; obtain the current class loader; set the context class loader; set security manager; create a new security manager; stop the JVM; or change the input, output, and error streams. The specification justifies this requirement in the following way: These functions are reserved for the EJB container. Allowing the enterprise bean to use these functions could compromise security and decrease the container's ability to properly manage the runtime environment.

## Mitigation:


PHASE:Architecture and Design Implementation:
Do not use the Class Loader when writing EJBs.

