# 2. Processing Data Securely

This chapter describes how to process data within software with security in mind, including treating untrusted data as dangerous, avoiding default and hardcoded credentials, avoiding memory safety issues (such as buffer overflows), and avoiding undefined behavior.

Learning objectives:

1. Discuss how to process data securely (e.g., treat untrusted data as dangerous).

2. Understand the importance of avoiding default and hardcoded credentials.

3. Discuss memory safety and the problems when it is not present: out-of-bounds reads/writes, double-free, use-after-free.

4. Understand avoiding undefined behavior.

## Processing Data Securely: General Issues

### Prefer Trusted Data. Treat Untrusted Data as Dangerous

Of course, once your software gets data, it needs to process that data.

If it matters, make sure you process your data by using an environment you can trust. Just like input validation, if you care about the answer after data processing, you need to process your data on a system you can trust. If you process data using a script on a web browser or a mobile application and that web browser or mobile application might be controlled by an attacker, then you cannot trust anything that it does; all that data will be visible to the attacker and the attacker might force different results. If attackers can only attack themselves, that is not a problem, but make sure it is limited to that. If an untrusted system processes some data, and sends the result to you, you need to treat it as untrusted data.

Which leads us to a useful rule-of-thumb: *whenever given a choice, try to use the more trusted data.*

An example might help. Many systems, when sent a password reset request, send an email to confirm the password reset. At one time GitHub would ask an untrusted user for their email address. If that matched an email address in their database, ignoring upper/lower case distinctions using the rules of English, GitHub would send the password reset to the email address *as provided by the attacker*. This was a terrible idea. Email standards do not guarantee that the local part of the email address (the part before the **@** symbol) is case insensitive (see [IETF RFC 5321 section 2.3.11](https://tools.ietf.org/html/rfc5321#section-2.3.11)). By converting the email address to lower case, there is no guarantee that the reset would be sent to the correct email address. Many email systems do ignore upper/lower case distinctions, but they might not use English! In some Turkic email systems, the local part of the email address would normalize to a *different* distinct email account than the original account. For example, **MIKE@example.org** would normalize to **mıke@example.org** (using a dotless i), which would be a different email account from **mike@example.org** (which uses a dotted i). This led to an exploitable vulnerability (GitHub Security, [*Password reset emails delivered to the wrong address*](https://bounty.github.com/researchers/jagracey.html), 2016).

This attack seems subtle, but this is a clear violation of our basic rule of thumb: if you have more trusted data available, try to use *that* more trusted data! For example, if you have a password reset request, and you want to send an email to confirm that the originally-confirmed user authorized it, you should send the reset email to exactly the *already confirmed* email address in your database. You have already confirmed that is the correct email address, so you can place more trust in it. This simple rule - *try to use the more trusted data* -  will avoid many subtle attacks without you even realizing it.

However, many applications do have to process untrusted data. In that case, when you have to process untrusted data, treat it as **_radioactive_** - that is, be careful when you process it in any way, remembering that it might be from an attacker. There are many ways you need to be careful, as we will discuss.