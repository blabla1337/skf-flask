### Web Application Scanners

[Web application]

Today many people develop web applications, and web applications have many standard interfaces. As a result, there are programs designed specifically to dynamically analyze web applications to look for vulnerabilities.

A web application scanner (WAS), also called a web application vulnerability scanner, essentially pretends it is a simulated user or web browser and tries to do many things to detect problems. Think of a WAS as a frenetic and malicious web browser user; the WAS will try to click on every button it finds, enter bizarre text into every text field it finds, and so on. In short, it attempts simulated attacks and odd behavior to try to detect problems. This means that WASs often build on fuzzers internally, but they are specifically designed to analyze web applications.

A key issue in a WAS is what input vectors it can test. Some WASs can only create new URLs and cannot test client-side JavaScript applications. Such programs are not as useful for testing programs with client-side JavaScript.

WASs also differ in how they detect problems with the results. Unsurprisingly, crashing a web application would be reported as a problem. WASs also tend to have a variety of *passive* checks (e.g., to check the attributes of cookies returned) to attempt to detect a variety of problems.

Like many other tools, WASs operate heuristically and generally have a variety of rules. As a result, different WASs may detect (and not detect) different things.

You will want to use a WAS in a test environment, not a true production environment, since it will *intentionally* attempt to cause problems. You may want to start with just running the WAS as-is, but you will soon want to create a bogus account and give the WAS the bogus account information. Otherwise, if your login system is built correctly, the WAS will only be able to test for vulnerabilities for someone without valid login credentials.

There are many of these tools. OSS tools include OWASP ZAP, W3AF, IronWASP, Skipfish, and Wapiti. Proprietary tools include IBM AppScan, HP WebInspect, and Burp Suite Pro. If you have no idea, you might check out OWASP ZAP at least; it is easy to use, and it can find many things. But tools change over time, and it is best to look at your options before picking one (or several).

If you are developing a web application, then it is a good idea to use at least one web application scanner. These tools will not find all possible problems, and like fuzzers, they tend to find fewer problems over time. But they can still be useful.

The term Dynamic Application Security Testing, or DAST, is often seen in literature. However, the *meaning* of DAST has a lot of variation:

* For some, DAST is dynamic analysis for finding vulnerabilities in web applications (see VeraCode, [*DAST TEST: Benefits of a DAST test for application security*](https://www.veracode.com/security/dast-test), 2020), making the term mostly equivalent to *web application scanners*. John Breeden II ([*9 top fuzzing tools: Finding the weirdest application errors*](https://www.csoonline.com/article/3487708/9-top-fuzzing-tools-finding-the-weirdest-application-errors.html), 2019) states this and expressly differentiates DAST from fuzzing.

* Thomas Scanlon ([*10 Types of Application Security Testing Tools: When and How to Use Them*](https://insights.sei.cmu.edu/sei_blog/2018/07/10-types-of-application-security-testing-tools-when-and-how-to-use-them.html), 2018) defines DAST as tools for finding security vulnerabilities where *“the tester has no prior knowledge of the system”* and that *“DAST tools employ fuzzing”*. With this definition, web application scanners and fuzzers are DAST tools. Similarly, Sergej Dechand ([*What is FAST?*](https://blog.code-intelligence.com/what-is-fast), 2020) includes web application scanners and fuzzers under “DAST”.

In this course we have intentionally used more specific terms instead of DAST, in the hopes of making things clearer. The point, regardless of the terminology, is to use approaches (including tools) to find and fix vulnerabilities before the attackers exploit them.