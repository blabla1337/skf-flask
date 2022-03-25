## How Can We Get There?

### Risk Management

Risks are *potential problems*. The key to developing adequately secure software is to manage the risks of developing insecure software, *before* they become problems.

#### The Need for Risk Management

All of life involves risk. It is unrealistic to expect that there will be no risks in life. In particular, there are risks to anyone using the software you develop because it may have vulnerabilities. When you develop software, you are likely to make mistakes, and some of those mistakes might eventually lead to security vulnerabilities. Someone may even try to intentionally insert vulnerabilities or malicious code into your software, or the software you depend on, during its development. Even very strong techniques for countering vulnerabilities must build on assumptions or can only eliminate *some* security-related risks, so again, it is unrealistic to expect there to be no risks.

But when you develop software, you should take reasonable steps to *manage* risks so that the risks are so low (both to its developers and users) that they are acceptable. In his book, [*“The Failure of Risk management: Why It’s Broken and How to Fix It”*](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119198536) (2009), Douglas Hubbard defines risk management as the *“identification, evaluation, and prioritization of risks… followed by coordinated and economical application of resources to minimize, monitor, and control the probability or impact of unfortunate events”*.

One of the risks when developing and deploying software is that attacker(s) will exploit its vulnerabilities and cause harm to others. You cannot prevent attackers from trying to attack the system. In fact:

** If people start using the software you develop, _expect_ that intelligent adversaries will try to attack it.**

But while you cannot prevent attackers from trying to attack it, you can make it difficult for an attack to succeed, or reduce the impact if an attack succeeds. You can do this by taking steps throughout software development and deployment to reduce the risks to an acceptably low level. If your software is widely-used or depended on for vital tasks, then it is especially important that you work to manage those risks to your users.

Do *not* wait to think about risks until they happen. Then they are no longer risks - they are *problems*. It is a lot easier and cheaper to address risks *before* they become problems! It is much easier to design the software to minimize risks than to change the software later. It is also better for the user, better for your professional reputation, and better for the reputation of that software.

#### Risk Management Process

Small projects with relatively low impacts can do risk management very informally. Large projects with major impacts should be more rigorous. But no matter what, risk management can be divided into the following activities (according to the US Department of Defense’s [*Risk, Issue, and Opportunity Management Guide for Defense Acquisition Programs*](http://acqnotes.com/wp-content/uploads/2017/07/DoD-Risk-Issue-and-Opportunity-Management-Guide-Jan-2017.pdf), 2017):

1. **Risk planning**. Determine your project’s risk management process.

2. **Risk identification**. Identify what *might* go wrong. A good trick is to look for similar projects - what risks and problems did they have? It is a good idea to write this list down so it can be shared. For our purposes, we are concerned about security-related risks.

3. **Risk analysis**. Determine the two key attributes of a risk: the **likelihood** of the undesirable event and the **severity** of its consequences. A risk becomes increasingly important if its likelihood and/or severity increases.

4. **Risk handling**. Determine what you will do about the risk. You have several options for each risk:

1. **Acceptance (& Monitoring)**: The risk is accepted, but monitored and communicated to its stakeholders (including its users). This is reasonable if the likelihood or severity are low.

2. **Avoidance**. The risk is eliminated by making some change. That is, you make its likelihood zero or its severity irrelevant. This is great when you can do it. For example, you might choose to *not* gather some data (then you cannot lose its confidentiality later), or you might choose a programming language where certain kinds of vulnerabilities cannot happen (eliminating the risks from those kinds of vulnerabilities).

3. **Transfer**. The risk is transferred to someone else, e.g., by buying insurance, or by changing the system so that another component has that risk and its developers accept it. For example, instead of taking on the risks of bad identification & authentication (I&A), depend on some existing system to do I&A.

4. **Control**. Actively reduce the risk to an acceptable level. Since the importance of a risk depends on its likelihood and severity, this means changing things to make the likelihood and/or severity low (or at least lower). For security-related risks, this is often what you need to do. There is no single way to do this, so instead you have to continuously reduce likelihood and severity through software development and deployment until the risks are acceptable. For example, you might:

1. Ensure all developers know about certain kinds of common mistakes that lead to a particular kind of vulnerability (so that they can avoid them),

2. Use approaches (such as secure design, specific programming languages, and APIs) that are designed to make those vulnerabilities less likely,

3. Use tools & reviews to catch mistakes (including vulnerabilities), and

4. Harden the system. Hardening a system means modifying a system so that defects are less likely to become security vulnerabilities. We will discuss hardening later in the course.

5. **Risk Monitoring**. Determine how the risks have changed over time. Over time, you should “burn down” your risks - that is, the steps you are taking should be continuously reducing the risk likelihood or severity to acceptable levels.

Risk management is *not* complicated. It is basically common sense. But when you are working on solving the current problems it is easy to forget about risks, which are only *potential* problems. A little thought *ahead* of time can eliminate potential problems before they become real problems.

#### Identifying Risks

Note that the first step (beyond planning) is identifying risks. But how do you identify the risks of security vulnerabilities? Clearly many people do *not* notice risks from security vulnerabilities.

Bruce Schneier has this wonderful story ([*The Security Mindset*](https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html), 2008): 

> *“Uncle Milton Industries has been selling ant farms to children since 1956. Some years ago, I remember opening one up with a friend. There were no actual ants included in the box. Instead, there was a card that you filled in with your address, and the company would mail you some ants. My friend expressed surprise that you could get ants sent to you in the mail. [Bruce Schneier] replied: ‘What’s really interesting is that these people will send a tube of live ants to anyone you tell them to.’ … Security requires a particular mindset. Security professionals -- at least the good ones -- see the world differently. They can’t walk into a store without noticing how they might shoplift. They can’t use a computer without wondering about the security vulnerabilities. They can’t vote without trying to figure out how to vote twice.”*

Can this mindset be taught? Our experience is that it can be, at least in part. Checklists, guidance, and tips help remind people to look for certain things, especially when they are built from relevant past experiences. Another technique that helps is working to develop a slightly paranoid mind-set. Not a clinical level of paranoia, but a constant low-level concern that there are many risks and that some people really are out to get you. Remember that some users will intentionally seek to cause rare, unlikely, or unexpected situations, in the hope that such attacks will give them unwarranted privileges. As a result, when writing secure programs, paranoia is a virtue. Talking about risks with others, reviewing plans with others, and continuously looking for risks can all help identify risks so that they can be addressed *before* they become problems.

#### Security Is A Process, Not A Product

In his essay, [*The Process of Security*](https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html) (2000), Bruce Schneier has famously explained that 

> *“security is a process not a product… there’s no such thing as perfect security. Interestingly enough, that’s not necessarily a problem. … Security does not have to be perfect, but the risks have to be manageable…”.*

The world changes. The ways your software is used changes. New vulnerabilities are discovered. The software’s platform and libraries change. Laws, company policies, and goals change.. Software that was secure a year or five ago may not be adequate today. 

Since security is a process, it is not just “fire and forget.” You need to continuously consider security.

#### Checklists Are Not Security

Do not equate checklists, guidelines, and tips with security. They are often *useful*, because they can help you identify risks and reasonable ways to handle them. Good checklists, guidelines, and tips can save you a lot of time and trouble, and they are also great aids for helping others evaluate the security of some software. Good ones are built on the experience of others, and you’d be foolish to ignore that experience.

But they are only aids to the real goal; they are not the goal itself. You can follow checklists, guidelines, and tips, and have terribly insecure software. You can also *disregard* some inappropriate ones and have very secure software. In short:

**_There is no substitute for thinking._**

This course will give you a number of tips to help you to reduce risks, focusing on lessons that previous developers have learned. But they are merely tips; they are merely an *aid* to developing secure software. When you are developing software, continuously think about the ways that an attacker might try to exploit your system. Anticipate the potential problems—while they are still risks—and mitigate them.