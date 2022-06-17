# C1: Define Security Requirements

## Description

A security requirement is a statement of needed security functionality that ensures one of many different security properties of software is being satisfied. Security requirements are derived from industry standards, applicable laws, and a history of past vulnerabilities. Security requirements define new features or additions to existing features to solve a specific security problem or eliminate a potential vulnerability.

Security requirements provide a foundation of vetted security functionality for an application. Instead of creating a custom approach to security for every application, standard security requirements allow developers to reuse the definition of security controls and best practices. Those same vetted security requirements provide solutions for security issues that have occurred in the past. Requirements exist to prevent the repeat of past security failures.

### The OWASP ASVS
[The OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) is a catalog of available security requirements and verification criteria. OWASP ASVS  can be a source of detailed security requirements for development teams.

Security requirements are categorized into different buckets based on a shared higher order security function. For example, the ASVS contains categories such as authentication, access control, error handling / logging, and web services. Each category contains a collection of requirements that represent the best practices for that category drafted as verifiable statements.

### Augmenting Requirements with User Stories and Misuse Cases

The ASVS requirements are basic verifiable statements which can be expanded upon with user stories and misuse cases. The advantage of a user story or misuse case is that it ties the application to exactly what the user or attacker does to the system, versus describing what the system offers to the user. 

Here is an example of expanding on an ASVS 3.0.1 requirement. From the "Authentication Verification Requirements" section of ASVS 3.0.1, requirement 2.19 focuses on default passwords.

    2.19 Verify there are no default passwords in use for the application framework 
        or any components used by the application (such as "admin/password").

This requirement contains both an action to verify that no default passwords exist, and also carries with it the guidance that no default passwords should be used within the application.

A user story focuses on the perspective of the user, administrator, or attacker of the system, and describes functionality based on what a user wants the system to do for them. A user story takes the form of "As a user, I can do x, y, and z".

    As a user, I can enter my username and password to gain access to the application.
    As a user, I can enter a long password that has a maximum of 1023 characters.

When the story is focused on the attacker and their actions, it is referred to as a misuse case.

    As an attacker, I can enter in a default username and password to gain access.
    

This story contains the same message as the traditional requirement from ASVS, with additional user or attacker details to help make the requirement more testable.

## Implementation
Successful use of security requirements involves four steps. The process includes discovering / selecting, documenting, implementing, and then confirming correct implementation of new security features and functionality within an application. 

### Discovery and Selection
The process begins with discovery and selection of security requirements. In this phase, the developer is understanding security requirements from a standard source such as ASVS and choosing which requirements to include for a given release of an application. The point of discovery and selection is to choose a manageable number of security requirements for this release or sprint, and then continue to iterate for each sprint, adding more security functionality over time.

### Investigation and Documentation
During investigation and documentation, the developer reviews the existing application against the new set of security requirements to determine whether the application currently meets the requirement or if some development is required. This investigation culminates in the documentation of the results of the review.

### Implementation
After the need is determined for development, the developer must now modify the application in some way to add the new functionality or eliminate an insecure option. In this phase the developer first determines the design required to address the requirement, and then completes the code changes to meet the requirement.

### Test
Test cases should be created to confirm the existence of the new functionality or disprove the existence of a previously insecure option.

## Vulnerabilities Prevented
Security requirements define the security functionality of an application. Better security built in from the beginning of an applications life cycle results in the prevention of many types of vulnerabilities. 

## References
* [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
* [OWASP Mobile Application Security Verification Standard (MASVS)](https://owasp.org/www-project-mobile-security-testing-guide/)
* [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
