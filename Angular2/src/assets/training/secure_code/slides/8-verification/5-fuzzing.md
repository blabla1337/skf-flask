### Fuzz Testing

Fuzz testing is a different kind of dynamic analysis.

#### Fuzzing vs. Traditional Testing

In fuzz testing, you generate a large number of *random* inputs, run the program, and see if the program behaves badly (e.g., crashes or hangs). A key aspect of fuzzing is that it does *not* generally check if the program produces the correct answer; it just checks that certain reasonable behavior (like “does not crash”) occurs.

It’s often a lot of work to create traditional tests, in part because you have to know what the correct result will be. Fuzzing gives that up, making it easier to send more inputs automatically to a program but giving up the ability to detect certain kinds of errors. As computers have gotten faster and cheaper, fuzzing has become very useful, because it is possible to run many computers for a long period of time to try out many inputs. Fuzzing can be particularly effective at detecting memory safety errors (which are both common and dangerous) and at creating odd inputs that stress the input validators. Fuzzing does not replace traditional testing, but it can be an excellent complement to traditional testing.

There are many fuzzers, and a lot of research has focused on improving them. Historically fuzzers applied truly random input. Today many fuzzers use heuristics, protocol models, and/or other information to generate the input of the software under test (SUT) aka the target of evaluation (TOE) aka the target. Some fuzzers have also increased the ways that they can detect a problem, not just by detecting a crash. These changes increase the likelihood of finding a defect (including a vulnerability).

#### Using Fuzzers Effectively

Fuzzers can be really useful for finding vulnerabilities. If you use one, it is often wise to add and enable program assertions. This turns internal state problems - which might not be detected by the fuzzer - into a crash, which a fuzzer can easily detect. If you are running a C/C++ program, you should consider running a fuzzer in combination with address sanitizer (ASAN) - ASAN will turn some memory access problems that would normally quietly occur into a crash, and again, this transformation improves the fuzzer’s ability to detect problems. 

Both the Firefox and Chromium web browsers use fuzzers, combined with ASAN, to try to detect vulnerabilities before releasing new versions.

If your program performs checks on input like examining checksums or CRC (Cyclic Redundancy Check) headers, you will probably soon need to disable those checks or specially re-implement those values when using a fuzzer. By all means use the fuzzer on the program unmodified first, but the problem is that the fuzzer will end up primarily testing the checksum/CRC header checking code again and again, not the rest of the code. Some fuzzers are tailored to create well-formatted inputs that will pass checks such as CRC and then attempt to find errors deeper in the program under test.

Many fuzzers are *mutation-based* - that is, they begin with a starting set of sample inputs (called “seeds”), and then repeatedly mutate previous inputs to create new test inputs. The effectiveness of mutation-based fuzzers greatly depends on the seeds chosen. A useful rule-of-thumb for creating seeds is to try to select a minimum set of inputs necessary to cover (or almost cover) the code (that is, to achieve 100% statement coverage). To learn more, see [*Optimizing Seed Selection for Fuzzing*](https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-rebert.pdf), 2014. If that is too many seeds, select seeds to cover as much of the code as possible with that number of seeds (so each seed will be significantly different).

#### Coverage-Guided Fuzzers

An important subclass of fuzzer is a *coverage-guided fuzzer*. These fuzzers instrument the software under test (SUT, the program being tested) so that the fuzzer gets information about what code is covered when each input is executed (including, in many cases, how often various parts of the code are executed). This information is then used to determine the next inputs to be generated. The tool American Fuzzy Lop (AFL) demonstrated the power of this technique; it uses not just which parts of the code are executed, but how many times, and prefers to generate new inputs similar to previous inputs that caused novel counts. Other tools such as libFuzzer also use this approach. These fuzzers are also called *feedback-based fuzzers* or a *feedback-based application security testing* (FAST) tool ([*What is FAST?*](https://blog.code-intelligence.com/what-is-fast), by Sergej Dechand, 2020). This approach combines static and dynamic analysis, so these tools could be considered hybrid analysis tools.

#### Diminishing Rate of Return

A challenge with fuzzers is that over time they generally have a diminishing rate of return. That is, they are often successful in finding vulnerabilities in programs that have never been fuzzed before, but it can quickly take exponential time (or never) to find the next vulnerability once the previously-detected problems have been fixed. It can also require resources; fuzzing may take days, weeks, or even longer of continuous execution on a number of parallel systems before fuzzing can find something. That does not mean fuzzers are useless - they can be very useful - but again, they are only part of a tool suite to make software secure.

#### Fuzzing Projects

If you manage an OSS project, you might consider participating in [Google’s OSS-Fuzz project](https://github.com/google/oss-fuzz). OSS-Fuzz applies fuzzing in combination with various sanitizers to try to detect vulnerabilities. [The Fuzzing Project](https://fuzzing-project.org/) encourages/coordinates applying fuzz testing to OSS.

#### Fuzzing and Web Application Scanners

There are a huge number of fuzzers, and things are changing all the time. The first step is to know that there is a tool that might be useful. However, if what you have developed is a web application, there is a tool specifically designed for that situation that typically embeds a fuzzer within it, called a *web application scanner*. We will discuss that in the next unit.