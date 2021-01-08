##Description:

The program violates the Enterprise JavaBeans (EJB) specification by using the java.io package.

The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the program violates the following EJB guideline: An enterprise bean must not use the java.io package to attempt to access files and directories in the file system. The specification justifies this requirement in the following way: The file system APIs are not well-suited for business components to access data. Business components should use a resource manager API, such as JDBC, to store data.

##Mitigation:


PHASE:Implementation:
Do not use Java I/O when writing EJBs.

