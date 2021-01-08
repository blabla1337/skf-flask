##Description:

The program violates the Enterprise JavaBeans (EJB) specification by using thread synchronization primitives.

The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the program violates the following EJB guideline: An enterprise bean must not use thread synchronization primitives to synchronize execution of multiple instances. The specification justifies this requirement in the following way: This rule is required to ensure consistent runtime semantics because while some EJB containers may use a single JVM to execute all enterprise bean's instances, others may distribute the instances across multiple JVMs.

##Mitigation:


PHASE:Implementation:
Do not use Synchronization Primitives when writing EJBs.

