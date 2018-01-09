## Description:

LDAP (Lightweight Directory Access Protocol) Injection is an attack used to exploit web based applications that construct LDAP statements based on user input. When an application fails to properly sanitize user input, it is possible to modify LDAP statements using a local proxy. This could result in the execution of arbitrary commands such as granting permissions to unauthorized queries, and content modification inside the LDAP tree. The same advanced exploitation techniques available in SQL Injection can be similarly applied in LDAP Injection.

## Solution:

The best way to prevent LDAP injection is to use a positive validation scheme for ensuring that the data going into your queries does not contain any attacks. However, in some cases, it is necessary to include special characters in the input that is passed into an LDAP query. In this case, using escaping can prevent the LDAP interpreter from thinking those special characters are actually part of the LDAP query.
