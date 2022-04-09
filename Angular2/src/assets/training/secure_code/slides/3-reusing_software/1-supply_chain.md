# 3. Reusing External Software

This chapter describes how to reuse software with security in mind, including selecting, downloading, installing, and updating such software.

Learning objectives:

1. Discuss the vital impact external software has on security.

2. Discuss how to consider security when selecting software.

3. Discuss how to consider security when downloading and installing software.

4. Discuss the importance of updating reused software.

5. Discuss the importance of avoiding/replacing the use of obsolete interfaces.

## Supply Chain

### Basics of Reusing Software

When developing software, you normally reuse lots of other software. This may include an operating system, container runtime, frameworks, and libraries. You will typically also use development tools that others have developed. This reused software, and how you get it, can significantly impact the security of the result.

![Dependency](../../dependency.png)

*Dependency* (retrieved from [xkcd.com](https://xkcd.com/2347/), provided under [CC-BY-NC-2.5](https://creativecommons.org/licenses/by-nc/2.5/))

Some consider the selection of reused software as part of design, since it clearly impacts how we divide up the problem. Others might describe this as its own category, e.g., supply chain. No matter what you call it, it is important. In general, software systems today are mostly reused software from somewhere else.

If you are purchasing expensive software you selected on behalf of an organization, there are often many steps and processes to work through, primarily focused on controlling money. That is outside the scope of this course. Instead, we are going to focus on the specific aspects related to security.

We’ll use the term “reused software” here, because that is our concern. This reused software includes all the software you depend on when the software runs, aka its dependencies. In practice, the vast majority of the software you reuse will be open source software (OSS), so we will especially focus on tips when reusing OSS.

### Selecting Reusable Software

There are many important things to consider when selecting reusable software. For security here are a few things to consider:

1. Is it *easy to use securely*? If something is hard to use *securely* the result is far more likely to be insecure.

1. Look at the defaults of its interface and configuration. Is its API secure by default, or are “simple examples” using the defaults also insecure?

2. If it has a discussion about how to use it securely, that is generally a good sign, especially if it is clear that its warnings recommend that you keep its defaults.

This is a reason to avoid using C and C++ to implement new software when there is no significant reason to use them; C and C++ have many insecure defaults (as we will discuss later).

2. Is there evidence that its developers *work to make it secure*?

1. If it is OSS, has the project earned an Open Source Security Foundation (OpenSSF) Best Practices badge (or at least are they well on their way to that)? An OSS project that has earned an OpenSSF Best Practices badge implements a number of best practices for sustainably developing secure software. We will discuss this in more detail later in the section on verification. You can learn more about the [OpenSSF Best Practices badge](https://bestpractices.coreinfrastructure.org/en) online.

2. Is there evidence that the developers use tools to detect defects and vulnerabilities as early as possible?

3. Is there documentation explaining why its developers believe it is secure (aka an “assurance case”)?

4. Is there evidence of a security audit, and that any problems found were fixed? Security audits are relatively uncommon, but they are a great sign when they exist. An audit that finds a large number of vulnerabilities could have found them because the software is just full of vulnerabilities, or because the audit was thorough, but no matter what, if the problems were found and fixed, those problems no longer exist in the version you plan to use.

5. Consider using [SAFECode’s guide ](https://safecode.org/principles-of-software-assurance-assessment/)[*Principles for Software Assurance Assessment*](https://safecode.org/principles-of-software-assurance-assessment/) (2019), which has a multi-tiered approach for examining the security characteristics of software.

This entire course discusses how to develop secure software; the more of these actions you see in the software you are considering, the better!

3. Is it *maintained*? Unmaintained software is a risk. If the software is not maintained, it is more likely to have serious unaddressed security vulnerabilities, and it is more likely that its developers will fail to quickly fix vulnerabilities when they are reported. In theory, software can be “completed” and not need future changes, but usually software that is not being changed is not being maintained.

1. If the software is OSS, you can generally look at its repository and see its commit history. If it continues to have active commits, especially by multiple people, that is a good sign. An OSS component with no changes in the last year is generally much riskier.

2. Are there recent releases or announcements from its developer?

4. Does it have *significant use*? Just because there are many users, or a large company (like Google or Facebook) uses it, does not mean it is appropriate for you. If you only choose the latest fad, you will sometimes make horrific mistakes! However, knowing that software is widely used can be useful information. If software has many users or large (corporate) users, then there’s more likely to be useful information on how to use it securely, and more people who will care about its security. Also, if it has a small number of users, see if something else with a similar name is more popular - that could indicate a typosquatting attack. We will discuss typosquatting in the next unit.

5. What is the software’s *license*? Licenses are technically not security, but licenses can have a big impact on security.

1. Some software is released without a license at all; this can be legally dangerous, especially if it is more than a line or two of code, because in most countries and situations the law does not permit its use. Sometimes this can be fixed by contacting the original developer and proposing a license. A developer who puts users at legal risk is probably not worried about preventing security risks either.

2. If the software has a license, make sure that its license is consistent with what you are trying to do. **Beware**: the costs of failing to abide by a license can be extremely steep. Be especially careful if the software is not released with an OSS license, since by definition you will have fewer rights, and in practice there will only be one supplier who will decide what information you can have and how it will change. Make sure you follow the license requirements. If you won’t follow the license requirements, you are not only at legal risk for using it, but you will generally not have the right to use its security updates either.

6. If it is important, what is *your own evaluation* of it? If the software is important to you, and especially if it is OSS, you can download and examine it yourself. Some people are scared of doing this, but there is no reason to be afraid. Even a brief review of software source code, and its changes over time, can give you some insight into the software you are thinking about using. This can be time-consuming, so many will not do this. But if the software you are developing is very important, this is a step worth seriously considering. Doing a thorough evaluation of such software is outside the scope of this course. There are many organizations with expertise in doing code-level security audits for a fee; you may want to engage their services if you want an in-depth review. However, if you decide that you want to do just a brief review, here are things to consider:

1. When you review the more detailed artifacts (e.g., the source code), is there evidence that the developers were trying to develop secure software (such as rigorous input validation of untrusted input and the use of prepared statements)?

2. Is there evidence of insecure or woefully incomplete software (such as a forest of TODO statements)?

3. What are the “top” problems reported when running it through static analysis tools (that examine the code to look for problems)?

4. Is there evidence that the software is malicious? The authors of [*Backstabber’s Knife Collection: A Review of Open Source Software Supply Chain Attacks*](https://arxiv.org/abs/2005.09535) (2020) article notes traits that are especially common in malicious packages: most malicious packages perform malicious actions during installation (so check the installation routines), most aim at data exfiltration (so check for extraction and sending of data like **~/.ssh** or environment variables), and about half use some sort of obfuscation (so look for encoded values that end up being executed). You could also run the software in a sandbox with an environment intended to trigger likely issues, and see if the software attempts to do something malicious. Some malicious software detects that it is being examined and behaves well when examined, so running code in a sandbox does not guarantee detection… but it may reduce risk.

Most software depends on other software, which in turn often depends on other software with many tiers. A software bill of materials (SBOM) is a nested inventory that identifies the software components that make up a larger piece of software. Many ecosystems have ecosystem-specific SBOM formats. There are also some SBOM formats that support arbitrary ecosystems: [Software Package Data Exchange (SPDX)](https://spdx.dev/), [Software ID (SWID)](https://csrc.nist.gov/Projects/Software-Identification-SWID/), and [CycloneDX](https://github.com/CycloneDX/specification). When an SBOM is available for a component you are thinking about using, it’s often easier to use that data to help answer some of the questions listed above. It’s also good to provide an SBOM to potential users of your software, for the same reasons.