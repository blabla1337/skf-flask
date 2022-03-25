### Other Design Principles

Many other design principles have been proposed, based on problems that have happened to past systems. Next, we will take a look at a few other design principles that you should consider.

#### Beware of Race Conditions

A *race condition* happens when a system’s correct behavior depends on the sequence of events, but there is no control over that sequence. Race conditions generally involve one or more processes or threads accessing a shared resource, but this multiple access has not been properly controlled.

If there is no control at all, that is a defect, and it might even be a vulnerability. Many programs, to be secure, have to do two things: (1) determine if a request is authorized, and (2) if it is, act on that request. If it is possible for an attacker to change the situation between steps 1 and 2, then the program could correctly determine that it is authorized, but then allow a different action that was *not* authorized. This kind of security mistake is so common that it has a name,  a *time of check - time of use* (TOCTOU) race condition.

In many situations, the right way to counter TOCTOU race conditions is to implement and use APIs that both check the authorization and perform the action *simultaneously* (that is, they will not allow an attacker to change the situation between the check and the use). For example:

1. When you create files or anything else that has privileges associated with it, do not create them and then try to reduce their privileges. Instead, create them with very minimal privileges and expand them as needed. That way, there is no window of time where an attacker might be able to exploit the excess permissions.

2. If you are writing a program for a Unix-like system, do not call **access()** to see if a file can be opened, followed by a call to **open()** to actually open the file. Instead, set things up to just call **open()** directly, since **open()** includes a check to see if the access is permitted.

3. If you want to create a new file on a Unix-like system, make sure you request that it be created *exclusively* (**O_EXCL** in the C **open()** API, and the letter **x** in **fopen()** and the option flags used in many other programming languages). Again, that way there is no window of opportunity for an attacker to create the file before the program can (if the attacker could do so).

Race conditions are such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #29. *Concurrent Execution using Shared Resource with Improper Synchronization (‘Race Condition’)* is [CWE-362](https://cwe.mitre.org/data/definitions/362.html).

#### Harden the System

Defects happen! But they don’t need to necessarily turn into vulnerabilities. Instead, try to design your system so a single defect is much less likely to result in complete compromise. This is basically a specific application of the least privilege principle, but if you think specifically about making the system hard to subvert *even* when there is a defect in it, you may identify other steps you can take.

#### Keep Secrets Secret

If your software manages secrets like private cryptographic keys and passwords, make sure they stay secret. In particular:

* Do not put live secrets in your source code. Source code is managed by version control systems and often gets spread to more people and systems than you might think.

* Store passwords used for inbound authentication with an algorithm specifically designed to do this. We will discuss these later in the course, but these kinds of algorithms are called *iterated per-user salted hash* algorithms. If done correctly, it is infeasible for an attacker to determine many passwords even if the attacker gets the encrypted password data.

#### Trust Only Trustworthy Channels

In general, only trust information (input or results) from trustworthy channels. For example, use **https://** instead of **http://**, because that checks if the server on the other side has a valid cryptographic certificate for that site. In general you should use **https**, because that will prevent attackers from snooping or modifying information exchanged with other users.

#### Separate Data from Control

A useful trick for developing more secure software is to separate data from control (aka programs). Put another way, you should separate the passive data from programs that are executed. That way, if an attacker manages to slip in “extra” information into data, that will not cause a potentially-malicious program to be executed. This is basically another way to implement least privilege - don’t give data the right to run as a program.

A good example of this is the Content Security Policy (CSP) supported by modern web browsers. CSP lets you state that the HTML being sent is only data, and is *not* allowed to provide inline scripts (programs) or styles (which can also be programs) - instead, the scripts and styles may only be downloaded from specified trusted places. That way, if an attacker manages to subvert the HTML, the attacker will not be able to cause attacker-provided programs to be run.