## Description:

Protect sensitive computations with obfuscation

MSTG-RESILIENCE-12: If the goal of obfuscation is to protect sensitive computations, an obfuscation scheme is used that is both appropriate for the particular task and robust against manual and automated de-obfuscation methods, considering currently published research. The effectiveness of the obfuscation scheme must be verified through manual testing. Note that hardware-based isolation features are preferred over obfuscation whenever possible.

Obfuscation can be used to protect sensitive data and critical processes from attackers perspective. Application will run on client side, which is a totally un-trusted environment, hence the obfuscation effectiveness should be tested and verified. 


## Mitigation:

Security best practices and industry standards should be implemented and verified by manual/automated testing with considering currently published researches and de-obfuscation methods to ensure a sophisticated way of protection takes place.

Hardware-based isolation is a better option over software obfuscation.