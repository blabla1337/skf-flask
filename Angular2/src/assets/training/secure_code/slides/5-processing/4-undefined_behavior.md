## Processing Data Securely: Undefined Behavior / Memory Safety

### Countering Out-of-Bounds Reads and Writes (Buffer Overflow)

[Memory-unsafe code]

#### Memory Safety

Unfortunately, handling untrusted data can be *especially* hard in some programming languages or when certain programming language modes are enabled. Most programming languages automatically prevent any attempt to read or write memory areas that are not allocated. These are called *memory safe languages*. However, memory safety mechanisms generally have a performance overhead.

As a result, some programming languages that emphasize performance are either *not* memory safe or have a way to disable memory safety. The widely-used programming languages C and C++ are *not* memory safe. There are also some languages emphasize performance that are *normally* memory safe, but have a way to disable safety checks to enable adequate performance; these include Rust (when using unsafe code), C# (when using unsafe code), and Ada (when using pragma suppress to suppress memory safety checks).

Memory safety problems are a common cause of vulnerabilities. Catalin Cimpanu’s study, [*Microsoft: 70 percent of all security bugs are memory safe issues*](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/) (2019), found that about ~70% of all Microsoft vulnerabilities in 2006-2018 were due to memory safety issues. What is more, while there are annual fluctuations, it has been relatively stable over that time:

![Memory safety has been consistently a vulnerability over time](../../memory_safety_over_time.png)

**Percentage of memory-safety vulnerabilities at Microsoft** (by Catalin Cimpanu, 2019, retrieved from [ZDNet](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/))

Memory safety is a subset of a larger category called *undefined behavior*, where the system guarantees nothing - and undefined behavior often leads to security vulnerabilities. We will discuss this more later, but we will briefly note that C and C++ have a remarkably large number of undefined behaviors, making it especially difficult to write secure software in these languages.

You can have these problems *even if* you write code in a language that is memory-safe and has no undefined behaviors. Your code might call some *other* code with undefined behavior that leads to vulnerabilities. Since almost every program ends up calling out to at least some code written with C or C++, that means at least some parts of your program might be indirectly vulnerable, even if your program is not written in C or C++.

One of the best-known attacker tricks is out-of-bounds reads and writes (including *buffer overflows*) - so we will briefly talk about what that is and how to counter it. We will then discuss another kind of flaw that often leads to security vulnerabilities, double-frees. Finally, we will discuss the larger category of undefined behaviors.

#### Out-of-Bounds Reads/Writes and Buffer Overflow

One of the most common kinds of security vulnerabilities is where a read or write is *“out of bounds”* inside memory-unsafe code. Such vulnerabilities are common, and attackers find them easy to exploit. This problem has been well-known for a long time; Aleph One (Elias Levy) describes in detail in [*Smashing the Stack for Fun and Profit*](http://phrack.org/issues/49/14.html#article) (1996) how to exploit such vulnerabilities.

In fact, out-of-bounds reads and writes are so common and dangerous that in the 2019 CWE Top 25 Most Dangerous Software Errors list this is the #1 weakness ([CWE-119](https://cwe.mitre.org/data/definitions/119.html) *Improper Restriction of Operations within the Bounds of a Memory Buffer*), and specific cases of it are #5 ([CWE-125](https://cwe.mitre.org/data/definitions/125.html) *Out-of-bounds Read*) and #12 ([CWE-787](https://cwe.mitre.org/data/definitions/787.html) *Out-of-bounds Write*).

Here are the fundamentals. Almost all programs have to store intermediate results, and such storage areas are often called *buffers*. Reading and writing within that buffer is fine. But what happens when your program tries to read from or write to that buffer, but it tries to do that outside the range of that storage area? For example, here is a trivial fragment of a C program that allocates some array **x** of size 10 (index values 0 through 9), and later stores the value of **y** to the index value **i** of that array:

~~~~C
    char x[10];
    ...
    x[i] = y;
~~~~

What happens if the value of **i** is out of bounds (that is, has a value other than 0 through 9)? There are two safe and common options that happen in different programming languages:

1. **Resize**
In many programming languages, trying to write (or read) out of bounds will resize the array so that the value can be stored or read from.

2. **Error**
In some languages, particularly those focused on excellent performance, an error (usually an exception) will be reported if the index is out of bounds.

Unfortunately, there is a third option: an out-of-bounds read or write can be accepted and turned into a potential security vulnerability. If you use a memory-unsafe language such as C, C++, or assembly language, then any read or write that can go out-of-bounds is a potentially dangerous security vulnerability. This problem can also happen if the language is normally memory-safe, but you disable the language’s memory safety checks (such as Rust, C#, and Ada).

In C, any attempt to read or write outside the bounds of a buffer (via an array index or a pointer) is an example of *undefined behavior*. If a C program will eventually execute a statement that will cause undefined behavior, the code is allowed to do anything at all at any time - even before that statement that caused the undefined behavior! You can find more information in the following references:

* [*With Undefined Behavior, Anything is Possible*](https://raphlinus.github.io/programming/rust/2018/08/17/undefined-behavior.html) (2018), by Raph Levien

* [*Undefined behavior can result in time travel (among other things, but time travel is the funkiest)*](https://devblogs.microsoft.com/oldnewthing/20140627-00/?p=633) (2014), by Raymond Chen

* [*A Guide to Undefined Behavior in C and C++ (Parts 1-3)*](http://blog.regehr.org/archives/213) (2010), by John Regehr.

In *practice*, if there is no memory safety, a write outside a buffer in most programming language implementations often ends up corrupting internal data structures that the program depends on. For example, it may overwrite local variables and/or change what will be run after a function returns. Similarly, a read outside a buffer often reveals internal information that is not normally revealed, including secrets that security (such as keys or hardening systems) depend on. In addition, if it is C or C++, compilers will often use such statements as a license to generate some very surprising machine code (because compiler authors are allowed to presume that such things will not happen). Attackers have honed their craft over decades to exploit these vulnerabilities, because they are common and they can often quickly turn discovery of this kind of vulnerability into a devastating attack.

There are many names for these attacks, with varying terminology and meanings. One of the most common variations of this vulnerability is when the attacker can write past the end of an array, and this vulnerability is sometimes called a *classic buffer overflow* vulnerability. An attack that exploits this vulnerability by writing data outside a buffer is often called a *stack smashing attack* (if the buffer is on the stack, such as by being a local parameter) or a *heap smashing attack* (if the buffer is on the heap, that is, was previously allocated by **new** or **malloc** depending on the language). CWE has various identifiers and names, including [CWE-119](https://cwe.mitre.org/data/definitions/119.html) (*Improper Restriction of Operations within the Bounds of a Memory Buffer*), which is a special case of [CWE-118](https://cwe.mitre.org/data/definitions/118.html) (*Incorrect Access of Indexable Resource (‘Range Error’)*).

If an attacker can cause your program to write outside its buffer, this often results in a serious vulnerability where the attacker can cause the program to do anything at all.

Unbounded writes are not the only problem. Historically, people worried about out-of-bounds writes more than reads, but the Heartbleed vulnerability in 2014 showed that out-of-bounds reads could also be extremely dangerous. Out-of-bounds reads can reveal information that allow attackers to completely break into a system. Even programs that only allow one byte of an out-of-bound read or write can have a dangerous vulnerability.

![image alt text](../../heartbleed.png)

**Heartbleed Explained**. Retrieved from [xkcd](https://xkcd.com/1354/), provided under [CC-BY-NC-2.5](https://creativecommons.org/licenses/by-nc/2.5/) 

STORY TIME: Heartbleed

In 2014 a vulnerability named Heartbleed ([CVE-2014-0160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2014-0160)) was found in the widely-used OpenSSL cryptographic library.  The key weakness was a buffer over-read (past the end of the buffer) was allowed in the heap due to improper input validation. This vulnerability allowed attackers to acquire sensitive data, and OpenSSL managed some extremely sensitive data such as server private keys. This vulnerability affected a huge number of popular websites, leading to problems such as user account hijacking and information compromises of millions of patients. ([*How to Prevent the next Heartbleed*](https://dwheeler.com/essays/heartbleed.html), 2020, by David A. Wheeler)

#### Solutions for Out-of-Bounds Reads and Writes

If you are curious, there are many papers and college courses that go into depth on exactly why this problem is so dangerous. But if you are just developing software, those details do not matter - you simply need to make sure that reads and writes are always within the bounds of what they are supposed to refer to. So how can we do this?

The simplest solution: **_always, where practical, use memory-safe languages and keep memory safety on_**. Almost all programming languages are memory-safe, at least by default. If you try to access a buffer outside of its bounds in a memory-safe language, it will resize the buffer or give you an error (typically an exception). In either case, the system doesn’t just cede control to an attacker. This solution is easier to apply when you are writing code from scratch, of course.

But sometimes this is not practical. This means you could never use C, C++, or assembly language. It would also mean you could not ever disable memory-safety in other languages. There are many large programs in C or C++ that would be difficult to rewrite, and of course, there are reasons people choose those languages. Most operating system kernels are written in C, since they are performance-critical and C was specifically designed for this task. Similarly, in languages that let you disable memory safety, there are reasons those mechanisms exist.

If you *must* have code without memory-safety, try to limit what is memory-unsafe where that is practical. For example, in languages that are memory-safe by default, but have mechanisms to disable it, you should minimize the amount of code that runs without memory safety. A large library in Rust, C#, or Ada should be almost entirely safe, with at most a very small unsafe portion. If you have a lot of existing C or C++ code, consider rewriting a portion in a memory-safe language. If you rewrite a portion, you should typically focus on the *most dangerous* portion (that is, code that is most exposed to attackers). For example, Mozilla’s Firefox browser was written mostly in C++ (and some JavaScript), but in 2017 some of that C++ code was replaced by implementations in Rust, and increasingly more and more of Firefox is written in Rust (Mozilla [*Oxidation*](https://wiki.mozilla.org/Oxidation) and [*Rust vs. C++ in macOS Firefox Nightly*](https://docs.google.com/spreadsheets/d/1flUGg6Ut4bjtyWdyH_9emD9EAN01ljTAVft2S4Dq620/edit#gid=885787479)).

If you have to program without memory safety checks, for whatever reason, then you have to carefully implement all the checks in the code itself. For security, you must make sure you never ever make a mistake: you must ensure that every reference is in bounds no matter what the attacker does. Each check is not hard to do; this is not rocket science. The problem is that never ever making a mistake is difficult to do. You can be very smart and still make a mistake. If you do write software without memory safety checks, where possible, you should use mechanisms like tools and peer review to reduce the risks of something slipping through to users. Later on we will discuss some of the tooling available to help.

Of course, just doing a check is not enough - what do you do when the check fails? The safest thing to do is to reject the input and not perform any action if a check fails along the way. However, it is often hard to do the rejection, and so developers are tempted to simply trim off any extra (or write code that accidentally does this). Sometimes that is fine, but this often means that an attacker can control what stays in the buffer and what doesn’t. That can sometimes lead to vulnerabilities, and determining if there is a vulnerability can be really difficult.

If you use C, there are many patterns that are especially likely to be vulnerable, including the use of functions like **strcpy()** to copy a string, **strcat()** to concatenate a string, and loops that incrementally add to a buffer. Early in C’s development, functions were created that limited where data would be written, specifically **strncpy()** and **strncat()**. However, using **strncpy()** and **strncat()** requires constant recalculation of the *space left over*, making them difficult to use correctly (it is extremely easy to have an “off by one” error in this code that only attackers notice). The **strncpy()** function also overwrites all remaining space, making it absurdly inefficient for most circumstances.

If you use C, sometimes you can use safer functions instead. The C function **snprintf()** writes output to a string buffer given a format, and it will not overwrite past a given length. The function **memccpy()** lets you do a simple copy, again without going beyond a maximum length. However, in all these cases you cannot just call the function - in most cases, you also have to check its return value to see if there was an overrun, and if there was, do something sensible (which is usually to stop processing the input). The functions **asprintf()** and **vasprintf()** let you reallocate a new string, which you can use to resize a string. As always, you must ensure that you free any previously-allocated strings once they are no longer used, and ensure that you only free them once (a problem we will discuss more soon). If you are not prepared to do this very carefully and methodically, you probably should not be using C.

Modern compilers for these languages, and the operating systems that support them, use a variety of hardening techniques to make exploiting these attacks harder. Widely-applied hardening measures include:

* Address Space Layout Randomization (ASLR)
Randomize where objects are stored in memory, making it harder for attackers to target some objects (in the gcc and clang compilers you may need to enable PIE mode, e.g., using **-fPIE**)

* Non-executable memory
Ensure that memory with executable instructions cannot also be written to at the same time, making it slightly harder for attackers to modify software or introduce their own malicious code.

* Canaries
Insert an extra check in selected functions; before they return, they do a sanity check on a value called a “guard” or “canary” that detects certain kinds of buffer overflows that perform writes (the gcc and clang compilers can do this with options like **-fstack-protector**)

* Automated bounds insertions
Modify code during compilation to do bounds checking even if was not originally requested (the gcc and clang compilers can do this with the option **-D_FORTIFY_SOURCE=2**).

If you are writing code that is not memory-safe, or calling code that is not memory-safe, make sure hardening measures like these are enabled whenever you can, including in compilation, test, and production. The good news is that hardening measures like these will slow down some exploits. But in the end, hardening measures often do not *prevent* exploits. In the best case, these hardening measures turn “take over program” into “program stops working”... and that is the *best* case. The only way to not have vulnerable code… is to not have vulnerable code.