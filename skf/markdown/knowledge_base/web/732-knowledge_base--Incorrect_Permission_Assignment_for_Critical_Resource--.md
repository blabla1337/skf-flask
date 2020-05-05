## Description:

The product specifies permissions for a security-critical resource in a way that allows that resource to be read or modified by unintended actors.

When a resource is given a permissions setting that provides access to a wider range of actors than required, it could lead to the exposure of sensitive information, or the modification of that resource by unintended parties. This is especially dangerous when the resource is related to program configuration, execution or sensitive user data.

## Mitigation:


PHASE:Implementation:
When using a critical resource such as a configuration file, check to see if the resource has insecure permissions (such as being modifiable by any regular user) [REF-62], and generate an error or even exit the software if there is a possibility that the resource could have been modified by an unauthorized party.

PHASE:Architecture and Design:
Divide the software into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully defining distinct user groups, privileges, and/or roles. Map these against data, functionality, and the related resources. Then set the permissions accordingly. This will allow you to maintain more fine-grained control over your resources. [REF-207]:EFFECTIVENESS:Moderate

PHASE:Architecture and Design Operation:STRATEGY:Sandbox or Jail:
Run the code in a jail or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.:EFFECTIVENESS:Limited

PHASE:Implementation Installation:
During program startup, explicitly set the default permissions or umask to the most restrictive setting possible. Also set the appropriate permissions during program installation. This will prevent you from inheriting insecure permissions from any user who installs or runs the program.:EFFECTIVENESS:High

PHASE:System Configuration:
For all configuration files, executables, and libraries, make sure that they are only readable and writable by the software's administrator.:EFFECTIVENESS:High

PHASE:Documentation:
Do not suggest insecure configuration changes in documentation, especially if those configurations can extend to resources and other programs that are outside the scope of the application.

PHASE:Installation:
Do not assume that a system administrator will manually change the configuration to the settings that are recommended in the software's manual.

PHASE:Operation System Configuration:STRATEGY:Environment Hardening:
Ensure that the software runs properly under the Federal Desktop Core Configuration (FDCC) [REF-199] or an equivalent hardening configuration guide, which many organizations use to limit the attack surface and potential risk of deployed software.

