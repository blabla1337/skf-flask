### Widely-Recommended Secure Design Principles

Software has been under attack for decades, and many key secure design principles were identified in 1975 by Jerome H. Saltzer and Michael D. Schroeder (S&S) in their paper, [*The Protection of Information in Computer Systems*](http://web.mit.edu/Saltzer/www/publications/protection/index.html). What is great about their list is that it has stood the test of time; these principles are just as important today. Other principles have been identified since then, but let’s start with their list.

In their list they focus on the *protection system* - that is, the part of the system that the security depends on. Here is their list, along with some alternative names:

1. **Least privilege**
Each (human) user and program should operate using the fewest privileges possible. This principle limits the damage from an accident, error, or attack. It also reduces the number of potential interactions among privileged programs, so unintentional, unwanted, or improper uses of privilege are less likely to occur.

2. **Complete mediation (aka non-bypassability)**
Every access attempt must be checked; position the mechanism so it cannot be subverted. A synonym for this goal is non-bypassability.

3. **Economy of mechanism (aka simplicity)**
The system, in particular the part that security depends on, should be as simple and small as possible.

4. **Open design**
The protection mechanism must not depend on attacker ignorance. Instead, you should act as if the mechanism is publicly known, and instead depend on the secrecy of relatively few and easily changeable items like passwords or private keys. An attacker should not be able to break into a system just because the attacker knows how it works. “Security through obscurity” generally does not work.

5. **Fail-safe defaults**
The default installation should be the secure installation. If it’s not certain that something should be allowed, don’t allow it.

6. **Separation of privilege (e.g., use two-factor authentication)**
Access to objects should depend on more than one condition (such as having a password). That way, if an attacker manages to break one condition (e.g., by stealing a key) the system remains secure. Note: sometimes programs are broken into parts, each part with a different privilege. This approach is sometimes confusingly called “privilege separation” - but breaking a program into parts with different privileges is something else. In this terminology, that is an example of least privilege.

7. **Least common mechanism (aka minimize sharing)**
Minimize the amount and use of shared mechanisms. Avoid sharing files, directories, operating system kernel execution, or computers with something you do not trust, because attackers might exploit them.

8. **Psychological acceptability (aka easy to use)**
The human interface must be designed for ease of use so users will routinely and automatically use the protection mechanisms correctly.

Since then, other secure design principles have also been identified by different people; we will cover a few of those throughout the course.

Remember, design principles are simply rules of thumb. As you break your problem down to solve it, you should think about these principles, because they will help guide you to creating more secure software. There are some cases where you will have good reasons to *not* apply them. These principles do not replace thinking - they help *guide* you when you are thinking.

Next, we will look in more detail at a few of these principles, because they have ramifications that might not be obvious. In the next unit we’ll start by looking at *least privilege*.