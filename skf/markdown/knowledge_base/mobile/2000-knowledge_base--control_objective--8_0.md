## Description:

## Control Objective

V8: Resilience Requirements

This section covers defense-in-depth measures recommended for apps that process, or give access to, sensitive data or functionality. Lack of any of these controls does not cause a vulnerability - instead, they are meant to increase the app’s resilience against reverse engineering and specific client-side attacks.

The controls in this section should be applied as needed, based on an assessment of the risks caused by unauthorized tampering with the app and/or reverse engineering of the code. We suggest consulting the OWASP document “Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention” for a list of business risks as well as associated technical threats.

For any of the controls in the list below to be effective, the app must fulfil at least all of MASVS-L1 (i.e., solid security controls must be in place), as well as all lower-numbered requirements in V8. For examples, the obfuscation controls listed in under “impede comprehension” must be combined with “impede dynamic analysis and tampering” and “device binding”.

Note that software protections must never be used as a replacement for security controls. The controls listed in MASVR-R are intended to add threat-specific, additional protective controls to apps that also fulfil the MASVS security requirements.

The following considerations apply:
	1. A threat model must be defined that clearly out lines the client-side threats that are to be defended. Additionally, the grade of protection the scheme is meant to provide must be specified. For example, a stated goal could be to force authors of targeted malware seeking to instrument the app to invest significant manual reverse engineering effort.
	2. The threat model must be credible and relevant. For example, hiding a cryptographic key in a whitebox implementation might prove redundant if an attacker can simply code-lift the white-box as a whole.
	3. The effectiveness of the protection should always be verified by a human expert with experience in testing the particular types of anti-tampering and obfuscation used (see also the “reverse engineering” and “assessing software protections” chapters in the Mobile Security Testing Guide).


## Mitigation:

empty control