# Secure Software Development Fundamentals

by David A. Wheeler

This is the content of a trio of self-paced courses. Users can learn from it for free, or apply for a certificate of completion for a fee.

To *take* the course, please go to the [OpenSSF web page on Secure Software Development Fundamentals courses](https://openssf.org/training/courses/).
You can also go to its
[edX page](https://www.edx.org/professional-certificate/linuxfoundationx-secure-software-development-fundamentals).
To get this content in Markdown format, go to <https://github.com/ossf/secure-sw-dev-fundamentals>.

This is split into 3 smaller courses (part 1-3):

1. Secure Software Development - Part I, Requirements, Design, and Reuse [Covers basics, requirements, design, reuse] - ~ 2-4 hours

2. Secure Software Development - Part II, Implementation - ~ 4-6 hours

3. Secure Software Development - Part III, Verification and More Specialized Topics [Covers verification, threat models, cryptography, & other advanced topics] - ~ 3-5 hours

These learning materials (including section quizzes) are released under the Creative Commons Attribution (CC-BY) license, specifically CC-BY-4.0. A few images (e.g., from XKCD) have different licenses and are noted as such. We do NOT release the chapter/final exams that way, as that would encourage cheating. If by some circumstance you end up with access to those exams,  DO NOT RELEASE them, please!

We can quickly fix significant mistakes, but we otherwise want to only implement updates every 1-1.5 years so its contents stay relatively stable. You can propose a change via [https://github.com/ossf/secure-sw-dev-fundamentals/issues](https://github.com/ossf/secure-sw-dev-fundamentals/issues). This course content was reconciled with the materials posted on edX as of 2020-12-03. LF Training & Certification has determined, from experience, that it’s safer & more reliable to write/edit content on some other platform and then convert it to edX (that is, instead of Don’t Repeat Yourself (DRY) it is safer to Write Everything Twice (WET)), so that is the process we’re using. The original document was developed using Google docs; other formats are translations, which may have translation errors.

The learning approach is designed to potentially support many users (with a potential of 10-15 million), so all problems (including knowledge checks) must be completely automated. There are no plans to use cohorts, discussions, or anything else requiring human instructors (because that doesn’t scale well). In most cases the knowledge checks are 1-2 multiple choice questions. They will generally have a random *order* of answers, but not Randomized *values* of answer (no Python script is involved).

Note that edX requires groupings at 3 levels: Sections, Subsections, and Units. Only Units (level 3) can have content.  We represent this in the material below as follows:  A “Heading 1” represents the beginning of a Section and contains ONLY sequences beginning with “Heading 2” (no text). A “Heading 2” represents the beginning of a Subsection and contains ONLY sequences beginning with “Heading 3”. A “Heading 3” represents the beginning of a Unit and contains all content. A Heading 3 cannot be directly contained within a Heading 1. Heading 4 (and below) are used freely within a Unit.

For more information about this material, see the folder here:

[https://drive.google.com/drive/folders/1AwqHfObQXxZrFSscXHBs8k5GSOCIKzxs](https://drive.google.com/drive/folders/1AwqHfObQXxZrFSscXHBs8k5GSOCIKzxs)

**About this course (Part 1)**

Modern software is under constant attack, but many software developers have never been told how to effectively counter those attacks. This course works to solve that problem, by explaining the fundamentals of developing secure software. Geared towards software developers, DevOps professionals, software engineers, web application developers, and others interested in learning how to develop secure software, this course focuses on practical steps that can be taken, even with limited resources, to improve information security. This course will enable software developers to create and maintain systems that are much harder to successfully attack, reduce the damage when attacks are successful, and speed the response so that any latent vulnerabilities can be rapidly repaired.

This course discusses the basics of security, such as what risk management really means. It discusses how to consider security as part of the requirements of a system, and what potential security requirements you might consider. This part then discusses how to design software to be secure, including various secure design principles that will help you avoid bad designs and embrace good ones. It also discusses how to secure your software supply chain, that is, how to more securely select and acquire reused software (including open source software) to enhance security.

This is the first of the three courses in the Secure Software Development Fundamentals Professional Certificate program, and was developed by the Open Source Security Foundation (OpenSSF), a project of the Linux Foundation focused on securing the open source ecosystem. The training courses included in this program focus on practical steps that you (as a developer) can take to counter most common kinds of attacks.

**What you'll learn (Part 1)**

- Security basics: risk management, the “CIA” triad, and requirements.
- Secure design principles: what are principles such as “least privilege” and how to apply these principles.
- Supply chain evaluation: tips on how to choose packages to reuse, and how to reuse them so that you can rapidly be alerted & update.


**About this course (Part 2)**

Modern software is under constant attack, but many software developers have never been told how to effectively counter those attacks. This course works to solve that problem, by explaining the fundamentals of developing secure software. Geared towards software developers, DevOps professionals, software engineers, web application developers, and others interested in learning how to develop secure software, this course focuses on practical steps that can be taken, even with limited resources to improve information security. This course will enable software developers to create and maintain systems that are much harder to successfully attack, reduce the damage when attacks are successful, and speed the response so that any latent vulnerabilities can be rapidly repaired.

This course focuses on key implementation issues: input validation (such as why allowlists should be used and not denylists), processing data securely, calling out to other programs, sending output, and error handling. It focuses on practical steps that you (as a developer) can take to counter the most common kinds of attacks.

This is the second of the three courses in the Secure Software Development Fundamentals Professional Certificate program, and was developed by the Open Source Security Foundation (OpenSSF), a project of the Linux Foundation focused on securing the open source ecosystem.

**What you'll learn (Part 2)**


- Implementation: You’ll learn how to implement much more secure software. This includes how to do Input validation, process data securely, call out to other programs, and send output. You’ll also learn about more specialized approaches, including some basics of cryptography and handling problems (such as error-handling code).


**About this course (Part 3)**

Modern software is under constant attack, but many software developers have never been told how to effectively counter those attacks. This course works to solve that problem, by explaining the fundamentals of developing secure software. Geared towards software developers, DevOps professionals, software engineers, web application developers, and others interested in learning how to develop secure software, this course focuses on practical steps that can be taken, even with limited resources to improve information security. This course will enable software developers to create and maintain systems that are much harder to successfully attack, reduce the damage when attacks are successful, and speed the response so that any latent vulnerabilities can be rapidly repaired.

This course discusses how to verify software for security. In particular, it discusses the various static and dynamic analyses approaches, as well as how to apply them (e.g., in a continuous integration pipeline). It also discusses more specialized topics, such as the basics of how to develop a threat model and how to apply various cryptographic capabilities.

This is the third of the three courses in the Secure Software Development Fundamentals Professional Certificate program, and was developed by the Open Source Security Foundation (OpenSSF), a project of the Linux Foundation focused on securing the open source ecosystem. The training courses included in this program focus on practical steps that you (as a developer) can take to counter most common kinds of attacks.

**What you'll learn (Part 3)**

- Security Verification: How to examine software, include some key tool types, and how to apply them in continuous integration (CI). This includes learning about security code scanners/static application security testing (SAST) tools, software composition analysis (SCA)/dependency analysis tools, fuzzers, and web application scanners.
- Threat modeling/Attack modeling: How to consider your system from an attacker’s point of view and how to apply a simple design analysis approach called STRIDE.
- Fielding: How to deploy and operate secure software, handle vulnerability reports, and how to rapidly update when reused components have publicly-known vulnerabilities.
- Assurance cases & formal methods: The basics of approaches to more strongly analyze and justify that your software is secure.


**Meet your instructor**

David A. Wheeler
Director of Open Source Supply Chain Security at The Linux Foundation
Dr. David A. Wheeler is an expert in developing secure software and in open source software (OSS). He is the Director of Open Source Supply Chain Security at the Linux Foundation and teaches graduate courses in developing secure software at George Mason University (GMU) in Fairfax, VA. He has a PhD in Information Technology, a Master's in Computer Science, a certificate in Information Security, a certificate in software engineering, and a B.S. in Electronics Engineering. He is also a Certified Information Systems Security Professional (CISSP) and an IEEE Senior member. He leads the Open Source Security Foundation (OpenSSF) Best Practices Badge project for the Linux Foundation and has served as a lead validator for National Information Assurance Partnership (NIAP) for the (security) Common Criteria. He lives in Northern Virginia.
