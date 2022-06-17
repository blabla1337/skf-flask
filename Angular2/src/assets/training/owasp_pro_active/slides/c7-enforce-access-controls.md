# C7: Enforce Access Controls

## Description
Access Control (or Authorization) is the process of granting or denying *specific requests* from a user, program, or process. Access control also involves the act of *granting and revoking those privileges*.

It should be noted that authorization (verifying access to specific features or resources) is not equivalent to authentication (verifying identity).

Access Control functionality often spans many areas of software depending on the complexity of the access control system. For example, managing access control metadata or building caching for scalability purposes are often additional components in an access control system that need to be built or managed.
There are several different types of access control design that should be considered.

* Discretionary Access Control (DAC) is a means of restricting access to objects (e.g., files, data entities) based on the identity and need-to-know of subjects (e.g., users, processes) and/or groups to which the object belongs.
* Mandatory Access Control (MAC) is a means of restricting access to system resources based on the sensitivity (as represented by a label) of the information contained in the system resource and the formal authorization (i.e., clearance) of users to access information of such sensitivity.
* Role Based Access Control (RBAC) is a model for controlling access to resources where permitted actions on resources are identified with roles rather than with individual subject identities.
* Attribute Based Access Control (ABAC) will grant or deny user requests based on arbitrary attributes of the user and arbitrary attributes of the object, and environment conditions that may be globally recognized and more relevant to the policies at hand.

## Access Control Design Principles
The following "positive" access control design requirements should be considered at the initial stages of application development. 

### 1) Design Access Control Thoroughly Up Front
Once you have chosen a specific access control design pattern, it is often difficult and time consuming to re-engineer access control in your application with a new pattern. Access Control is one of the main areas of application security design that must be thoroughly designed up front, especially when addressing requirements like multi-tenancy and horizontal (data dependent) access control.

Access Control design may start simple but can often grow into a complex and feature-heavy security control. When evaluating access control capability of software frameworks, ensure that your access control functionality will allow for customization for your specific access control feature need.

### 2) Force All Requests to Go Through Access Control Checks
Ensure that all request go through some kind of access control verification layer. Technologies like Java filters or other automatic request processing mechanisms are ideal programming artifacts that will help ensure that all requests go through some kind of access control check.

### 3) Deny by Default
Deny by default is the principle that if a request is not specifically allowed, it is denied. There are many ways that this rule will manifest in application code. Some examples of these are:

1. Application code may throw an error or exception while processing access control requests. In these cases access control should always be denied.
2. When an administrator creates a new user or a user registers for a new account, that account should have minimal or no access by default until that access is configured.
3. When a new feature is added to an application all users should be denied to use that feature until it's properly configured.

### 4) Principle of Least Privilege
Ensure that all users, programs, or processes are only given as least or as little necessary access as possible. Be wary of systems that do not provide granular access control configuration capabilities.

### 5) Don't Hardcode Roles
Many application frameworks default to access control that is role based. It is common to find application code that is filled with checks of this nature.
```
    if (user.hasRole("ADMIN")) || (user.hasRole("MANAGER")) {
        deleteAccount();
    }
```
Be careful about this type of role-based programming in code. It has the following limitations or dangers.
* Role based programming of this nature is fragile. It is easy to create incorrect or missing role checks in code.
* Role based programming does not allow for multi-tenancy. Extreme measures like forking the code or added checks for each customer will be required to allow role based systems to have different rules for different customers.
* Role based programming does not allow for data-specific or horizontal access control rules.
* Large codebases with many access control checks can be difficult to audit or verify the overall application access control policy.

Instead, please consider the following access control programming methodology:

```

    if (user.hasAccess("DELETE_ACCOUNT")) {
        deleteAccount();
    }
```

Attribute or feature-based access control checks of this nature are the starting point to building well-designed and feature-rich access control systems. This type of programming also allows for greater access control customization capability over time.

### 6) Log All Access Control Events
All access control failures should be logged as these may be indicative of a malicious user probing the application for vulnerabilities.

## Vulnerabilities Prevented
* [OWASP Top 10 2017-A5-Broken Access Control](https://www.owasp.org/index.php/Top_10-2017_A5-Broken_Access_Control)
* [OWASP Mobile Top 10 2014-M5 Poor Authorization and Authentication](https://www.owasp.org/index.php/Mobile_Top_10_2014-M5)

## References
* [OWASP Cheat Sheet: Access Control](https://www.owasp.org/index.php/Access_Control_Cheat_Sheet)
* [OWASP Cheat Sheet:  iOS Developer - Poor Authorization and Authentication](https://www.owasp.org/index.php/IOS_Developer_Cheat_Sheet#Remediations_5)
* [OWASP Testing Guide: Testing for Authorization](https://www.owasp.org/index.php/Testing_for_Authorization)

## Tools
* [OWASP ZAP](https://www.owasp.org/index.php/ZAP) with the optional [Access Control Testing](https://github.com/zaproxy/zap-extensions/wiki/HelpAddonsAccessControlConcepts) add-on
