# 2. Design

This chapter describes how to design software to be secure, focusing on key secure design principles such as least privilege, complete mediation, and input validation.

Learning objectives:

1. Explain what secure design principles are and provide examples of some key widely-accepted principles.

2. Discuss the concept of least privilege.

3. Discuss complete mediation (“non-bypassability”), including common mistakes.

4. Understand input validation on an environment you can trust.

5. Discuss other widely-accepted secure design principles, particularly those identified by Saltzer and Schroeder.

## Secure Design Basics

### What Are Security Design Principles?

When you write non-trivial software, you have to break the problem into smaller components that work together. This process of deciding how to break a problem into components and how they will work together is called *design* or *architectural design*. For example, you are designing when you are trying to decide how to break a problem into a particular set of classes and methods. The result of those decisions is also called a design or architectural design. The word “design” is also used to describe user interface design, but that is not the sense we mean here.

Remember that the design process, like any other software development process, doesn’t happen just once. It is really common to try to implement some software, realize that the design doesn’t work, and then change the design. You often have to change a design when you change what the software does. So the design process happens whenever you think about changing how to break the problem down in your software.

Some designs are better than others: some are easier to maintain, faster, and so on. In particular, some designs are more secure than other designs. There is no magic trick that guarantees that your design is secure. But people have been developing software for decades, and through experience, they have identified a set of *design principles* that can help you choose good designs over bad ones.

Design principles are broadly accurate guides based on experience and practice. Put another way, design principles are rules of thumb for helping you quickly avoid a bad design and guiding you to a good design instead. Secure design principles do not guarantee security, though; they are an aid to thinking, not a replacement for thinking. For example, sometimes a principle will not apply at all. Sometimes principles clash; for example, one secure design principle is keeping things simple, but sometimes you need more complexity to get something else done. In rarer cases, there may be good reasons from a security point of view to even completely violate a principle. That said, your software will generally be more secure if you think about secure design principles and try to apply them. Secure design principles are distilled wisdom, and you would be wise to consider them.

When thinking about your design, you need to think about what components you can trust (and how much), and what components you cannot necessarily trust. Some design principles talk about a *trust boundary*. The trust boundary is simply the boundary between the components you trust and the components you do not necessarily trust. Where the trust boundary is depends on what software you are developing:

* If you are writing a server-side application, you presumably trust what you are running on (e.g., the computer, operating system, and container runtime if there), but not the external client systems (some of which might be controlled by an attacker). The trust boundary is between the server and the clients.

* If you are writing a mobile (smartphone) application that talks to a server you control, you presumably trust that remote server. You should not trust the communication path between your mobile application and server (so you will want to use TLS to encrypt it). You certainly should not trust other applications on the smartphone, unless you have special reason to trust one. So clearly, there is a boundary between your mobile application and (1) the general Internet and (2) other mobile applications. Trust is often not absolute; you probably trust that the mobile smartphone operating system will run for that user, but that user might be an attacker, so you should probably ensure that some secrets never get into the mobile application at all.