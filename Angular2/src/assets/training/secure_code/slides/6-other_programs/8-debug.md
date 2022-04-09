### Debug and Assertion Code

Sometimes vulnerabilities stem from debug and assertion code; let’s talk about that.

#### Debug Code

Developers often insert code solely to gain visibility of what is going on. For example, when debugging, they may insert print statements. They may also do it to simplify testing or simply to gain understanding. By itself, that is fine, but there is a risk of leaving this debug code enabled in production. These are much more likely to lead to defects and security vulnerabilities, since they were not intended to be there in the released software.

So if you insert debug code, segregate it somehow so it is *easy* to automatically remove. It doesn’t matter how; naming conventions, compiler flags, and so on, can all work, as long as it is easy to do the *right* thing.

A good long-term strategy is to have a logging system enabled early, and either use that or transform your debug statements into logging statements. If you find it useful to see information now, it might be useful to see that later. That also means that instead of needing to remove the debug code, you can easily enable it later, even within a production system. This logging code must resist attack, just like the rest of the code.

#### Assertions

Many languages have “assert” statements or expressions to state something that is *supposed* to always be true at runtime. These can be useful for sanity checking of a program while it runs. Examples include Java’s **assert** statement, Python’s **assert** statement, C/C++/Rust’s **assert()** macro, and JavaScript Node.js’s **assert()** method. In most languages, if the assertion fails at runtime, then an exception is thrown.

Assertions are often great, because they can stop problems before they get more serious. However, if an attacker can cause an assertion to fail, that may lead to application exit or other behavior more severe than necessary. In particular, where practical:

* Avoid allowing an attacker to trigger an assertion. In particular, *never* use assertions for input validation of untrusted input. There are at least two good reasons:

1. Countering attacker input is *expected* behavior!

2. Assertions can often be disabled with compiler or runtime flags. This violates the principle of having non-bypassable input validation for security, because a perfectly reasonable optimization approach can accidentally disable a vital security need.

* Limit scope of the assertion response (exception handler) to the attacker’s session where you can. For example, try to crash just that connection, not all connections, if an assertion fails.

A *Reachable Assertion* (an assertion an attacker can trigger), [CWE-617](https://cwe.mitre.org/data/definitions/617.html), is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #40. 

Inserting assertions can make a verification technique called “fuzzing” more effective. So, it is often a good idea to have many assertions, as long as they are expressions that absolutely *should* always be true. We will discuss fuzzing in more detail later.