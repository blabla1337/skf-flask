# Introduction
The OWASP Top Ten Proactive Controls 2018 is a list of security techniques that should be considered for every software development project. This document is written for developers to assist those new to secure development.

One of the main goals of this document is to provide concrete practical guidance that helps developers build secure software. These techniques should be applied proactively at the early stages of software development to ensure maximum effectiveness.

## The Top 10 Proactive Controls
The list is ordered by importance with list item number 1 being the most important:

* C1: Define Security Requirements
* C2: Leverage Security Frameworks and Libraries
* C3: Secure Database Access
* C4: Encode and Escape Data
* C5: Validate All Inputs
* C6: Implement Digital Identity
* C7: Enforce Access Controls
* C8: Protect Data Everywhere
* C9: Implement Security Logging and Monitoring
* C10: Handle All Errors and Exceptions

## How this List Was Created

This list was originally created by the current project leads with contributions from several volunteers. The document was then shared globally so even anonymous suggestions could be considered. Hundreds of changes were accepted from this open community process.

## Target Audience
This document is primarily written for developers. However, development managers, product owners, Q/A professionals, program managers, and anyone involved in building software can also benefit from this document. 

## How to Use this Document
This document is intended to provide initial awareness around building secure software. This document will also provide a good foundation of topics to help drive introductory software security developer training. These controls should be used consistently and thoroughly throughout all applications. However, this document should be seen as a starting point rather than a comprehensive set of techniques and practices. A full secure development process should include comprehensive requirements from a standard such as the OWASP ASVS in addition to including a range of software development activities described in maturity models such as [OWASP SAMM](https://www.owasp.org/index.php/OWASP_SAMM_Project) and [BSIMM](https://www.bsimm.com/).

## Link to the OWASP Top 10 Project
The OWASP Top 10 Proactive Controls is similar to the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) but is focused on defensive techniques and controls as opposed to risks. Each technique or control in this document will map to one or more items in the *risk based* OWASP Top 10. This mapping information is included at the end of each control description.
