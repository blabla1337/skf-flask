### Countering ReDoS Attacks on Regular Expressions

When you add code, there is a risk that the added code has a vulnerability. This is especially true when you add code that is supposed to help keep your software secure, since by definition, problems in that code could lead to a security problem.

If you add input validation checks using regular expressions - a common and helpful approach - there is a kind of vulnerability you can unintentionally add called a *Regular expression Denial of Service (ReDoS)* vulnerability. If your software has a ReDoS vulnerability, attackers can force situations where the regular expression can be run for an extremely long time (possibly days or years). The result is a denial of service (DoS) - the attack may be able to send a small amount of data and cause the service to be unavailable! This is not theoretical. In 2020, the **websocket-extensions npm** package and its Ruby version were found to both have this flaw (these were given identifiers [CVE-2020-7662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7662) and [CVE-2020-7663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7663) respectively).

The reason that the ReDoS vulnerability is possible is that most regex implementations have a worst case complexity that grows exponentially based on the size of the input. A little background may help here. There are two main approaches to implementing regexes: a *deterministic finite automaton* (DFA) or *nondeterministic finite automaton* (NFA). DFAs are fast, in part because they never backtrack, and DFAs are immune to ReDoS vulnerabilities. But DFAs are also limited in what they can do. In practice, most regex implementations today are NFAs, and NFAs *are* potentially vulnerable to ReDoS attacks.

NFA implementations of regexes - and that is most of them - *backtrack* whenever they fail a specific match until they either find a match or have tried all possibilities. In short, in the worst case they try *all* combinations. For many regular expression patterns this worst case is not a problem. However, certain kinds of regex patterns can make this worst case really bad. In particular, let’s imagine that we provide a pattern where:

1. The regex pattern uses repetition on complex subexpressions (the use of “**+**” and “**&#42;**” on complex subexpressions), and

2. Within these repeated subexpressions, there are additional repetition symbols and expressions that match a suffix of another match. ([OWASP ReDoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service&#95;-&#95;ReDoS))

A trivial example is the regex pattern “**^(a+)+$**”. Let’s imagine that an attacker provided the input value ”**aaaaX**”. An NFA will match the input first letter “**a**” with the “a” in the pattern easily, but then the regex implementation has two options: should it try to apply the *inner* “**+**” or the *outer* “**+**” to the next letter? Most implementations would try the inner one first, and then backtrack as needed. In the worst case, an NFA has to try out *all* possible combinations. Thus, to determine if the input “**aaaaX**” matches the pattern, an NFA regex has to try out 16 possible paths (all possibilities), with each one eventually failing because of the trailing “**X**”. If the attacker provides the input “**aaaaaaaaaaaaaaaaX**” there would be 65536 possible paths, with the number of paths doubling for each additional “**a**”. If an attacker provided 80 ‘**a**’s followed by **X**, that thread will try to process all combinations, which would take so long that it would become a denial-of-service. 

We use the term *vulnerable regexes* for regex patterns with this awful worst-case behavior. A common industry term for these patterns is *evil regexes*. It is not that the regex is provided by an attacker necessarily, it is just that their worst-case behavior is “evil” and this makes them vulnerable to attack. Another term for this behavior is *catastrophic backtracking*.

There are many solutions to this problem, including the following:

1. Use a regex implementation that uses a DFA. DFA-based implementations are not vulnerable to this problem. For example, in the NPM ecosystem, “**re2**” implements a DFA regex engine. However, DFA-based regex engines are generally less capable and in many environments are much more trouble to install and use, so this is rarely done.

2. Modify the regex so that it doesn’t have this worst-case behavior. This is the usual approach. Be especially wary of any group “**(...)**” that contains a branch and/or ends with a repeat and is itself repeated.

1. If there is a repeat or branch in a regex that is itself repeated, rewrite the regex so the next character in the input would unambiguously determine if the repeat continues or not. E.g., rewrite “**^(a+)+$**” as “**^a+$**”.

2. Another approach is to use mechanisms that tell the regex engine not to backtrack; many regex implementations have *possessive quantifiers* and/or *atomic grouping* which can prevent unnecessary backtracking.

3. Avoid unbounded repetition. For example, define maximum repetition counts (e.g., **{0,5}**) so the worst-case behavior is greatly limited.

Some tools examine source code to detect regexes with worst-case behaviors (these may be standalone tools or part of bigger tools).

3. Where you can, limit the maximum length of input strings and check the input length first. If inputs must be short, the exponential growth in time will still end up as a small total amount of time.

4. Don’t run regexes provided by attackers on systems you trust. It is okay for an adversary to provide a regex that they themselves always run (in that case, attackers just attack themselves). But if attackers can provide regexes that you run, they may be able to cause a ReDOS (unless you have taken other steps to prevent it). Regexes are, in general, programming languages, and you should generally avoid running attacker-provided programs. It is possible to do it relatively securely, but you need to take a lot of precautions and it is always more secure to just not do it.

If you are interested in more details, see the [OWASP discussion](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service&#95;-&#95;ReDoS) about this.