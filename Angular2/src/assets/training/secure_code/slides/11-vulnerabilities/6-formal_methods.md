### Formal Methods

Today most software needs to be developed to be “reasonably” or “adequately” secure. This course has focused on techniques to help you do that. However, if it is *extremely critical* that your software meet some criteria - such as some security criteria - there is an additional approach that you should be aware of: *formal methods*.

Formal methods are the use of *“mathematically rigorous techniques and tools for the specification, design and verification of software and hardware systems”*, where *“mathematically rigorous”* means that *“specifications are well-formed statements in a mathematical logic and that the formal verifications [if any] are rigorous deductions in that logic”* ([*What is Formal Methods?*](https://shemesh.larc.nasa.gov/fm/fm-what.html), by Ricky W. Butler). In short, formal methods apply mathematics to software.

The big advantages of formal methods are that:

* You can eliminate many sources of ambiguity.

* You can *prove* that certain things are true or false, given certain assumptions (and you can decide what the assumptions are).

The big disadvantages of formal methods are that:

* Using formal methods to develop software today often requires more effort.

* In many cases, using formal methods also requires specialized knowledge (e.g., of mathematics and/or of the formal methods tools being used).

Many people are working on developing and improving tools to overcome these disadvantages.

Formal methods *are* being used today to develop software, for example:

* Engineers at Amazon Web Services (AWS) use TLA+ to analyze services including its widely-used Simple Storage Service (S3) and DynamoDB (a NoSQL data store). For more details, see [*Use of Formal Methods at Amazon Web Services*](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf) (2014) and [*How Amazon Web Services Uses Formal Methods*](https://cacm.acm.org/magazines/2015/4/184701-how-amazon-web-services-uses-formal-methods/fulltext) (2015), by Chris Newcombe, Tim Rath, Fan Zhang, Bogdan Munteanu, Marc Brooker, and Michael Daerdeuff.

* The seL4 operating system kernel (an OSS kernel) has been proven correct.

* The s2n implementation of TLS/SSL has had formal verification of important aspects and also formally verified its implementation of the HMAC algorithm ([*Automated Reasoning and Amazon s2n*](https://aws.amazon.com/blogs/security/automated-reasoning-and-amazon-s2n/), by Colm MacCarthaigh, 2016).

* Many proposed cryptographic protocols are examined with model checkers for possible exploits, and some tools embed formal methods approaches to address certain kinds of problems ([*Dramatically Reducing Software Vulnerabilities: Report to the White House Office of Science and Technology Policy*](https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8151.pdf), by Paul E. Black, Lee Badger, Barbara Guttman and Elizabeth Fong, 2016).

* Hubert Garavel ([*Formal Methods for Safe and Secure Computers Systems*](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Studien/formal_methods_study_875/formal_methods_study_875.pdf?&#95;&#95;blob=publicationFile&v=1), 2013) provides a large list where formal methods have been used, as well as a broader survey on formal methods.

That said, using formal methods during software development is unusual today. But formal methods may become more common in the future, or you may be asked to develop software where the risk from a vulnerability is extremely high. So in this section we will provide some brief awareness about formal methods.

Before we do that, we need to make one thing clear: Formal methods always require assumptions. If the assumptions are false then their conclusions don’t necessarily hold. For example, you could prove that something is true if the CPU works correctly; a bug in the CPU means that the proof does not hold in that case. That does not make formal methods useless, because they can eliminate many other problems, and you can choose what to assume. But it is important to remember that when someone says “something is proven” that it is really proven given some assumptions… and it is important to understand what those assumptions are.

#### Formal Methods Levels

Because of the extra effort, formal methods are often applied to a subset of components or specific properties that are especially important. Formal methods can also be applied to various degrees. There is varying terminology on these degrees, but one way is these three levels:

* **Level 0**
A formal specification is created (that is, mathematically-based techniques are used to rigorously describe what the program is supposed to do). The program is then informally developed from it. This is sometimes called *formal methods lite*. This approach can help remove some ambiguities.

* **Level 1**
Apply level 0 and then prove some select properties from that or do a formal refinement from specification towards something that will become the program.

* **Level 2**
Fully prove the claims of a program, including mechanically checking it. This provides the strongest results, but also requires the most effort.

#### How Can Math Be Applied?

There are many different ways to apply mathematics, and so there are many different ways to use formal methods. Let’s briefly look at a few common math concepts that are used in formal methods.

##### Boolean Expressions

A widely-used tool is the idea of boolean expressions. These expressions are true or false, and can include various *propositional connectives* (a proposition is simply something that is either true or false). Here are common propositional connectives. The first three should be very familiar to you, since programming languages copied them from mathematics, but their traditional mathematical notation might be new to you:

1. “x and y” (mathematical “x ∧ y”) is true if both x and y are true, otherwise it is false.

2. “x or y” (mathematical “x ∨ y”) is true if either or both x and y are true; if both are false it is false.

3. “not x” (mathematical “￢x”) is true if x is false, and it is false if x is true.

4. “x→y” is true if x is false *or* if y is true, that is, x → y is the same as ((not x) or y). The arrow is often read as “implies”. This operator may be new to you, but this arrow simply represents “if x is true then y is true”. It is formally called *material implication*.

5. “x&harr;y” is true if x and y have the same value. This is basically “are these values equal” for boolean values. It is sometimes read as “if and only if” (iff).
