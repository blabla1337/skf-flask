### OS Command (Shell) injection

Another kind of injection attack is the operating system (OS) injection attack, also known as a shell injection attack. This is similar to an SQL injection attack; the problem is that information (usually text), some of it trusted and some from an attacker, is sent to an interpreter that executes what it is sent. The difference is that instead of being sent to a database, this mixture is sent to the OS command interpreter, aka the command shell.

Most systems have at least one command shell. Even small embedded systems, like televisions and routers, often have a command shell inside. Shells are useful for many things, including quickly combining programs, doing some queries, debugging, and so on. Many Unix-like systems, including typical Linux distributions, have multiple shells available including bash, dash, ksh, zsh, and csh; at least one of those is installed as **/bin/sh** or **/usr/bin/sh**. MacOS similarly comes with a shell and others can be easily installed. Windows systems typically use different shells with very different syntax (**cmd.exe**, **command.exe**, or PowerShell), but they have shells too.

A shell is a program that directly takes commands and runs programs as commanded. Since this is useful, many programming languages make it easy to call out to a shell. In particular, many languages have a way to dynamically construct a call to a shell and then execute it. However, it is easy to make mistakes when combining attacker data into a command to be run by a shell. In particular, try to avoid dynamically creating a mixture of commands and attacker-provided data to then be executed by the shell. Instead, try to find an alternative that is easier to use securely.

If all you want to do is call another program and pass it some parameters, try to do that without dynamically creating and then interpreting a shell command at all! Instead, try to call the program directly. This is more efficient anyway, and this is far easier (and more likely) to be secure if any of those parameters might include data from an attacker. For example:

* In C, prefer **execve(3)** (it does not use the shell) instead of using **system(3)** (which does use the shell).

* In Python, prefer using **shell=False** (the default) with **subprocess.run()** or  **subprocess.call()**, instead of using **shell=True** or **os.system()**

* In JavaScript Node.js, prefer using **shell=False** (the default) with **child_process.spawn()** or **child_process.execFile()** instead of using **shell=True** or **child_process.exec()**

In short: if you see code that concatenates strings for execution by a shell, and that concatenation includes untrusted input, be extremely concerned. While it is possible to do this securely, it is better avoided when you reasonably can.

If you must call a program through a shell, and also include some data that might be provided by an attacker, you need to use it securely. That is actually rather tricky. As always, *do not use a denylist*. There are many “lists of shell metacharacters” that are wrong because they miss some. So if you are sending data through a shell, you need to escape every character except for ones on an allowlist (characters you know are *not* metacharacters). Generally, A-Z, a-z, and 0-9 are not metacharacters, and after that, check very carefully. Make sure you quote everything as needed.

Of course, if you are calling a program with any data that might be from an attacker, you need to make sure that the data will not be misinterpreted. For example, make sure your command-line options will be correctly interpreted; if an attacker can cause the initial character to be “**-**” or “**/**” in a parameter, then they might be misinterpreted as an option or root directory. Anything passed in (e.g., by parameter or anything else) must be carefully escaped to prevent attack. This brings us to the topic of filenames, which we will cover next.

OS command injection is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #11. It is [CWE-78](https://cwe.mitre.org/data/definitions/78.html), *Improper Neutralization of Special Elements used in an OS Command (‘OS Command Injection’)*.