## Other Verification Topics

### Combining Verification Approaches

There are many other kinds of verification approaches, and many ways to combine them.

A *penetration test* (aka *pen test*) simulates an attack on a system to try to break into (*penetrate*) the system. The people doing a penetration test are called penetration testers or a red team; they may be actively countered by a defensive team (also called a blue team). The point of a penetration test is to learn about weaknesses so they can be strengthened *before* a real attacker tries to attack the system.

A *security audit* reviews a system to look for vulnerabilities. Often the phrase is used implying a more methodical approach, where designs and code are reviewed to look for problems. But that is not always true; the terms *security audit* and *penetration test* are sometimes used synonymously. Regardless of this, security audits and penetration tests often employ a variety of techniques, including both static and dynamic analysis, to try to find vulnerabilities before real attackers can find and exploit them.

The Open Source Security Foundation (OpenSSF) Best Practices badge identifies a set of best practices for open source software (OSS) projects. There are three badge levels: passing, silver, and gold. Each level requires meeting the previous level; gold is especially difficult and *requires* multiple developers. Within each level are a set of criteria that are considered best practices for developing secure and sustainable OSS, and each criterion has a short identifier. Here are some examples of its criteria:

* “*The project MUST **use at least one automated test suite that is publicly released as FLOSS** (this test suite may be maintained as a separate FLOSS project).”* [test] Note that this criterion is solely about a traditional automated test suite (e.g., for its functionality).

* *“At least one static code analysis tool MUST be applied to any proposed major production release of the software before its release, if there is at least one FLOSS tool that implements this criterion in the selected language.”* [static_analysis]

* *“The project sites (website, repository, and download URLs) MUST support HTTPS using TLS.”* [sites_https]

If you are using OSS, consider preferring OSS who have earned a badge. If you are developing OSS, you should strongly consider working to earn an Open Source Security Foundation (OpenSSF) Best Practices badge. By implementing these best practices you will increase the likelihood of developing higher-quality and more secure software. To learn more and get started, check out the [OpenSSF Best Practices Badge Program](https://bestpractices.coreinfrastructure.org/en).