### Development Processes / Defense-in-Breadth

There is no single magic mechanism to make secure software. Instead, you have to continuously consider security throughout software development and deployment. Considering security at all times, through all development and deployment processes, is sometimes called “defense in breadth”. So let’s talk about the processes used for software development and deployment.

#### Individual Software Development & Deployment Processes

Whenever you develop software there are certain processes that all developers have to do. These include:

* Determine *requirements* (what the software must do). For security, make sure you know what security requirements it needs to provide. For example, is there data it should keep confidential?

* Determine *architectural design* (how to divide up the problem into interacting components to solve it). Later in this course we will discuss various secure design principles to help you design a system that is easier to secure.

* *Select reusable components* (decide what reusable packages/libraries you will use). You need to evaluate the components you will use, since any of their vulnerabilities may become vulnerabilities of the software you are developing. These reused components come from somewhere, and depend transitively on other components. The set of all those dependencies, including where they come from and how they eventually get to you, is your *supply chain*.

* *Implement* it (write the code). Most security vulnerabilities made during implementation are specific common kinds; once you know what they are, you can avoid them.

* *Verify* it (write/implement tests and use analyzers to gain confidence that it does what it is supposed to). You should be testing to make sure that your system is secure, and using tools to help you find vulnerabilities before attackers find them.

* *Deploy* it. You should help ensure that users can get the correct version, that it is secure by default, and that they can easily operate it in a secure way.

#### Using These Processes Together

Of course, you need to use these processes together.

A common mistake is to try to execute these software development processes in a strict sequence (figure out all the requirements, then work out the entire design, then implement the entire system, then verify it). Attempting to create software in this strict sequence is called the *waterfall* model. The waterfall model is beguiling because doing these processes in strict sequence *appears* rigorous and sensible at first. In 1970, Winston W. Royce explained in his essay [*Managing the Development of Large Systems: Concepts and Techniques*](https://dl.acm.org/doi/10.5555/41765.41801) why trying to follow these processes in a strict sequence (a “waterfall”) is extremely risky in most circumstances and should normally be avoided.

Another common mistake is to implement software components independently and never integrate and test them together until everything is completed independently. This is typically a mistake, because this leads to serious problems getting the components to work together.

In practice, most software development executes these processes in parallel, bouncing information between the processes as new information is learned. There are many ways to combine processes, which depend on many factors such as the size of the team and how reliable the result needs to be. There are many different kinds of approaches, including the many different Agile, incremental, evolutionary, and waterfall development approaches. For purposes of this course, we will focus on security aspects whenever you choose to apply some process, and not much on these specifics. So you can apply this course’s materials regardless of the approach you use. However, let’s look at a few specific practices and terms that can be important for security.

A highly recommended practice is to use Continuous Integration (CI), the practice of frequently merging working copies of development into a shared mainline (e.g., once every few days through many times a day). This routine merging reduces the risks of components not working together if integration was delayed until later, and that is a good thing. However, successful CI requires a way to determine if the components are actually working together. This is resolved by using a CI pipeline—a process that runs whenever something is merged to ensure that it builds and passes a set of automated tests and other checks.

Many organizations want to deploy software/services more rapidly, and have adopted various approaches to do that building on these standard software development processes. Definitions vary, but here are some common terms:

* Continuous Delivery (CDE) aims to ensure *“an application is always at production-ready state after successfully passing automated tests and quality checks [by employing practices] to deliver software automatically to a production-like environment”* (Mojtaba Shahin, Muhammad Ali Babar, and Liming Zhu, [*Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices*](https://arxiv.org/abs/1703.07019), 2017). Note that the software is not actually released/deployed without a separate manual approval step.

* Continuous Deployment (CD) *“goes a step further [than continuous delivery] and automatically and continuously deploys the application to production or customer environments”* (Mojtaba Shahin, Muhammad Ali Babar, and Liming Zhu, [*Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices*](https://arxiv.org/abs/1703.07019), 2017).

* DevOps focuses on coordination and cooperation between the software development (Dev) and IT operations (Ops) teams (Mike Loukides, [*Revisiting “What Is DevOps”*](http://radar.oreilly.com/2014/06/revisiting-what-is-devops.html), 2014), e.g., to shorten development and deployment time. In practice, this typically includes Continuous Delivery (CDE) and may include Continuous Deployment (CD).

* DevSecOps (also called SecDevOps) is DevOps, but specifically integrating security concerns into the development and operations process (Red Hat, [*What Is DevSecOps?*](https://www.redhat.com/en/topics/devops/what-is-devsecops))

All these depend on automated tests and quality checks, and from a security perspective, what is critical is that tools to check for security vulnerabilities and potential security issues need to be integrated into those automated tests and quality checks. For example, you should ensure that tools are in your CI pipeline that check for various security issues, so that any security problems are detected early. Security tools that take a long time to run might be run in parallel but be used as a “gate” for CDE. We will discuss much more about tools to support security later in the course.

Simply inserting some “security tools” into an automated test suite, by itself, tends to be ineffective. Security tools will not generally know what the software is supposed to do (the requirements). For example, security tools will not know what information is confidential. Security tools usually cannot detect fundamental problems in the software design, and even if they could, fixing design problems is not what detection tools do.  Security tools often miss vulnerabilities, especially if the software is poorly designed. And perhaps most importantly, information from security tools generally do not make sense to developers if they do not have a basic understanding about security. There is an old phrase that is still true: *“a fool with a tool is still a fool”*.

**In short:** Tools are important, but not enough. You must continuously consider security throughout development and deployment, no matter what you are doing, so you can identify and handle security-related risks. Consider how your system might be attacked (identifying its risks), analyze risks to determine how likely the system could be exploited and the severity if it was, and then decide what to do. That definitely includes adding security tools in your continuous integration pipeline, but those tools will be far more effective if you think about security throughout development and deployment. In the rest of this course we will cover how to do that. We will eventually discuss tools, but only after we understand what the tools are helping us do.

You also should focus on continuous improvement, of both the software itself and the processes you use to develop it. If the current design or API is hard to use securely, make it easy to use securely. Look for ways to harden the software against attacks. Modify the verification processes by adding new tools, or changing the configuration of existing tools, to increasingly detect problems before they are released to users.