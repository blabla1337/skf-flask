##Description:

The software generates an error message that includes sensitive information about its environment, users, or associated data.

The sensitive information may be valuable information on its own (such as a password), or it may be useful for launching other, more serious attacks. The error message may be created in different ways: self-generated: the source code explicitly constructs the error message and delivers it externally-generated: the external environment, such as a language interpreter, handles the error and constructs its own message, whose contents are not under direct control by the programmer An attacker may use the contents of error messages to help launch another, more focused attack. For example, an attempt to exploit a path traversal weakness (CWE-22) might yield the full pathname of the installed application. In turn, this could be used to select the proper number of .. sequences to navigate to the targeted file. An attack using SQL injection (CWE-89) might not initially succeed, but an error message could reveal the malformed query, which would expose query logic and possibly even passwords or other sensitive information used within the query.

##Mitigation:


PHASE:Implementation:
Ensure that error messages only contain minimal details that are useful to the intended audience, and nobody else. The messages need to strike the balance between being too cryptic and not being cryptic enough. They should not necessarily reveal the methods that were used to determine the error. Such detailed information can be used to refine the original attack to increase the chances of success. If errors must be tracked in some detail, capture them in log messages - but consider what could occur if the log messages can be viewed by attackers. Avoid recording highly sensitive information such as passwords in any form. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a username is valid or not.

PHASE:Implementation:
Handle exceptions internally and do not display errors containing potentially sensitive information to a user.

PHASE:Implementation:STRATEGY:Attack Surface Reduction:
Use naming conventions and strong types to make it easier to spot when sensitive data is being used. When creating structures, objects, or other complex entities, separate the sensitive and non-sensitive data as much as possible.:EFFECTIVENESS:Defense in Depth

PHASE:Implementation Build and Compilation:STRATEGY:Compilation or Build Hardening:
Debugging information should not make its way into a production release.

PHASE:Implementation Build and Compilation:STRATEGY:Environment Hardening:
Debugging information should not make its way into a production release.

PHASE:System Configuration:
Where available, configure the environment to use less verbose error messages. For example, in PHP, disable the display_errors setting during configuration, or at runtime using the error_reporting() function.

PHASE:System Configuration:
Create default error pages or messages that do not leak any information.

