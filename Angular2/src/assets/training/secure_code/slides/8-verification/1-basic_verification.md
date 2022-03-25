# 1. Verification

This chapter describes how to verify for security, including the limitations of tools, the meaning of *static analysis* and *dynamic analysis*, and common types of tools such as security code scanners/static application security testing (SAST) tools, fuzzers, and web application scanners.

Learning objectives:

1. Understand verification tools, including the issues of false positives and false negatives.

2. Discuss common types of static analysis tools, including security code scanners/static application security testing (SAST) tools.

3. Discuss common types of dynamic analysis tools, including fuzzers and web application scanners.

## Basics of Verification

### Verification Overview

Verification can be defined as determining whether or not something complies with its requirements (including regulations, specifications, and so on). Testing is one verification approach, but verification is more than testing. We want to verify (to some reasonable level) that our software is secure, just like we want to verify that our software does other things it is supposed to do.

#### Verification Approaches

There are two main technical categories of verification:

* **Static analysis** is any approach for verifying software (including finding defects) without executing software. This includes tools that examine source code looking for vulnerabilities (e.g., source code vulnerability scanning tools). It also includes humans reading code, looking for problems.

* **Dynamic analysis** is any approach for verifying software (including finding defects) by executing software on specific inputs and checking the results. Traditional testing is a kind of dynamic analysis. Fuzz testing, where you send many *random* inputs to a program to see if it does something it should not, is also an example of dynamic analysis.

Some people also have a category called *hybrid analysis* for approaches that combine both, while others will include hybrid approaches in the dynamic analysis category.

#### True and False Reports

There is a long history of using various kinds of detectors to detect important situations, many of which have nothing to do with software. Smoke detectors, for example, attempt to detect smoke from dangerous fires. Sadly, detectors are never perfect.

In security we often want to use tools that find and report certain kinds of vulnerabilities. Ideally, such a vulnerability detection tool would always report exactly the vulnerabilities you want it to report, and nothing else. Again, such ideals rarely occur in reality. So a tool may report something or not, and that report or non-report may be correct or incorrect, leading to 4 possibilities:

<table>
  <tr>
    <td><b>Analysis/tool report</b></td>
    <td><b>Report correct</b></td>
    <td><b>Report incorrect</b></td>
  </tr>
  <tr>
    <td><b>Reported</b> (a defect)</td>
    <td><i>True positive (TP)</i>: Correctly reported (a defect)</td>
    <td><i>False positive (FP)</i>: Incorrect report (of a “defect” that’s not a defect) (“Type I error”)</td>
  </tr>
  <tr>
    <td><b>Did not report</b> (a defect (there))</td>
    <td><i>True negative (TN)</i>: Correctly did not report (a given defect)</td>
    <td><i>False negative (FN)</i>: Incorrect because it failed to report (a defect) (“Type II error”)</td>
  </tr>
</table>


The reality is that there is usually a trade-off between false positives and false negatives. Tools can be designed or configured to have fewer false positives (incorrect reports), but that lack of sensitivity typically means that it will often have more false negatives (it will fail to report things that you might expect it to report). For more about details, see the [*SATE V Report: Ten Years of Static Analysis Tool Expositions*](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.500-326.pdf), 2018.

#### Applying Tools

If you are adding a tool to an existing project, you may want to configure tools to greatly limit what they report, and focus just on the vulnerabilities you are most concerned about. This gives you time to learn how to *tune* the tool and understand its results. Then, once those results are addressed, increase the sensitivity of your tools or add more tools to detect more issues. There is no point in trying to detect more issues than you can deal with.

If you are adding tools to a newly-started project, you are often better off configuring your tools to be very sensitive. In a new project, you will not be overwhelmed by the reports, and you will immediately get feedback on the issues your tools can detect.

Where do you add these tools? In short, maximally add these tools to at least your continuous integration (CI) pipeline. That way, incremental changes will be repeatedly analyzed and security issues will be reported early.

Some tools are OSS, while others are proprietary. Some of the proprietary tools are expensive, but if you are using them to develop OSS, many tools and/or services are free to use or are available at a substantial discount.

So let’s look at some kinds of tools you can use to help make your software secure.