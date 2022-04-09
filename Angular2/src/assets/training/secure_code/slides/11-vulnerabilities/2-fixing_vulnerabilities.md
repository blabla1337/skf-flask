### Respond To and Fix the Vulnerability in a Timely Way

Of course, once a vulnerability report is received, it must be responded to and fixed in a timely way. OWASP recommends the following ([OWASP Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)):

* Respond to reports in a reasonable timeline.

* Communicate openly with researchers.

* [Do] not threaten legal action against researchers.

You need to be able to quickly triage vulnerability reports; some reports won’t apply to your software or are not really vulnerabilities. It is quite common to need to ask further questions to really understand the vulnerability.

#### Fixing the Vulnerability

Once you have determined that it really is a vulnerability, you will need to fix it.

If you want to be able to discuss reports in a constrained group - and most groups do - you should set that up ahead of time.

Ensure that you can quickly stand up a working test environment for any supported version and environment of the software. So make sure you have good version control of the source code, and also ensure that you can quickly stand up the development and test environments.

When fixing a security vulnerability, check to see if the same kind of vulnerability exists in similar situations in the software. Otherwise, you will end up creating many more patches.

If your update causes problems, people will reject it and learn to not accept any future updates from you. Any proposed fix must avoid backwards incompatibilities if at all possible. It must also be of high quality. This implies that you need to have a strong *automated* test suite before you release the software, and have any needed hardware to execute it (if the tests need special hardware). Add automated tests related to what you are changing, both to ensure that it really fixes the problem and also to verify that the change does not negatively affect anything else.

![image alt text](../../worst.png)

**Worst Thing That Could Happen**, retrieved from [xkcd.com](https://xkcd.com/2261/), licensed under [CC-BY-NC-2.5](https://creativecommons.org/licenses/by-nc/2.5/) 

#### Limiting Disclosure and the FIRST Traffic Light Protocol (TLP)

When discussing a vulnerability, it is often important to discuss detailed information, yet simultaneously tell people to limit disclosure of some information for a period of time. In addition, it has become common for there to be multiple different parties involved in a vulnerability: there may be multiple suppliers (including vendors) who implement software with the vulnerability, distributors, and organizations involved in distributing information about the vulnerability.

FIRST developed a simple marking system for this called the [Traffic Light Protocol](https://www.first.org/tlp/) (TLP) that is often used to indicate to whom the information can be shared. Here is a brief summary. The TLP has four color values to indicate sharing boundaries, which are placed as follows:

1. In email: the TLP color is in the subject line and also in the body before the designated information.

2. In documents: the TLP color is in the header and footer of each page, typically right-justified.

The TLP color is shown in all-caps after “**TLP:**”, so you will see **TLP:RED**, **TLP:AMBER**, **TLP:GREEN**, or **TLP:WHITE**. These colors have the following meaning:

* **TLP:RED** = Not for disclosure, restricted to participants only.

* **TLP:AMBER** = Limited disclosure, restricted to participants’ organizations.

* **TLP:GREEN** = Limited disclosure, restricted to the community.

* **TLP:WHITE**  = Disclosure is not limited.

 

#### Get a CVE and Compute CVSS

You should request a CVE where appropriate and it has not already been requested ([OWASP Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)). Typically, you would start this process once you have verified that the report really is a vulnerability, and thus you would do it simultaneously with fixing it. If you request a CVE, you should also calculate the vulnerability’s Common Vulnerability Scoring System (CVSS) score. CVSS is a rough estimate of a vulnerability’s severity.

The reason for CVEs and CVSS is simple: organizations are overwhelmed with software updates, and they need information to help them prioritize updates. CVE and CVSS are not perfect, but they are widely used and depended on. The Ponemon Institute’s [*Costs and Consequences of Gaps in Vulnerability Responses*](https://www.servicenow.com/lpayr/ponemon-vulnerability-survey.html) (2019) survey found that:

* *“Almost half of respondents (48%) report that their organizations had one or more data breaches in the past two years.”*

* *“60% of breach victims said they were breached due to [a] known vulnerability where the patch was not applied”*

* *“CVSS scoring… is often the only metric of patch prioritization [even though it] leaves out asset criticality and systems as part of vulnerability response.”*

* *“44% of respondents say their organizations use automation to assist with vulnerability management and patching [(primarily prioritization and patching)]”*

* *“Automation reduces the time to respond to vulnerabilities… 80% of organizations… that use automation say they have the ability to respond to vulnerabilities in a shorter timeframe.”* However, this automation depends on a variety of factors, including (in most cases) having a CVE assigned when there is a vulnerability.

CVSS is widely used, because there is a need for clear prioritization, but CVSS is also widely criticized (for example, [*Broken vulnerabilities severities*](https://opensourcesecurity.io/2020/05/27/broken-vulnerability-severities/), by Josh Bressers, 2020). A new version of CVSS (beyond version 3), or a replacement for it, may be developed and/or become widely used in the future.

#### Release the Update and Tell the World

Once the fix is ready, release it. You will need to tell the world the software is fixed, and do all you can to encourage rapid uptake of the fixed version. OWASP recommends that suppliers publish clear security advisories and changelogs, and also that suppliers offer credit to the vulnerability finder ([OWASP Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)).

If there are workarounds that can be applied without updating the software, be sure to note those. This is particularly important if:

* there are likely to be many users who cannot update their software, or 

* the vulnerability is publicly known, but the patch will not be released for some time.

Ensure that it is easy to automatically update to the fixed version of the software. If your software platform does not provide automated patch releases or installation, consider implementing one yourself. Users need to be able to quickly and automatically receive fixes, unless they have expressly opted out of updates.

Be sure to always credit and thank vulnerability reporters, unless they request otherwise. It is rude to not provide credit, and many vulnerability reporters provide reports *primarily* to get credit. What is worse, reporters may be less cooperative in the future if they do not receive appropriate credit.