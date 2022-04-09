# Course Introduction

## Introduction

*Learn the security basics that allow you to develop software that is hardened against attacks, and understand how you can reduce the damage and speed the response when a vulnerability is exploited.*

Modern software is under constant attack, but many software developers have never been told how to effectively counter those attacks. This course works to solve that problem, by explaining the fundamentals of developing secure software. Geared towards software developers, DevOps professionals, software engineers, web application developers, and others interested in learning how to develop secure software, this course focuses on practical steps that can be taken, even with limited resources, to improve information security. This course will enable software developers to create and maintain systems that are much harder to successfully attack, reduce the damage when attacks are successful, and speed the response so that any latent vulnerabilities can be rapidly repaired.

The course discusses risks and requirements, design principles, and evaluating code (such as packages) for reuse. It then focuses on key implementation issues: input validation (such as why allowlists and not denylists should be used), processing data securely, calling out to other programs, sending output, cryptography, error handling, and incident response. This is followed by a discussion on various kinds of verification issues, including tests, including security testing and penetration testing, and security tools. It ends with a discussion on deployment and handling vulnerability reports. 

The *Secure Software Development Fundamentals* course was developed by the Open Source Security Foundation (OpenSSF), a project of the Linux Foundation focused on securing the open source ecosystem. The course focuses on practical steps that you (as a developer) can take to counter most common kinds of attacks.

## A Note from the Author

Our thanks to the many people who provided helpful commentary and advice. We especially thank Paul E. Black (NIST), Steve Lipner (SAFECode), Dan Lorenc (Google), Sherif Mansour (OWASP), and Yannick Moy (AdaCore) for their thoughtful and specific recommendations.

## Motivation

### Motivation: Why Is It Important to Secure Software?

Every day there is news about computer systems being broken into, often via various vulnerabilities in the software. Insecure software may:

* Release private/secret information (aka *“lose confidentiality”*)

* Lose or corrupt information (aka “*lose integrity*”)

* Lose service (aka *“lose availability”*).

But the problems don’t end there. Any of these can cause *real world* losses. They can cost money, time, trust, and even lives.

Yet developers are often never told how to develop secure software. We should *expect* that developers who are never told how to do something will have a hard time doing it.

This course focuses on helping you understand how to practically develop secure software. By *secure software* we mean software:

* that is much harder for attackers to exploit,

* that limits damage if an exploitation is successful, and

* where vulnerabilities can be fixed and exploitations partially recovered from relatively quickly.

### Motivation: Why Take This course?

Our primary concern is that you learn how to develop *secure* software. Here are some of the features and advantages of this specific course:

1. **Quizzes**. We ask quiz questions along the way to help reinforce concepts. It is easy to disengage with traditional books and videos, thinking that you understand the core concepts even when you don’t. In contrast, the quizzes help reinforce the core concepts so you will understand them.

2. **Free**. If you just want to learn, it doesn’t cost anything! All you need is an internet connection. Many people have limited resources and we want to make sure this information is available to them.

3. **Open Content**. The main informational material is not just “free” in the sense of “no cost” but also in terms of freedom. In particular, the informational content is released under the [Creative Commons Attribution License (CC-BY) version 4.0](https://creativecommons.org/licenses/by/4.0/), so you can reuse it in many ways. We *want* you to use this information! There are some exceptions: we quote other material (such as from xkcd) which are under their own licenses, and to counter cheating we do not release the graded tests used in the edX version of this course this way.

4. **Certificate of Completion (for learners enrolled in a Verified track in the edX version)**. If you want to prove that you took the course (as opposed to simply learning it), that is available at a nominal price. This might really help you communicate what you know to employers, customers, or potential employers. By comparison, just owning a book doesn’t prove that you have read or understood it.

5. **Accessibility**. We have worked to make this information accessible. We want to make sure that those who are blind, have low vision, color-blindness, and so on can learn from this material.

6. **Applicable to Open Source Software (OSS)**. Many materials on security don’t spend significant time on OSS, or are difficult to apply when developing OSS. Yet OSS is key to modern software development. We include information specifically for those developing and/or using open source software (OSS).

7. **Independent of organization size**. We don’t require that you be in a large or small software development organization. Some courses implicitly assume you are in a large software development organization.

8. **Independent of programming language**. Most software developers use multiple programming languages or will switch through their career. With that in mind, this course provides a basic grounding in developing secure software that applies to *many* programming languages. We will use examples from specific programming languages, but we want you to have a firm foundation no matter what you use—now or in the future. You should supplement this information with materials for the specific language or framework you use, but this course will give you the key building blocks to understand and apply those other materials.

9. **Practical**. This course focuses on *practical* advice for the people developing software. In particular, we recommend specific things to do or avoid, etc. It briefly discusses why this advice applies, but this is not a graduate course; we focus more on *what* to actually do instead of all the theory or technical details behind it.

There are other materials that can provide information about software security. Here are a few worthy alternatives and a contrast to them:

1. The [*Security Engineering*](https://www.cl.cam.ac.uk/~rja14/book.html) book by Ross Anderson focuses on systems as a whole, including hardware and business processes, and focuses on big-picture concerns. However, this book does not cover most of the specifics of how to implement secure software. In contrast, this course (unlike Ross Anderson’s book) takes care to identify and discuss how to counter the most common kinds of security vulnerabilities.

2. [SAFECode training materials](https://safecode.org/training/). SAFECode has a number of training materials available. Some materials are quite good and are videos (while this course is mostly text). Note that many of their materials are often narrowly focused. For example, their course *“Cross Site Scripting (XSS) 101”* is on a single common kind of vulnerability, and *“Secure Java Programming 101”* only applies to one language. Check the dates, as some materials may be out of date. That said, if their materials match what you want, you should definitely check them out, as they are definitely worthy alternatives.

3. [OWASP Security Knowledge Framework (OWASP-SKF)](https://www.securityknowledgeframework.org/). “OWASP-SKF is an open source web application that explains secure coding principles in multiple programming languages. The goal of OWASP-SKF is to help you learn and integrate security by design in your software development and build applications that are secure by design. OWASP-SKF does this through manageable software development projects with checklists (using [OWASP-ASVS](https://owasp.org/www-project-application-security-verification-standard/)/[OWASP-MASVS](https://owasp.org/www-project-mobile-security-testing-guide/)  or custom security checklists) and labs to practice security verification (using SKF-Labs, [OWASP Juice-shop](https://owasp.org/www-project-juice-shop/), and best practice code examples from SKF and the [OWASP-Cheatsheets](https://cheatsheetseries.owasp.org)).” In contrast, this course (unlike OWASP-SKF) doesn’t require software development projects and labs.

Obviously, choose the material that will provide you with the information you want to learn, and you can certainly use them all if you wish.

With that, let’s begin.