# Sandboxing
-------

## Description:

A sandbox is a security mechanism for separating running programs.
It is often used to execute untested code, or untrusted programs from
unverified third parties, suppliers, untrusted users and untrusted websites. It's creating
an extra layer of security where an attacker first need to break out from.

## Solution:

Examples of sandbox implementations include the following:

A jail: 
network-access restrictions, and a restricted filesystem namespace. Jails are most commonly used in virtual hosting.

Rule-based executiongives users full control over what processes are started, spawned (by other applications), or allowed to inject code into other applications and have access to the net, by having the system assign access levels for users or programs according to a set of determined rules. It also can control file/registry security (what programs can read and write to the file system/registry). In such an environment, viruses and trojans have fewer opportunities of infecting a computer. The SELinux and Apparmor security frameworks are two such implementations for Linux.

Virtual machines emulate a complete host computer, on which a conventional operating system may boot and run as on actual hardware. The guest operating system runs sandboxed in the sense that it does not function natively on the host and can only access host resources through the emulator.

Sandboxing on native hosts: Security researchers rely heavily on sandboxing technologies to analyse malware behaviour. By creating an environment that mimics or replicates the targeted desktops, researchers can evaluate how malware infects and compromises a target host. Numerous malware analysis services are based on the sandboxing technology.

Capability systems can be thought of as a fine-grained sandboxing mechanism, in which programs are given opaque tokens when spawned and have the ability to do specific things based on what tokens they hold. Capability-based implementations can work at various levels, from kernel to user-space. An example of capability-based user-level sandboxing involves HTML rendering in a Web browser.

Secure Computing Mode (seccomp) is a sandbox built in the Linux kernel. When activated, seccomp only allows the write(), read(), exit(), and sigreturn() system calls.

HTML5 has a "sandbox" attribute for use with iframes.

Java virtual machines include a sandbox to restrict the actions of untrusted code, such as a Java applet.

The .NET Common Language Runtime provides Code Access Security to enforce restrictions on untrusted code.
```
