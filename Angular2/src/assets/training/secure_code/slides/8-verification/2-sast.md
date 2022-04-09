## Static Analysis

### Static Analysis Overview

Static analysis is any approach for verifying software (including finding defects) without executing software. This includes humans who review code. It also includes tools that review source code, byte code, and/or machine code.

#### Human Review

Humans can be amazing at finding defects. This is one of the big potential advantages of open source software (OSS); since anyone can review OSS source code to find defects, there is a potential mass peer review. But humans have their downsides. Human time is expensive, humans get bored, and humans have “off” days where they are less effective (e.g., they might miss things). Different humans have different levels of effectiveness, too. It’s great to have humans review code, but you also want to support humans with tools that will find problems the humans may miss.

If you can get humans to review code, do so! But you may want to direct the humans to examine issues that tools are especially not good at. In particular, it is good to have people review the “entry points” (attack surface) across a trust boundary to ensure that every request is either authorized or rejected. Determining whether or not a request is authorized is not something most tools are good at (they lack the information to make the decision). What is more, if that analysis is too hard for humans, there is something wrong with the software - it should be relatively *easy* to answer that question on each entry point. It is also a common problem; as we noted earlier, *Broken Access Control* is 2017 OWASP Top 10 #2.

In general, if there are problems that tools are not good at finding, it may be best to modify your design so the problem cannot happen in the first place. For example, choose a memory-safe language or design a system component so only safe requests can be made. If that does not work, it may be wise to try to find or develop a tool to find it. That said, there will always be issues that tools will not work well for. If nothing else works, then work to focus the most powerful tool of all on the problem: people. But people’s time is limited, so where you can, try to not depend *solely* on human review.

So with that said, let’s start discussing tools to help us.

#### Generic Bug-Finding Tools: Quality Tools, Compiler Warnings, and Type-Checking Tools

Some tools examine source code, byte code, or machine code to look for generic “quality” problems. For example, they may look for misleading indentation, combinations of constructs that usually indicate a defect, or overly-long methods that may be hard to understand later. There are a large variety of these, including compiler warning flags, style checkers, and so on. The tools themselves are often cheap or free, and they often run quickly, because they typically don’t need to do a deep analysis.

These tools often don’t focus on security, but using them can still help improve security:

1. Some defects they find are security vulnerabilities.

2. There are reports that *clean* code is easier for other tools and humans to understand… so fixing the reported problems can make other approaches more effective.

If you are starting a new project, it is important to turn on as many of these tools (including compiler warnings) as soon as you can. If you turn them on early, you will see a few reports recommending a different approach and just use that instead. If you try to add them to an *existing* project, you will often see far too many issues to fix, even though the odds of any one being a serious problem is small. So if you have an existing project, you typically need to add these tools slowly, configuring them to only report a subset (such as only reports triggered by a change) and then slowly expanding what they report.

Similar comments apply to static type-checking. Some programming languages have built-in checks for statically-declared types. There are pros and cons to statically-declared types. It takes time to determine and specify types, so doing that can slow down initial development, which is a negative for small and throw-away programs. However, those static declarations can help automatically finding certain kinds of defects, as well as aid support tools and optimization. If you are using a programming language with static type-checking, work with the type system to use it to help find defects early.

That said, while these tools are often easy to use, they generally are not focused on security issues… and thus they often miss security issues. Let’s talk about tools that use static analysis specifically to find security vulnerabilities.

#### Security Code Scanners/Static Application Security Testing (SAST) Tools

Some tools analyze code specifically looking for vulnerabilities. They go by a variety of names, such as Static Application Security Testing (SAST) tools, security code scanners, security source code scanners (if they examine source code), binary code scanners (if they only examine executables), or just *static code analyzers*. Some people use the term SAST only when the tool analyzes source code (for more details, see [*The AppSec alphabet soup: A guide to SAST, IAST, DAST, and RASP*](https://www.synopsys.com/blogs/software-security/sast-iast-dast-rasp-differences/) by Fred Bals, 2018, and [*10 Types of Application Security Testing Tools: When and How to Use Them*](https://insights.sei.cmu.edu/sei_blog/2018/07/10-types-of-application-security-testing-tools-when-and-how-to-use-them.html) by Thomas Scanlon, 2018), but we will not limit the term that way.

The idea behind these tools is that many vulnerabilities have specific patterns. A tool designed to look for those patterns can report similar kinds of vulnerabilities.

The patterns are generally heuristic, and different tools generally look for different patterns. So one tool can find *some* vulnerabilities, but don’t make the mistake of thinking that any one of these tools finds *all* vulnerabilities. In addition, each tool will only look for patterns relevant to a particular set of languages/environments. That means these tools are only good for languages/environments they are designed to support, and in addition, a tool might be better at one language than another. Even given multiple tools designed to support a given language, different tools will often find vulnerabilities that others miss.

If your primary goal is to find as many vulnerabilities as possible, it is best to use multiple tools, even multiple tools of the same kind, so that a vulnerability not detected by one tool might be detected by another. Unfortunately, using multiple tools can get expensive in money and effort. Some tools are expensive, and no matter what, it takes time to configure the tool for its particular use and to analyze its reports. As often happens, there is a trade-off; the set of tools you select will be strongly influenced by the resources available, as well as the expected likelihood and impact of unfound vulnerabilities.

Of course, not everything reported by any of these tools is an *actual* vulnerability. All of these tools have some risk of generating a false positive. For example, a tool might detect a vulnerability triggered by some input, but you may know that only a trusted user can control that input… so while the tool is correct in one sense, it is not actually a vulnerability. In many cases, it is best to fix the report anyway; people are often wrong when they say something “can’t” happen, and the software or its environment may change in the future (so fixing it will future-proof the software). If you are confident the report is a false positive, and “fixing” the code to eliminate the report is not worth the trouble, most such tools have a way to disable the report (e.g., via a comment in the source code). That way, the tool will stop reporting about it; otherwise the tool reports will over time only have a large set of false positives. Just make sure that you only disable a report if you are *certain* it is a false positive.

#### Specialized Security Code Scanners/SAST Tools

Some tools are designed to only look for one or a very few specific kinds of vulnerabilities. These are still security code scanners, aka SAST tools, but since they are specially written to perform that one specific analysis, they can sometimes be better at that one analysis than a more general-purpose tool designed to find many different kinds of vulnerabilities. In addition, some more general-purpose tools don’t look for these specific problems at all.

Here are some kinds of vulnerabilities that specialized SAST tools can detect:

* Regular Expression Denial-of-Service (ReDoS) vulnerabilities (that is, regular expressions with terrible worst-case performance). You can look for terms like “ReDoS”, “evil regex”, and “safe regex”. These extract the regular expressions from source code, and then analyze the regular expressions.

* Hardcoded credentials such as cryptographic keys and passwords.

#### Other Static Analysis Tools

There are many other kinds of static analysis tools.

One kind is so important that we will dedicate a whole separate section to it. The kind of analysis these tools do has a variety of names, including software composition analysis (SCA), dependency analysis, and origin analysis. No matter what it is called, it is important, so we will discuss that next.