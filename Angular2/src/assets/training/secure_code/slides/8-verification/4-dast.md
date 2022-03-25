## Dynamic Analysis

### Dynamic Analysis Overview

Dynamic analysis is any approach for verifying software (including finding defects) by executing software on specific inputs and checking the results. We will look at a few kinds of tools that do this, but first, let’s discuss their limitations.

#### Limitations to Dynamic Analysis

All dynamic analysis tools have a fundamental limitation: it is impossible to evaluate all possible inputs in a reasonable amount of time. It is not even possible to evaluate a *reasonable subset*.

Let’s imagine a trivial program that adds two 64-bit integers. The number of possible inputs is (2^64)\*(2^64) = 2^128. If we ran tests with a 4GHZ processor, and could run and test each input in 5 cycles, it would take 13.5 x 10^21 years (13.5 zetta years) to fully test the program. Using 1 million 8-core processors does not help enough; that would reduce the time to 1.7 x 10^15 years (that is, 1.7 quadrillion years). Real programs have far more complex inputs than this, so testing even 0.00001% of all inputs of real programs is impossible in human lifetimes.

As a result, all dynamic analysis approaches must try to select a very small subset of possible inputs that still have a chance of detecting problems where they exist. They are often very effective. But dynamic analysis approaches cannot “prove” that anything works correctly in general; at best, they have a good chance of detecting problems.

#### Traditional Testing

The best-known dynamic analysis approach is traditional testing. You select specific inputs to send to a program, and check to see if the result is correct. You can test specific parts of a program, such as a method or function (this is called *unit testing*). You can also send sequences of inputs to the system integrated as a whole (*integration testing*). Most people combine unit and integration testing. Unit testing is fast and it can be easy to test many special cases, but unit testing often misses whole-system problems that integration testing is much more likely to detect. Since computers are much faster than they were decades ago, it is often best to focus on integration testing over unit testing, but both approaches have their place. The testing literature describes other kinds of testing, but for our purposes, these two approaches are enough to understand the issues.

If your software needs to work correctly, it is critically important that you have a good test suite of *automated* tests and apply that test suite in your continuous integration pipeline. By *good* we mean “relatively likely to detect serious problems in the software”. While this does not guarantee there are no errors, a good test suite greatly increases the probability of detection, and is especially important for detecting problems when you upgrade a reused component.

If you deliver software, and a defect is later found and fixed, for each fix you should think about adding another test for that situation. Often, defects that escape to the field indicate a kind of subtle mistake that might reoccur in a future version of the system. In that case, add test(s) so if that problem recurs, will be detected *before* releasing another version.

If you are contracting someone else to write (some of) your software, and you don’t want to be controlled by them later, you need to make sure that you not only get the application source code (and the rights to modify it further), but also get all the build instructions and tests necessary to be able to confidently change the software. After all, if you cannot easily build or test a software modification, there is no safe way to make modifications and ship it.

In theory, you can create manual tests, that is, write a detailed step-by-step manual procedure and have a human follow those test steps. In practice, manual tests are almost always “tests that won’t be done” because of their high costs and delay. Another problem with manual testing is that it *discourages* continuous testing, since it costs time and money to do those manual tests. So avoid manual testing in favor of automated testing where practical. In some cases you may need to do manual testing, but remember that every manual test is a test that will rarely (if ever) be done, making that test far less useful. Note that what we are describing as *manual tests* are different from *undirected manual analysis* (where humans use the software *without* a step-by-step process). Undirected manual analysis can be quite effective, but is completely different from manual tests as we have defined them here.

A tricky problem in testing is when a resource is not available. If the test requires some software, hardware, or data that you don’t have, you cannot directly test it. Typically, the best you can do in those cases is simulate it (e.g., with mocked software, simulated hardware, or a stand-in dataset). If that is the best you can do, it is usually worthwhile. But don’t confuse the simulation with reality; the test results may be misleading due to differences between the actual resource and its stand-in.

#### Traditional Testing for Security

From a security perspective, it is important to include tests for security requirements. In particular, test both “what should happen” and “what should not happen”. Often people forget to test *what should not happen* (aka negative testing). For example, where it applies, you should have a test to check “Can I read/write *without* being authorized to do so?” (the answer should be “no”) and “Can I access the system with an *invalid* certificate or no certificate at all?” (again, that should fail). It is very common for programs’ security to fail because they don’t properly check for authentication (2017 OWASP Top 10 #2) or authorization (2017 OWASP Top 10 #5), so make sure you have tests for that!

One approach to developing software is called t*est-driven development* (TDD). To over-summarize, in TDD the tests for a new capability are written before the software to implement the capability. This has some advantages, in particular, it encourages writing useful tests that actually check what they are supposed to check, and it also encourages developing testable software. One potential problem with TDD is that many TDD practitioners fail to write *negative* tests. Some TDD guidance even argues that you should only write tests for the new capability and nothing else. This is terrible guidance, because sometimes some things should simply *never* be allowed to happen, and you still need to test for them. You can definitely write secure software using TDD, but you must include negative tests (tests for what the software must *not* do) if you apply TDD.

#### Test Coverage

You can *always* write another test; how do you know when you have written enough tests? It takes time to create and maintain tests, and tests should only be added if they add value. This turns out to be a hard question, and much depends on how critical your software is.

Two simple measurements that can help you answer this question are *statement coverage* and *branch coverage*:

1. Statement coverage is the percent of program statements that have been run by at least one test.

2. Branch coverage is the percentage of branches that have been taken by at least one test. In an **if-then-else** construct, the **then** part is one branch and the **else** part is the other branch. In a loop, the *run the body* part is one branch and *do not run the body* is the other branch. In a switch (case) statement, each possibility is a branch.

Statement coverage and branch coverage combine dynamic analysis (test results) with static analysis (information about the code), so it is sometimes considered a *hybrid* approach. But no matter what you call it, these measurements do provide some information about how well a program is tested.

One potential problem with statement coverage and branch coverage is that some statements and branches may be unreachable for a variety of reasons. If a statement cannot be reached, you may want to insert the equivalent of “**assert(false)**” to inform tools and humans that this statement should never be reached. What you really want to know is the percent of *possible* branches and statements that were covered by tests.

As a rule of thumb, we believe that an automated test suite with less than 90% statement coverage or less than 80% branch coverage (over all automated tests) is a poor test suite. But this is merely a rule of thumb. Some experts think that larger numbers should be expected (some argue anything less than 100% of possible statements and branches is unacceptable). All other things being equal, larger numbers are good, but it is often much costlier to get those last few percent, and whether or not it is worth it depends on how important the software is. In many cases some statements or branches cannot be executed, and there may not be a way to indicate that to the measurement tools.

These test coverage measures warn you about statements and branches that are not being tested, and that information can be really valuable. From a security standpoint, coverage measures warn you about statements or branches that are not being run in tests, which suggests that either there are some important tests missing or the software is not working properly. Don’t just add a test; make sure you understand *why* something is not being covered.

For example, we earlier mentioned a dangerous vulnerability in many versions of Apple’s operating systems, formally named CVE-2014-1266 and informally called the “goto fail; goto fail;” vulnerability. The problem was that due to a duplicated **goto** statement, some code vital for checking security certificates was skipped. A statement coverage measure would have trivially detected that this security-critical code was not being run by any test, and that should have been enough warning to look into the problem.

A big problem with statement and branch coverage measures is that they can warn you about some bad automated test suites, but a bad test suite could still get 100% perfect scores. For example, a test suite might exercise all the branches and statements but not check if any of the answers were correct. That test suite would have 100% branch and statement coverage, and would also be a bad test suite. In addition, while they can tell you about whether or not existing code was tested, they cannot detect *missing* code. For example, if there is a special case that needs special handling, but nothing checks for that special case, typically these coverage measures cannot detect that.

In short: these coverage measures can be useful for warning about some problems, but they do not warn about all testing problems.

But there is more to dynamic analysis when you are interested in security. Let’s next look at fuzz testing.