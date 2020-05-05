## Description:

If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the software system.

If the EJB deployment descriptor contains one or more method permissions that grant access to the special ANYONE role, it indicates that access control for the application has not been fully thought through or that the application is structured in such a way that reasonable access control restrictions are impossible.

## Mitigation:


PHASE:Architecture and Design System Configuration:
Follow the principle of least privilege when assigning access rights to EJB methods. Permission to invoke EJB methods should not be granted to the ANYONE role.

