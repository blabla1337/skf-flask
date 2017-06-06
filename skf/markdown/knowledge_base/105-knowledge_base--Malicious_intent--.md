# Malicious intent
-------

## Description:

Before pushing a code live you should check the software for malicious code in order to
make sure no developers with evil intent made backdoors or deliberately put in exploits.

Dependencies and third party libraries should also be validated against malicious code.
These depedencies and libraries should also be validated for known vulnerabilities (CVE)

## Solution:

Running your code through a static code analyzer or auditing tools could give you a chance
to find malicious pieces of code which could be embedded into the software.
Also if the new or adjusted functionality is critical then check manually it in the form
of a code review for back doors, Easter eggs, and logic flaws.

This should also mean that authorized administrators must have the capability to verify the integrity of
all security-relevant configurations to ensure that they have not been tampered with.

Determine also that the business logic of high-value transactions is not imported from untrusted third party libraries.

Note:
Studies have shown backdoors written by employees with malicious intend will propably do this within
the first half year of their employment. The implementing of back doors has little to do with how happy an
employee is with the current employer, it has proven to be a trait of character rather than a trait of discontent.
