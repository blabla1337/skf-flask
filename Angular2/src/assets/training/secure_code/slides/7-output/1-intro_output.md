# 4. Sending Output

This chapter describes how to send output securely, including how to counter cross-site scripting (XSS) attacks, using HTTP hardening headers, and securely using formatting systems.

Learning objectives:

1. Discuss how to securely send output.

2. Explain how to counter Cross-Site Scripting (XSS) attacks.

3. Use HTTP hardening headers, including Content Security Policy (CSP).

4. Explain how to prevent other common output-related vulnerabilities in web applications.

5. Understand how to securely use format strings and templates.

6. Understand how to address other common output-related vulnerabilities.

### Introduction to Sending Output

Eventually, programs need to send output somewhere. It could be a reply to a request, a display to a user, storing information in a database, or anything else that returns a result.

Everything we learned about sending information to other programs also applies here. For example, you will often need to be sanitizing, escaping, and/or normalizing the output you send back to some user.

A quick rule-of-thumb is that you should try to minimize the information your program shows to an untrusted user, especially if it is security-related:

* If your program requires some sort of user authentication (such as many with a network connection), give the user as little information as possible before they authenticate. In particular, avoid giving away the version number of your program before authentication, unless this is easy to find anyway or it is the only instance of the program. Otherwise, if a particular version of your program is found to have a vulnerability, then users who don’t upgrade from that version advertise to attackers that they are vulnerable.

* If a login fails, note that it failed, but in general don’t say why. For example, don’t say that the username is wrong, unless the attacker can get usernames anyway as public information. Never say a password is “almost” correct; it is correct or it is not.

* Don’t show passwords on the screen by default. For example, in HTML, use the “password” data type, because that normally replaces each password character with a dot. Otherwise, an attacker shoulder-surfing behind the user could get this information, or the information might accidentally be revealed by a user making a video.

* If you must display some sensitive information in a form, make that a separate page or have a button that can hide/reveal that information. Try to make hiding the sensitive information the default. Again, this helps counter shoulder-surfing and accidental revelation of information.

* Minimize inline code comments sent to users; this wastes network traffic and might accidentally reveal information. If you are using JavaScript, minification can help prevent this.

Your program should also be prepared to handle attackers who intentionally reject or very slowly accept the output. Otherwise, an attacker might be able to make your program unresponsive to other users, simply by clogging some output. Implementations that use asynchronous communications are usually much less vulnerable to this, but any implementation *can* have this problem. Basically, make sure an attacker cannot clog a system by halting or slowing their web browser, having an intentionally slow TCP/IP connection, and so on. In short, don’t create an easy opportunity for a Denial-of-Service attack. Here are some tips:

* Release locks quickly, preferably before replying with *any* output.

* Use timeouts on network-oriented writes.

* Measure the time from the start of your attempt – it is ok to halt in the middle if it is suspiciously slow.

You should follow the standing conventions of the system you are using where possible, since often other components depend on that. In particular, on the web, the **GET** and **HEAD** methods of HTTP should not take any permanent action by themselves; they should be just retrieving information. The **GET** method, in particular, can be caused by a simple click on a hyperlink in a static page, and should not involve anything permanent like buying or selling. Instead, use other methods (like **POST**, **PUT**, and **DELETE**) to indicate permanent changes. The HTTP protocol can’t enforce this, but it is the standard convention, and many tools assume it, so you should also apply this rule where practical.

Make sure that you tell the receiver exactly how to interpret the output. Otherwise, if it includes data from an attacker, the attacker might be able to fool the recipient into interpreting it the wrong way. This is an especially common problem in web applications:

* Clearly state the MIME type of the data that is being sent. Browsers can guess, but they may guess wrong.

* Clearly state the character encoding of the output that is being sent. Don’t make the receiving program guess the character encoding! If the receiving program (typically the web browser) has to guess, the attacker may fool your system into sending material that leads to a wrong guess and eventually an attack. If you are sending HTML, usually you should tell the recipient that it is UTF-8. The best way to do that is via the HTTP **charset** option, which you can often do with a simple configuration option. If you cannot control that for some reason, include that information in the HTML **&lt;head&gt;**, e.g., **&lt;meta http-equiv="Content-Type” content="text/html; charset=UTF-8"&gt;**.

More generally, you often need to **_escape your output_** so that any data you generate that might be influenced by an attacker cannot become an attack. This is an especially common problem in web applications. One of the most common vulnerabilities in web applications is called *Cross-Site Scripting* (XSS). This problem is all about not sending output properly and, in particular, about escaping output correctly. The next unit will explain the vulnerability and how to deal with it.