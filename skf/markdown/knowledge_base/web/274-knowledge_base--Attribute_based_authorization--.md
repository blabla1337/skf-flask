## Description:

Access Control (or Authorization) is the process of granting or denying specific requests from a user, 
program, or process. Access control also involves the act of granting and revoking those privileges.

It should be noted that authorization (verifying access to specific features or resources) is not equivalent
to authentication (verifying identity).  

## Solution:

Attribute Based Access Control (ABAC) will grant or deny user requests based on arbitrary 
attributes of the user and arbitrary attributes of the object, and environment conditions 
that may be globally recognized and more relevant to the policies at hand. 

Once you have chosen a specific access control design pattern, it is often difficult and time
consuming to re-engineer access control in your application with a new pattern. Access Control is
one of the main areas of application security design that must be thoroughly designed up front, 
especially when addressing requirements like multi-tenancy and horizontal (data dependent) access control. 


Ideally we want to move from here:
```
if (user.hasRole("ADMIN")) || (user.hasRole("MANAGER")) {
   deleteAccount();
}
```

To here:

```
if (user.hasAccess("DELETE_ACCOUNT")) {
   deleteAccount();
}
```

This is becuase the latter is more manageble over time.

For more information please refer to the OWASP top 10 pro active controls.

https://www.owasp.org/index.php/OWASP_Proactive_Controls

OWASP pro active controls chapter C7 "Enforce Access Controls"

