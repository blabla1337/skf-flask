# OWASP Dependency track
-------

## Example:

        Zest is an experimental specialized scripting language (also known as a domain-specific language) 
        developed by the Mozilla security team and is intended to be used in web oriented security tools.

        It is included by default with ZAP.

        ZEST can be used to record and replay attacks to your applications in
        a running state to identify the existence of attacks.

        When security teams find vulnerabilities they typically describe them to developers using words, for example in a PDF or via a bug tracker. Unfortunately in many cases developers may lack the security knowledge to understand or reproduce the problem. Also security teams often use tools which the developers do not have access to or have no experience with. And developers sometime fail to solve the underlying problems.

        While it will still be necessary to describe vulnerabilities, Zest allows security teams to create reproducible test cases which they can then share with the developers. These test cases can be used by the developers to reproduce the issues and test their fixes.

        Ideally security engineers will be able to use their favourite security tools to create Zest scripts while developers will be able to rerun those scripts using the tools that they are familiar with.

        In this case the sequence of events could be:

        1. The security team discovers a vulnerability using specialist security tools
        2. They use those tools to create a Zest script which reproduces the problem
        3. They hand the script over to the developer
        4. The developer adjusts the script to match their local environment
        5. They run the script and see the vulnerability
        6. They fix the vulnerability
        7. They rerun the script to check that the vulnerability is fixed
        8. The fix is applied to the system that the security team is testing
        9. The security team rerun the script as an initial check
        10. They then perform any manual testing they think is necessary
        11. Note that the developers could also include the script in the regression tests to make sure that it doesnt reoccur.

        [ZEST main site](https://www.zaproxy.org/docs/desktop/addons/zest/)
        [ZEST more info](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Zest)