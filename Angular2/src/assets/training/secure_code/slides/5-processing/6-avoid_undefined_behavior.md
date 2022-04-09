### Avoid Undefined Behavior

[Memory-unsafe code]

Many programming languages are defined in some sort of formal specification. When that is the case, where practical, you should try to write code that conforms to those specifications, because your code is more likely to work in all cases, and as the language implementations change, your code is more likely to keep working.

Sometimes these specifications will permit one of several different options (this is sometimes called “unspecified behavior” or “compiler-specific behavior”). You should normally try to write your code so that it does not matter which permitted option is used, it will just keep working. Languages that support threading allow the threads to execute in parallel and in arbitrary order. In many languages, the order of operations in a call such as **f(aa, bb, cc)** is not defined (that is, it does not guarantee that **aa** or **cc** is computed first). Beware of depending on what your tools currently do, because when the tools are upgraded what they do may change. For many developers, dealing with this is already second nature.

However, some languages (such as C and C++) have constructs with truly *undefined behavior*. That is, if you take certain actions, the specification guarantees *absolutely nothing*. For example, the [C FAQ](http://c-faq.com/ansi/undef.html) notes that with undefined behavior, *“Anything at all can happen; the Standard imposes no requirements. The program may fail to compile, or it may execute incorrectly (either crashing or silently generating incorrect results), or it may fortuitously do exactly what the programmer intended.”* 

Any undefined behavior can be - and often is - a security vulnerability. Even if it just happens to not be a security vulnerability today, a minor upgrade in your tools, operating system, or configuration might turn it into a vulnerability.

Many languages have at least some undefined behaviors, and so, if you use those languages, you need to learn what they are and avoid them. C and C++ have an especially large number of undefined behaviors. For example, for C, there are hundreds of undefined behaviors; the list is 11 pages long in the publicly available final draft of [C18 annex J.2](https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf). It is also very easy in C and C++ to accidentally write code that has undefined behavior.  We have already seen some examples of undefined behavior: reads and writes out of the bounds of a buffer, use-after-free, and double-frees. Here are a few more.

In C and C++, a null pointer dereference is also undefined (e.g., evaluating “**&#42;p**” when **p** is **NULL**). This means that an attempt to dereference a null pointer does not necessarily lead to trying to read an invalid value, the program might do *anything* at all.

*Null Pointer Dereference* ([CWE-476](https://cwe.mitre.org/data/definitions/476.html)) is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #14. 

In C  and C++, signed integer overflow is undefined (e.g., an **int** with value **MAX_INT** with 1 added to it). There is no guarantee that signed integers wrap; instead, the program might do anything at all.

Integer overflow or wraparound is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #8. It is [CWE-190](https://cwe.mitre.org/data/definitions/190.html), *Integer overflow or wraparound* (though this CWE also covers unsigned wraparound, which is defined in C and C++).

Perhaps by now it is clear why many people recommend avoiding C and C++ if the code has to be secure. For a variety of reasons, it is more difficult to write secure software in these languages! But again, there are *reasons* that people choose these languages, and of course, if something is already written in these languages, it is hard to change.

So, if you do use C and C++, there are ways you can reduce your risks. We have already discussed some options. Here are a few more:

* Read its standards carefully so that you know all common undefined behaviors and actively avoid them when writing code.

* Turn on warnings about undefined behaviors. Examples of such gcc and/or clang flags include **-fsanitize=signed-overflow** (warn about signed overflow), **-ftrapv** (traps signed integer overflows), **-fsanitize=address**, **-fsanitize=undefined**, and **-fcatch-undefined-behavior** (but it will not ALWAYS detect them!)

* Force the compiler to assign a meaning to officially undefined behaviors. You should not rely on these, but they will reduce the impact of making a mistake. Examples of such gcc and/or clang flags include **-fwrapv** (wrap integers on overflow), **-fno-delete-null-pointer-checks**, and **-fno-strict-overflow**.

We will later discuss using tools to try to detect these, but be warned: most tools at best detect *some* undefined behaviors, not all of them. Your best defense is to use a language with no or few undefined behaviors. Where that is not reasonable, know exactly what is not defined, and carefully write code so it does not depend on undefined behaviors.