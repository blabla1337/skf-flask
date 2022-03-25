### Handling Errors

Real programs must handle errors. Many production programs are *mostly* error-handling, because there are so many problems that can happen in the real world.

Poor error handling can lead to security vulnerabilities. So let’s discuss common approaches to error handling and how to use them securely. Basically, this involves understanding their strengths and weaknesses, and being cautious about their weaknesses when using them.

STORY TIME: Apple **goto fail; goto fail;**

An example of a security vulnerability caused by bad error handling is [CVE-2014-1266](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-1266), commonly called the “*goto fail; goto fail;*” vulnerability. This was a vulnerability in the Apple implementation of the SSL/TLS protocol in many versions of its operating systems. The problem was a second (duplicate) “**goto fail;**” statement in the function **SSLVerifySignedServerKeyExchange**, as follows:

~~~~C
    if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
      goto fail;
    goto fail;
    ... other checks ...
    fail:
      ... buffer frees (cleanups) ...
      return err;
~~~~

> The indentation here is misleading; since there are no curly braces after the **if** statement, the second “**goto fail**” is always executed. In context, that meant that vital signature checking code was skipped, so both bad and good signatures would be accepted. The extraneous “**goto**” caused the function to return 0 (“no error”) when the rest of the checking was skipped; as a result, invalid certificates were quietly accepted as valid. This was a disastrous vulnerability, since it meant that all sorts of invalid certificates would be accepted, completely compromising security. This vulnerability would be easily detected by an automated test suite. ([*The Apple goto fail vulnerability: lessons learned*](https://dwheeler.com/essays/apple-goto-fail.html), by David A. Wheeler, 2020).

#### Return Codes

One of the most common error-handling mechanisms are return codes. A return code is simply a single value that is *either* the return value of a method/function/procedure or a value that indicates an error. For example, “on success returns 0..INT_MAX, on error returns -1” or “on success returns a pointer, on error returns NULL”. In some cases, nothing is being returned (at least as its return value), so the return value is simply whether or not there was an error. Return codes are the usual approach in C, but return codes are used in many programming languages.

Obviously, when you are developing a program, you need to ensure that the return code is not a legitimate value, so that errors and normal values *can* be distinguished.

Return codes work, but they have many problems when maintaining software over time:

* They require the caller to check every return value for an error to handle it. These are easy to forget, and thus this is a common mistake.

* Every method may have different semantics (e.g., different values to indicate “error”). They are often **0**, **negative**, **INT_MAX**, **NULL**, or some other special value… but not always.

* If new types of errors are added, you must often check every caller to ensure they are handled correctly.

* They lead to functional logic and error handling being mixed together. This often creates more complex code, leading to mistakes and poorer productivity. In particular, such code often fails to deallocate resources if it must do so.

In most programming languages it is often better to use another mechanism (like exception handling) instead when you are creating the interface, because return codes so easily lead to mistakes over time. This is not practical in portable C, since C does not have many other mechanisms (e.g., C does not have a standard exception handling mechanism). So, if you are using C, consider moving the error handling to the end of the function. This separates error-handling from the functional logic and simplifies correct resource deallocation. A good explanation of this approach is in the [Linux kernel coding style guide](https://www.kernel.org/doc/Documentation/process/coding-style.rst).

When you are using an interface that uses return codes, make certain that you check every time there’s a return code if a failure might lead to a vulnerability. For example, about 35 billion Internet of Things (IoT) devices were found in 2021 to have disastrous security vulnerabilities due to inadequate cryptographic random number generation. This is in part because many IoT software developers directly called hardware random number generators (they shouldn’t do that), but even worse, they ignored error return codes from those generators (and they definitely shouldn’t do that). For more details about this example, see [You're Doing IoT RNG](https://labs.bishopfox.com/tech-blog/youre-doing-iot-rng) ([presentation](https://www.youtube.com/watch?v=Zuqw0-jZh9Y)) by Dan Petro and Allan Cecil, a 2021 DEF CON presentation. We’ll discuss cryptographic random number generation in more detail later.

#### Exceptions

Most programming languages have an *exception handling mechanism* (though there are, er, exceptions!). This includes such diverse languages as Java, C#, Python, PHP (5+), Perl, Ruby, Tcl, JavaScript, C++, Ada, Smalltalk, Common Lisp, Scheme (6+), Erlang, and OCaml. In such systems, you can “throw” or “raise” an exception when an error is detected, and you can “catch” or “rescue” an exception to handle it; the stack is repeatedly unwound when an exception is thrown until there is a matching catch. Many languages define regions to catch (e.g., “try”).

If you are implementing the *top* level of a program or framework (e.g., its main event loop), you typically want to catch all exceptions (with perhaps a few, er, exceptions). Log the exception (with some details, except information like passwords that perhaps should be omitted from the log). Ensure that after the request or event has completed, including when an exception has been processed, that all resources have been returned if they should be. Finally, repeat the event loop to process the next event. Logging can aid debugging and intrusion detection. It is fine to tell the requestor that “there was a problem” while not providing many details; that is what the internal log is for.

Otherwise, you generally should be specific about the exceptions you catch, and only catch an exception if you can do something appropriate about it. Attackers will try to trigger exceptions, so make sure that exception handlers are secure.

#### Other Approaches

There are other error-handling approaches.

Some programming languages use type constructors that provide a return value that distinguishes normal values from error values. A good example of this is Haskell’s **Maybe**, which is defined as “**data Maybe a = Nothing | Just a**”. This means that a **Maybe** value must be either **Nothing** or **Just** a value. This approach is like an error return, but, because the type system distinguishes value from errors (non-values), you cannot accidentally ignore errors; you have to extract the value to get a result. Some programming languages also provide constructs to easily do this extraction and otherwise propagate the error, e.g., the [“?” operator in Rust](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html) and [optional chaining in Swift](https://docs.swift.org/swift-book/LanguageGuide/OptionalChaining.html). Of course, you could intentionally write code to skip the error value (e.g., **Nothing**); beware of doing so if this could have a security impact.

Some languages allow multi-value returns and use that for error handling. For example, Go’s error conventions do this. Functions can return multiple values, and one of them can be an error value. This avoids the risks of overloading values as compared to traditional return values. However, like return values, there is a risk you will forget to check the separate error return value. For more details, check out [*The Go Blog: Error handling and Go*](https://blog.golang.org/error-handling-and-go) (2011), by Andrew Gerrand.

#### Error Handling Wrap-up

Error-handling is a fact of life, but you need to make sure your error handling (not just your “main” line) is secure. It is easy to forget to detect or handle errors. Where you can, try to use approaches that are more likely to work correctly *even* as the program is changed by others.