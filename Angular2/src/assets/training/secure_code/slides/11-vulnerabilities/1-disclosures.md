# 4. Other Topics

This chapter describes topics on the fundamentals of developing secure software that have not been covered elsewhere, including handling vulnerability disclosures, assurance cases, the basics after development, formal methods, and top vulnerability lists.

Learning objectives:

1. Understand how to properly handle vulnerability disclosures.

2. Discuss the basics of assurance cases.

3. Discuss the basics beyond development: distributing, fielding/deploying, operations, and disposal.

4. Get a brief introduction about formal methods.

5. Take a look at top vulnerability lists (e.g., OWASP Top 10 and CWE Top 25).

## Vulnerability Disclosures

### Receiving Vulnerability Reports

Unfortunately, even after your best efforts, someone may find a vulnerability in the software you have developed. In this unit, we will discuss receiving vulnerability reports, including how to prepare to receive vulnerability reports *before* vulnerabilities are found.

#### Product Security Incident Response Teams (PSIRTs)

If you are part of a team developing a large software application within a single organization, then you probably have or should consider forming a group to address security incidents related to that software. Such teams are sometimes called a Product Security Incident Response Team (PSIRT). The nonprofit Forum of Incident Response and Security Teams (FIRST) defines a PSIRT as *“an entity within an organization which... focuses on the identification, assessment and disposition of the risks associated with security vulnerabilities within the products, including offerings, solutions, components and/or services which an organization produces and/or sells”* ([FIRST](https://www.first.org/standards/frameworks/): *Product Security Incident Response Team (PSIRT) Services Framework* and *Computer Security Incident Response Team (CSIRT) Services Framework*). FIRST recommends that PSIRTs be formed while requirements are still being developed, but they should at least be formed before the initial release of the software. A properly-running PSIRT can identify and rapidly respond to an extremely serious vulnerability report.

PSIRTs often work with computer incident response teams (CSIRTs); a CSIRT is focused on the security of computer systems and/or networks that make up the infrastructure of an entire organization, while PSIRTs focus on specific products/services. Should you have one (or want to establish one), FIRST provides useful frameworks describing what PSIRTs and CSIRTs should do within an organization ([FIRST Services Framework](https://www.first.org/standards/frameworks/)).

Many governments and large companies also have their own requirements and guidelines for how to handle vulnerability reports. If your project is one of their efforts, you will need to follow those requirements and consider its guidelines.

A simple short guide is the [OWASP Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html). This short document provides useful guidance for both security researchers (who find security vulnerabilities) and organizations (who receive vulnerability reports).

There are many other useful documents that discuss vulnerability disclosure. In particular:

* [*The CERT Guide to Coordinated Vulnerability Disclosure*](https://vuls.cert.org/confluence/display/CVD/The+CERT+Guide+to+Coordinated+Vulnerability+Disclosure), by Allen Householder, 2019. In that document the “vendor” is the organization that releases the software and needs to learn about the security vulnerability.

* FIRST’s [*Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure*](https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1) [https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1](https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1)

There is an Open Source Security Foundation (OpenSSF) working group on vulnerability disclosures, which may in the future provide additional guidance. You can learn more about this working group here: [OpenSSF Vulnerability Disclosures Working Group](https://github.com/ossf/wg-vulnerability-disclosures).

In the rest of this unit we will discuss some of the key issues for accepting vulnerability reports.

#### Publicly State How to Send Vulnerability Reports

You must tell others, publicly, how to send vulnerability reports… and this information must be extremely easy to find. Otherwise, potential reporters will not report vulnerabilities to you, or there may be a significant delay while the project tries to figure out how to receive a report. This is time wasted where time is often of the essence. In 2019, failure to publicly state how to send vulnerability reports was the #1 most common reason OSS projects did not earn the OpenSSF Best Practices *passing* badge ([*Core Infrastructure Initiative (CII) Best Practices Badge in 2019*](https://events19.linuxfoundation.org/wp-content/uploads/2018/07/cii-bp-badge-2019-03.pdf), by David A. Wheeler).

In one sense this requirement is easy. Decide what your reporting convention is, and make that information easy to find. Here are some common conventions:

1. Many companies and projects support an email address of the form **security@example.com** or **abuse@example.com**.

2. A common convention in OSS projects is to provide this information in a file named **SECURITY.md** in the repository’s root or **docs/** directory. Sites such as GitHub will highlight this file if present and encourage their creation. Add a link from your **README.md** file to this **SECURITY.md** file.

3. If the project has or implements a website, a common recommendation is to add a **security.txt** file on the website at **/security.txt** or **/.well-known/security.txt**. To learn more, visit [securitytxt.org](https://securitytxt.org/).

One challenge is that attackers are also very interested in getting vulnerability reports, because they want to exploit those vulnerabilities until everyone installs its fixes or mitigations. So, it is usually important to have some mechanism for reporting vulnerabilities that prevents attackers from also getting this information before a patch is distributed. This can sometimes be hard to do:

1. Email systems are generally not end-to-end encrypted. Email systems that support end-to-end encryption (e.g., OpenPGP and S/MIME) are not widely used, may be hard to use, and/or are primarily used only within specific communities.

2. Many other communication systems for 1-on-1 secure communication expect that the parties already know each other, which is often not the case in vulnerability reporting.

3. OSS projects generally work in the open, so normal reporting and discussion forums (such as issue trackers, chat systems, etc.) may allow many people (or everyone) to see the discussion about a vulnerability, even if it is not supposed to be publicly known.

If you don’t want attackers to immediately exploit vulnerabilities reported to you, you should use some sort of encryption for the initial report. One imperfect but useful solution is to use email systems that support STARTTLS. Most large email providers (like GMail) and many companies support STARTTLS. STARTTLS provides *transport layer encryption*, that is, the emails are encrypted *between* email relays. Transport layer encryption is not as secure as end-to-end encryption, because the emails are decrypted at various points. In addition, STARTTLS is often deployed as *opportunistic TLS* - meaning an active attacker who controls certain network routers or email relays may be able to disable this encryption for a period of time. That said, using email providers who support STARTTLS transparently provides protection from many of the most common kinds of attacks on communication, while being very easy to use.

You should also use encryption to communicate among the key developers if you don’t want attackers to know about what is going on. However, the developers often know each other, so this is usually much easier to accomplish.

#### Monitor for Vulnerabilities, Including Vulnerable Dependencies

As we have already mentioned, monitor for vulnerabilities about your software and all libraries embedded in it. You can use Google alerts to alert you about your software from various news sources. Use a software composition analysis (SCA) / origin analysis tool to alert you about newly-found publicly-known vulnerabilities in your dependencies.

As noted earlier, a software bill of materials (SBOM) is a nested inventory that identifies the software components that make up a larger piece of software. When an SBOM is available for a component you are using, it’s often easier to use that data to help detect known vulnerabilities. Many ecosystems have ecosystem-specific SBOM formats. There are also some SBOM formats that support arbitrary ecosystems: [Software Package Data Exchange (SPDX)](https://spdx.dev/), [Software ID (SWID)](https://csrc.nist.gov/Projects/Software-Identification-SWID/), and [CycloneDX](https://github.com/CycloneDX/specification).

#### Consider Creating a Bug Bounty Program

A widely-used technique to encourage vulnerability reporting is a *bug bounty program*, where you pay reporters to report about especially important defects. This can be a cost-effective way to encourage people to report vulnerabilities to you once all relatively “easy-to-find” vulnerabilities have been found and fixed. If you don’t want to manage such a program yourself, there are various companies that can do that for you for a fee.

Be sure to clearly establish the scope and terms of any bug bounty programs ([OWASP Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)). Specify what you will pay for, including a minimum and maximum range. For example, *“$X-$Y for a vulnerability that directly leads to a remote code execution without requiring login credentials.”* If there is a maximum that you can spend in a year, say so, and indicate the total amount, the calendar used, and what will happen to reports after the annual funding is used up. Also make it clear who is ineligible, e.g., developers of the software and/or employees of companies that develop the software.

However, beware: a bug bounty program can be an incredible waste of money unless the easy to find vulnerabilities are found and fixed first. As Katie Moussouris has noted, *“Not all bugs are created equal"*; many defects (such as most XSS defects) are easy to detect and fix, and *“you should be finding those bugs easily yourselves too.”* Using a bug bounty program to find easy-to-find vulnerabilities is extremely costly and *“is not appropriate risk management.”* She even noted a case where a company ended up paying a security researcher $29,000/hour to find simple well-known defects. Find and fix the simple bugs first, and *then* a bug bounty program may make sense ([*Relying on bug bounties ‘not appropriate risk management’: Katie Moussouris*](https://www.zdnet.com/article/relying-on-bug-bounties-not-appropriate-risk-management-katie-moussouris/), by Stilgherrian, 2019).