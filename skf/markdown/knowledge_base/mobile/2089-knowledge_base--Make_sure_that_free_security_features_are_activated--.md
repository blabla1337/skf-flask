## Description:

Make Sure That Free Security Features Are Activated

MSTG-CODE-9: Free security features offered by the toolchain, such as byte-code minification, stack protection, PIE support and automatic reference counting, are activated.

Both iOS and Android platforms present many security features and enabling them help to increase application security.


## Mitigation:

For iOS, Xcode enables all binary security features by default, it may be relevant to verify this for an old application or to check for the misconfiguration of compilation options. The following features are applicable:

	- ARC - Automatic Reference Counting - A memory management feature that adds retain and release messages when required
	- Stack Canary - Helps prevent buffer overflow attacks by means of having a small integer right before the return pointer. A buffer overflow attack often overwrites a region of memory in order to overwrite the return pointer and take over the process-control. In that case, the canary gets overwritten as well. Therefore, the value of the canary is always checked to make sure it has not changed before a routine uses the return pointer on the stack.
	- PIE - Position Independent Executable - enables full ASLR for binary

And for Android, because decompiling Java classes is trivial, applying some basic obfuscation to the release byte-code is recommended. [ProGuard](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x08-Testing-Tools.md#proguard) offers an easy way to shrink and obfuscate code and to strip unneeded debugging information from the byte-code of Android Java apps. It replaces identifiers, such as class names, method names, and variable names, with meaningless character strings. This is a type of layout obfuscation, which is "free" in that it doesn't impact the program's performance.

Since most Android applications are Java-based, they are [immune to buffer overflow vulnerabilities](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow "Java Buffer Overflows"). Nevertheless, a buffer overflow vulnerability may still be applicable when you're using the Android NDK; therefore, consider secure compiler settings.
