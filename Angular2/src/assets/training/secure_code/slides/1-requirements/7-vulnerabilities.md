### Vulnerabilities

A vulnerability is simply a failure to meet some security requirement. Typically vulnerabilities are unintentional, but vulnerabilities can be intentional. For example, someone may have intentionally inserted malicious code (or at least attempted to do so) in the software you reuse or develop, such as a backdoor (a way to gain unauthorized access) or a logic bomb (code that performs a malicious function when specified conditions are met). This course focuses strictly on software, though of course hardware can also have vulnerabilities.

Modern society depends on software (and hardware), and as a result, there has been a massive growth in the number of publicly-known vulnerabilities. This has made it difficult to answer simple questions like, *“did you fix this particular vulnerability"*? Next, we will outline some efforts that have been made to identify and address known vulnerabilities.

#### Reporting and Handling Vulnerabilities - A Brief Summary

There are many people who have, for one reason or or another, found security vulnerabilities in software. Some people, called security researchers, make finding vulnerabilities part of their career.

In most cases, these vulnerability finders report the vulnerability to the software supplier(s) through a *“timed coordinated disclosure”* process. The finders privately report the vulnerability to the supplier(s), giving the supplier(s) some limited time (called the *“embargo time”*) to fix the vulnerability. After this embargo time (typically 14-90 days), or when the vulnerability has been fixed and users have had an opportunity to install the upgraded version of the software, the vulnerability is publicly disclosed. Sometimes this process is just called *“coordinated disclosure”*, but we want to make it unambiguously clear that in this process, the vulnerability will be publicly disclosed if the supplier fails to fix it in a timely manner.

In practice, things are more complicated. Often there are multiple suppliers and other stakeholders involved. It is critically important that you (as a developer/supplier) prepare ahead-of-time so that people can easily report vulnerabilities to you, so that you can privately discuss the issue with trusted parties, and so that you can rapidly fix any issues. Later in this course we will further discuss how to accept and report vulnerabilities, including references to useful documents about it. In addition, there is so much software and so many vulnerabilities that there is a need to track vulnerabilities. This need for tracking led to the creation of something called Common Vulnerabilities and Exposures (CVE).

#### CVEs

Common Vulnerabilities and Exposures (CVE) is a global dictionary of (some) publicly disclosed cybersecurity vulnerabilities. The goal of CVE is to make it easier to share data about vulnerabilities. A CVE entry has an identification number (ID), description, and at least one public reference. CVE IDs have the form CVE-*year*-*number*, where *year* is the year it was reported and *number* is an arbitrary positive integer to ensure that CVE IDs are unique. For example, [CVE-2014-0160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160) is a specific vulnerability in OpenSSL (called the Heartbleed  vulnerability) that was first reported in 2014. There are databases, such as the [US National Vulnerability Database (](https://nvd.nist.gov/)[NVD](https://nvd.nist.gov/)[)](https://nvd.nist.gov/), that track the current public set of CVE entries.

CVEs are assigned by a CVE Numbering Authority (CNA). A CNA is simply an organization authorized to assign CVE IDs to vulnerabilities affecting products within some scope defined in advance. The primary CNA (aka “CNA of last resort”) can assign a CVE even if no one else can (this role is currently filled by [MITRE](https://www.mitre.org/)). Many CNAs are software product developers (such as Microsoft and Red Hat) who assign CVE numbers for their own products. There are also third-party coordinators for vulnerabilities, such as the [CERT Coordination Center](https://sei.cmu.edu/about/divisions/cert/index.cfm), who are CNAs. Each CNA is given a block of integers that it can use in CVEs. This means that CVE-2025-50000 does not mean that it is vulnerability number 50,000 in the year 2025, but merely that the CNA who assigned that CVE ID was authorized to assign 50,000 in the year 2025.

Many publicly-known vulnerabilities do not have CVE assignments. First of all, CVEs are only assigned if someone requests an assignment from a CNA; if no request is made, there will be no CVE. In addition, CVEs are intentionally limited in scope. CVEs are only granted for software that has been publicly released (including pre-releases if they are widely used). CVEs are generally not assigned to custom-built software that is not distributed. They are also not normally assigned to online services. That said, CVEs are the most widely used method for giving a unique identifier for each publicly-known vulnerability, so it is important to know about them.

#### Top Kinds of Vulnerabilities

The vast majority of vulnerabilities can be grouped into categories. That turns out to be very useful; once we identify categories, we can determine which ones are common and what steps we can take to prevent those kinds of vulnerabilities from happening again.

The [Common Weaknesses Enumeration (CWE)](https://cwe.mitre.org/) is a very long list of common weaknesses. In their terminology, a “weakness” is a category (type) of vulnerability. Note the difference between CVE and CWE:  a CWE identifies a *type* of vulnerability, while a CVE identifies a *specific* vulnerability in a particular (family of) products. Each CWE has an identifier with a number, e.g., CWE-20. We will mention CWE from time to time. However, the CWE is a large list, and we cannot cover all CWEs in this course.

People have identified the most important or top kinds of vulnerabilities in terms of their likelihood and severity. Two of the most popular lists of top kinds of vulnerabilities are:

1. [**OWASP Top 10 Web Application Security Risks**](https://owasp.org/www-project-top-ten/)
This list, developed by the Open Web Application Security Project (OWASP), represents a *“broad consensus about the most critical security risks to web applications.”*

2. [**CWE Top 25 List**](https://cwe.mitre.org/top25/archive/2019/2019_cwe_top25.html)
This is a list of the most widespread and critical kinds of vulnerabilities. It was created by the Common Weaknesses Enumeration (CWE) Team by analyzing data about publicly-known vulnerabilities over many years. This list can be applied to any software, but it is especially common to apply it to software that is not a web application (since the OWASP list focuses on web applications). One interesting quirk: they identify important weaknesses beyond the first 25, so you can see numbers larger than 25 associated with this list.

OWASP has other top 10 lists for different kinds of software. For example:

* [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/) - the mobile applications top 10

* [OWASP Internet of Things Project](https://wiki.owasp.org/index.php/OWASP_Internet_of_Things_Project) - the Internet of Things (IoT) top 10. 

That said, the web application top 10 list is the best known top 10 list from OWASP.

These top vulnerabilities are not only common, but they tend to result in severe vulnerabilities.

 

These top lists do change over time. Unfortunately, they do not change very much. Many of the top vulnerabilities in the CWE Top 25 have been the same common kinds of vulnerabilities for decades (e.g., see *Computer Security Technology Planning Study*, [volume I](https://csrc.nist.gov/csrc/media/publications/conference-paper/1998/10/08/proceedings-of-the-21st-nissc-1998/documents/early-cs-papers/ande72a.pdf) and [volume II](https://apps.dtic.mil/dtic/tr/fulltext/u2/772806.pdf), by James P. Anderson, 1972), and most of the top web application problems have been common kinds of web application vulnerabilities since the 1990s. So while things do change, learning about the *top* kinds of vulnerabilities will be helpful to you for years to come.

In various places throughout the course you will see the alarm bell symbol 🔔. This symbol indicates that the vulnerabilities being discussed are so common that they are in the OWASP top 10 web application security risk list and/or the CWE top 25 list.

#### Value of Knowing Top Kinds of Vulnerabilities

We will spend a lot of time in this course reviewing common kinds of vulnerabilities. The risk of doing this is that you may think that is all there is to developing secure software. This is not true.

Avoiding common mistakes is **_not_** enough, by itself, to make software secure.

But depending on how you measure things, anywhere from 90% to 99% or more vulnerabilities are covered by these top lists. By preventing common mistakes, you will reduce the number of vulnerabilities by at least an order of magnitude! That makes knowing - and countering - common kinds of vulnerabilities very valuable, because it will make your software much more secure. Saying *never make a mistake* is impractical. In contrast, it is practical to focus on identifying and managing the most common kinds of mistakes that lead to vulnerabilities. Part of the reason that these vulnerabilities are common is that most developers do not know what they are; knowing what they are is the first step to managing them.

Identifying common kinds of vulnerabilities has another advantage, too: It will help you identify *other* kinds of vulnerabilities. As we have already noted, there is no substitute for thinking. But many developers find it challenging to view their systems like an attacker would. By looking at common kinds of vulnerabilities of the past, you can become more sensitive to vulnerabilities in general. So while knowing common kinds of vulnerabilities does not *replace* thinking, knowing them can *help* you think.