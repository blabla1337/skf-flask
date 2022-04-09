### Complete Mediation (Non-Bypassability)

Every time a program gets a request, at least from a source the program cannot completely trust (it is outside the trust boundary), the program must check the request. Examples of security checks are checking that the request is authorized and that the input is valid before you act on that data. This principle is also called *non-bypassability*, because the point is that it must not be possible for an attacker to bypass security checks.

A common mistake is to try to run security checks on a system that the attacker can control. If an attacker can control a system, then the attacker can easily bypass all security checks run by that system. Let’s look at some examples of *insecure* designs.

#### Insecure Design: Client-side HTML Input Validation

A simple example of an insecure design is when a server-side web application sends some HTML to a client, and the HTML includes some validation requirement. For example, the HTML might include the following statement to require that the maximum length be no more than 100:

~~~~html
    <input id="name" type="text" maxlength="100">
~~~~

This HTML is fine if its purpose is to be a quick check to counter accidental mistakes. But since attackers can control their own web browser, this maximum length check is trivial to bypass. An attacker can easily send a much longer input. You cannot *depend* on the web browser to do any security-relevant checking for you if the attacker could control or replace the web browser.

#### Insecure Design: Client-Side JavaScript/WASM Input Validation

A related and common insecure design is where code is sent to web browsers, for example, as JavaScript or WebAssembly (WASM), and that code does security checks before sending its data to a server. In most situations, an attacker can control the web browser, while the server is under your control, so again, you cannot trust anything the web browser does. Put another way, any security checks in the code sent to the browser can be trivially bypassed by an attacker, since attackers control their own web browsers. A related problem is providing direct database access to untrusted users. Often users do not need full access, so this is giving users far more privilege than they need (violating least privilege), and such access can make it harder to prevent bypassing security checks. The following figure shows this mistake:

![Insecure design: In this figure security-relevant input validation checks are run in a web browser, and not run again by the web server. Since the attacker can control their own web browser, this is insecure. The database is also directly accessible by logged-in users; this is a bad sign, because this grants a lot of data access that is often unnecessary.](../../insecure_design.png)

An Insecure JavaScript Application

#### Secure Design: Input Validation on an Environment You Can Trust

You can use JavaScript securely, you just need to do it correctly. You can send JavaScript to the client, and you can do some security-relevant checks in the browser (say, to give quick feedback). But if attackers could control some web browsers (but not the servers), the browser-side security checks are irrelevant for security. In this common case, you have to do all security-related input checks in the servers, even if some of the checks were supposed to be done on the client and are now being “redone”. The input checks (validations) are not really being redone, because the client-side ones could not be trusted.

The following figure shows a similar but secure design; notice that all the security-related checks are being done in the server, since in this case that is the system we can trust. It also prevents direct database access, which is often a good idea if users do not need direct access:

![A More Secure Alternative of the JavaScript Application: In this figure some security-relevant input validation checks are run in a web browser, but all security checks are run by the web server, even if some were run in the browser earlier. Since the server in this case is trusted, this is a secure design. The database is not directly accessible by logged-in users; this is a good architecture, because direct access to the database is often unnecessary.](../../secure_design.png)

A More Secure Alternative of the JavaScript Application


#### Insecure Design: Mobile Application with Client-Side Checking

A similar common insecure design is code in smartphone mobile applications that does all the security checks before sending its data to a server. Again, we cannot assume that any security checks in the mobile application will actually be made. An attacker could modify the mobile application, or write a different application, to bypass any checks made in the mobile application. If you are writing a smartphone mobile application, you also normally cannot trust the other applications - the other applications may themselves be malicious!

#### Insecure Design: Client Application Depending on Untrusted Server

Don’t be confused; the message is not *“server good, client bad”*. The issue is that in almost all cases, any code you need to trust must run in an environment you can trust.

If you’re writing a web browser, for example, you will need to trust the local operating system services, but you certainly cannot trust arbitrary remote web servers - some of those remote web servers may send you malicious data!

#### The Key: Run Code You Must Trust in an Environment You Can Trust

In short: any code you need to trust must (in most cases) run in an environment you can trust, *not* on a system potentially controlled by an attacker.

You can use client-side JavaScript, client-side WebAssembly, and mobile applications - that is not the problem. You can write web browsers, too! The problem is trusting a system that might be under the control of an attacker. If you have a web-based client-server system, for example, generally the code that runs on the server (that you control) must do all the security checking. After all, attackers can build or modify their own web clients, including any JavaScript sent to their client by a server. It is fine to run checks on a system you don’t fully trust if you want to provide rapid response for unintentional mistakes. But that is not enough - for security, all security checks have to be done (or redone) on a system that you can fully trust. You can run those server-side checks using JavaScript, WebAssembly, or anything else that you trust - but you have to run the checks on a system you can trust.

Some developers try to run code on systems they cannot trust by using obfuscation. That is, they will use tools that try to make it harder to understand the code sent to a system they cannot trust. An example of this is using JavaScript minification and hoping that it will make the client code hard to figure out. Don’t do that! JavaScript minification’s purpose is to reduce the number of bytes sent over a network, not to hide what the code does or to prevent changing it.

What can be obfuscated can be de-obfuscated, and it is remarkably easy for attackers to de-obfuscate information. Many tools exist that can quickly de-obfuscate information. Trying to run code you need to trust on systems you cannot trust is best avoided.

It is much better to run software you need to trust on a system you can trust; then the software just works all the time.

#### Warning Signs

Building a system with security checks that can be bypassed is a dangerous mistake. Not only does it mean the system is insecure, but it is often very difficult to fix this mistake once you make it. You might have to rewrite a lot of software to fix this mistake. Here is a quick checklist of things to look for that might indicate these kinds of mistakes:

* HTML or other data format sent to a client that performs security-relevant input validation on a system an attacker might control. This could be fine, but only if all of those checks are re-performed in a trusted environment.

* JavaScript or other code sent to the client that does input validation or other security-relevant operations on a system an attacker might control. This could be fine, but only if all of those checks are re-performed in a trusted environment.

* A mobile app that does security-relevant input validation. This is the same client-side issue.

* A database that is directly accessible via the network for use by a client application (web browser, mobile app, etc.). This can be secure, but you must ensure that all operations the user is allowed to perform are authorized. In many systems, you can control this with the SQL GRANT command, if you need to do this. However, it is often better (or necessary) to mediate access using a program instead of providing direct access to a database. Direct database access can make it harder to do input validation. It often violates least privilege, since often the user does not need full access to the database. If you do provide direct access to a database, consider limiting the privileges. For example, you might grant access to only a read-only view instead of the entire database.

* A network communication channel that an attacker can hijack. Properly-implemented network connections that use TLS (such as **https:**) and SSH resist hijacking; almost everything else does not. Software may communicate over the channel assuming that it is talking to the same user/software, but this is easily bypassed if the channel can be hijacked.

#### Trying to Run Software You Must Trust in Untrustworthy Environments

*Could* you try to run software that you need to trust on a system you don’t trust? You can try, but that generally works out badly, and trying to do it is a highly advanced topic. Here are some of the techniques that have been tried:

* One technique is homomorphic encryption. This lets you run code while data stays encrypted. But currently homomorphic encryption is only practical for specialized circumstances. It is orders of magnitude slower and far more complex.

* Intel’s Software Guard eXtensions (SGX) CPU mechanisms are supposed to enable execution and data storage, but in practice they have been repeatedly broken ([*Plundering of crypto keys from ultrasecure SGX sends Intel scrambling again*](https://arstechnica.com/information-technology/2020/06/new-exploits-plunder-crypto-keys-and-more-from-intels-ultrasecure-sgx/), by Dan Goodin, 2020).

* If you are trying to secure games on a laptop/desktop, and you don’t trust the laptop/desktop, there are anti-cheat systems. But anti-cheat systems are routinely broken. You are better off having physical events where all the laptops/desktops are owned by you.

In general, you are better off with simple solutions that do not involve trying to trust systems controlled by attackers.