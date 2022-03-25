### Security Requirements

To create software, you need to know what you want it to do. Requirements are simply what a product or service needs to do or be. For our purposes, we will include in requirements anything required by law or regulation, as well as anything important to its (potential) customers/users. If you are being paid to develop software, requirements are typically written down somewhere.

In some cases there are special laws or regulations that you must comply with. This is especially true in areas where vulnerabilities are more likely to lead to significant harm (such as medical, financial, and military systems). This also arises if you are planning to sell software, or a system with software, in many different legal jurisdictions (so there may be many laws or regulations that apply). Again, for our purposes these are all requirements.

Requirements might not be recorded in a single formal document. Sometimes each specific new requirement is simply accepted as an issue in an issue/bug tracker. In most software development projects, the requirements are identified over time in discussions with its users.

Requirements don’t even *have* to be written down to be used, especially for a small project. However, in the case of security (at least), it is a good idea to record the high-level security requirements in one place. That way, when someone is thinking about using your software, or may modify it, they’ll have an idea of what the system is trying to accomplish for security.

Of course, the actual requirements depend on what you’re trying to accomplish.

So how can you determine the security requirements for a particular system? One way to identify security requirements is to think about the common security objectives and supporting security functions we have *already* discussed and determine the specific requirements for your system in each category. In particular, think about how each one applies to the kind of information your program will manage. Let’s walk through each security objective and supporting security function, and discuss some things to consider:

1. **Confidentiality** (“No unauthorized read”)
Identify information that should not be publicly revealed, such as private information about people and systems. Who should be allowed to see that? Can you avoid having that information at all (since you cannot reveal what you do not have)? If you store password information so people can log in to your system (aka “inbound” authentication), you need to store this password information using special algorithms designed for it (such as Argon2id), as we will discuss later.

2. **Integrity** (“No unauthorized modification”)
Identify information that only some people should be allowed to modify, and who that is.

3. **Availability** (“Keeps working in presence of attack”)
What is the impact if it does not work for a while - is that serious? Availability is rarely an absolute. If your system is accessible via the internet, availability is very challenging to provide; a well-resourced attacker can always use a Distributed Denial of Service (DDoS) attack to take down a site, at least for a little while. It is possible to work to counter DDoS attacks, but in the end it can turn into a competition between how many resources each side has.
    
Even when availability cannot be universally guaranteed, you can still have secure software by focusing on the bigger-risk items ([Not all attackers are equal: understanding and preventing DoS in web applications](https://r2c.dev/blog/2020/understanding-and-preventing-dos-in-web-apps/), by Jacob Kaplan-Moss, 2020).  In many cases, focus on developing your software so it is not *easy* to overwhelm or take down with simple inputs; make it possible to temporarily scale up the software by rapidly adding new servers; and implement the software so it quickly recovers when an attack ends. To counter the risk that the system might be destroyed or have its data deleted, design the software so its data is easily backed up, and plan for backups. Ensure that data can be backed up to “cold storage” (where the data cannot be corrupted later if the software is subverted). If the system is routinely backed up in operations, you can recover relatively quickly (at least partially). So yes, you *can* have availability as a requirement, as long as its limitations are clear.

4. **Non-repudiation** (“Prove someone did something”)
Is there some action that you want to be able to *prove* someone took? In many systems this is not critical, but in some it is.

5. **Identity & authentication (I&A)**
How will users prove who they are? You want to make sure that someone cannot spoof a legitimate user. You should normally support two-factor authentication (2FA), either directly or by allowing users to prove their identity via some other service that supports it.

6. **Authorization**
Who is allowed to do what? This is a part of confidentiality and integrity, but if you think about people’s roles in addition to thinking about the information to protect, you will probably get a better picture.

7. **Auditing/Logging**
What information/events should you record? Typically you at least record login, logout, and important events like user account creation and deletion. Generally a system should record when something happened (date and time), what happened, what system component did it, and who caused it to happen.

You will sometimes see documents that use the security terms “subject” and “object”. A “subject” is something that acts (e.g., a user or process). An “object” is something being acted on (e.g., a file or network port).

Some developers capture some requirements as *use cases*. Each use case is a list of interactions between actor(s) and a system to achieve a goal. This has led to an interesting security approach, the development of *abuse cases* or *misuse cases*. An abuse case is a list of interactions between actors and a system that are intended to cause harm (e.g., to the system, actor(s), or stakeholders). A very similar term is “misuse case”, a description of a malicious act against a system. Many have found it useful to define abuse cases or misuse cases to then describe how the system must *counter* such abuse/misuse. By thinking about abuse and misuse, and figuring out how to counter them early, a lot of mischief can be prevented. Many developers find it hard to *think like an attacker*, so throughout this course we will focus on techniques to help you find vulnerabilities anyway, for example, by identifying common types of vulnerabilities and explaining how to systematically do threat modeling.

An important aspect about security requirements is what kind of attackers you expect to counter. Countering targeted attacks by well-resourced nation-states is extremely difficult; you need to know and apply more than this course can cover by itself. However, most people are not trying to develop systems that withstand these kinds of attacks. In this course, we will assume that your software must stand up to attacks that a typical commercial site might need to counter, where the attacker has limited resources and the attacks are often not highly targeted. If you need to defend against attackers with more resources, you will probably need to do much more, but the material in this course will give you a good starting point.

Note that in this course we focus on attackers, not hackers. In the computer community the term “hacker” is widely used to identify *“a person who delights in having an intimate understanding of the internal workings of a system, computers and computer networks in particular.”* ([IETF RFC 1983](https://tools.ietf.org/html/rfc1983)). By this definition, many hackers never attack computer systems, and many attackers are not hackers. This course focuses on foiling attackers.

If you are looking for ideas for potential security requirements, one source is the [*Common Criteria for Information Technology Security Evaluation” (CC) part 2*](https://www.commoncriteriaportal.org/), which is freely available. The CC is an international standard for evaluating security that was originally developed in 1994. The vast majority of software developed today does not undergo a CC evaluation, in part because it is often both expensive and time-consuming to have an external lab formally evaluate your software using the CC. However, you can still look at the CC for ideas even if you will not use an evaluation lab. The CC is publicly available and has 3 parts: part 1 is an introduction, part 2 is a list of common security functional requirements, and part 3 is a list of common assurance requirements. Part 2 in particular is a list of *“security functions you might require”*. If you suspect your system will need some special security requirements, but are not sure what those might be, part 2 provides a long list of ideas that might be useful. Some of its terminology is arcane, but it includes a glossary which can help.

**Finally:** If there is existing software that does something like the software you are developing, look at its security capabilities. They added those capabilities for a reason, and your software might need at least some of them as well.
