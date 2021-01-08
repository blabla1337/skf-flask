##Description:

The program violates the Enterprise JavaBeans (EJB) specification by using AWT/Swing.

The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the program violates the following EJB guideline: An enterprise bean must not use the AWT functionality to attempt to output information to a display, or to input information from a keyboard. The specification justifies this requirement in the following way: Most servers do not allow direct interaction between an application program and a keyboard/display attached to the server system.

##Mitigation:


PHASE:Architecture and Design:
Do not use AWT/Swing when writing EJBs.

