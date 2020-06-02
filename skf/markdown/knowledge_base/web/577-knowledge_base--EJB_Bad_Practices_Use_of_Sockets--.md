## Description:

The program violates the Enterprise JavaBeans (EJB) specification by using sockets.

The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the program violates the following EJB guideline: An enterprise bean must not attempt to listen on a socket, accept connections on a socket, or use a socket for multicast. The specification justifies this requirement in the following way: The EJB architecture allows an enterprise bean instance to be a network socket client, but it does not allow it to be a network server. Allowing the instance to become a network server would conflict with the basic function of the enterprise bean-- to serve the EJB clients.

## Mitigation:


PHASE:Architecture and Design Implementation:
Do not use Sockets when writing EJBs.

